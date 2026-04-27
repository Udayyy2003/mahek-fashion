from flask import Flask, render_template, request, redirect, url_for, session
import os
from mahek_fashions.products import products

app = Flask(__name__)
app.secret_key = 'mahek_fashions_secret_key_2024'

# --- Routes ---

@app.route('/')
def home():
    # Show 4 featured products from each category
    featured_kurtis = [p for p in products if p['category'] == 'Kurtis'][:4]
    featured_sarees = [p for p in products if p['category'] == 'Sarees'][:4]
    featured_traditional = [p for p in products if p['category'] == 'Traditional Wear'][:4]
    
    return render_template('home.html', 
                         featured_kurtis=featured_kurtis,
                         featured_sarees=featured_sarees,
                         featured_traditional=featured_traditional)

@app.route('/gallery')
def gallery():
    category = request.args.get('category')
    return render_template('gallery.html', products=products, active_category=category)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# --- Cart Functionality ---

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append({
            'id': product['id'],
            'name': product['name'],
            'category': product['category'],
            'price': product['price'],
            'image': product['image']
        })
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    # Remove the first occurrence of the product with the given ID
    for i, item in enumerate(cart):
        if item['id'] == product_id:
            cart.pop(i)
            break
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Clear cart after order placement
        session.pop('cart', None)
        return render_template('success.html')
    
    cart_items = session.get('cart', [])
    if not cart_items:
        return redirect(url_for('gallery'))
        
    total_price = sum(item['price'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

if __name__ == '__main__':
    app.run(debug=True)
