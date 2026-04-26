from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'mahek_fashions_secret_key_2024'

products = [
    # Pakistani Kurtis (1-8)
    {
        'id': 1,
        'name': 'Embroidered Lawn Kurti',
        'category': 'Kurtis',
        'price': 2500,
        'image': 'images/gallery_1.jpg'
    },
    {
        'id': 2,
        'name': 'Digital Printed Kurti',
        'category': 'Kurtis',
        'price': 1800,
        'image': 'images/gallery_2.jpg'
    },
    {
        'id': 3,
        'name': 'Cotton Silk Kurti',
        'category': 'Kurtis',
        'price': 3500,
        'image': 'images/gallery_3.jpg'
    },
    {
        'id': 4,
        'name': 'Chiffon Party Kurti',
        'category': 'Kurtis',
        'price': 2100,
        'image': 'images/gallery_4.jpg'
    },
    {
        'id': 5,
        'name': 'Mirror Work Kurti',
        'category': 'Kurtis',
        'price': 2800,
        'image': 'images/gallery_5.jpg'
    },
    {
        'id': 6,
        'name': 'Designer Georgette Kurti',
        'category': 'Kurtis',
        'price': 1500,
        'image': 'images/gallery_6.jpg'
    },
    {
        'id': 7,
        'name': 'Formal Office Kurti',
        'category': 'Kurtis',
        'price': 1600,
        'image': 'images/gallery_7.jpg'
    },
    {
        'id': 8,
        'name': 'Daily Wear Kurti',
        'category': 'Kurtis',
        'price': 1400,
        'image': 'images/gallery_8.jpg'
    },
    # Sarees (9-16)
    {
        'id': 9,
        'name': 'Banarasi Silk Saree',
        'category': 'Sarees',
        'price': 5500,
        'image': 'images/gallery_9.jpg'
    },
    {
        'id': 10,
        'name': 'Kanjivaram Silk Saree',
        'category': 'Sarees',
        'price': 8500,
        'image': 'images/gallery_10.jpg'
    },
    {
        'id': 11,
        'name': 'Chanderi Saree',
        'category': 'Sarees',
        'price': 2200,
        'image': 'images/gallery_11.jpg'
    },
    {
        'id': 12,
        'name': 'Paithani Saree',
        'category': 'Sarees',
        'price': 4800,
        'image': 'images/gallery_12.jpg'
    },
    {
        'id': 13,
        'name': 'Bandhani Saree',
        'category': 'Sarees',
        'price': 9500,
        'image': 'images/gallery_13.jpg'
    },
    {
        'id': 14,
        'name': 'Georgette Print Saree',
        'category': 'Sarees',
        'price': 3200,
        'image': 'images/gallery_14.jpg'
    },
    {
        'id': 15,
        'name': 'Organza Floral Saree',
        'category': 'Sarees',
        'price': 3800,
        'image': 'images/gallery_15.jpg'
    },
    {
        'id': 16,
        'name': 'Tussar Silk Saree',
        'category': 'Sarees',
        'price': 4200,
        'image': 'images/gallery_16.jpg'
    },
    # Traditional Wear (17-24)
    {
        'id': 17,
        'name': 'Bridal Lehenga Choli',
        'category': 'Traditional Wear',
        'price': 15000,
        'image': 'images/gallery_17.jpg'
    },
    {
        'id': 18,
        'name': 'Heavy Anarkali Suit',
        'category': 'Traditional Wear',
        'price': 4500,
        'image': 'images/gallery_18.jpg'
    },
    {
        'id': 19,
        'name': 'Designer Sharara Set',
        'category': 'Traditional Wear',
        'price': 3800,
        'image': 'images/gallery_19.jpg'
    },
    {
        'id': 20,
        'name': 'Gown Style Dress',
        'category': 'Traditional Wear',
        'price': 5200,
        'image': 'images/gallery_20.jpg'
    },
    {
        'id': 21,
        'name': 'Palazzo Suit Set',
        'category': 'Traditional Wear',
        'price': 6000,
        'image': 'images/gallery_21.jpg'
    },
    {
        'id': 22,
        'name': 'Punjabi Salwar Kameez',
        'category': 'Traditional Wear',
        'price': 4200,
        'image': 'images/gallery_22.jpg'
    },
    {
        'id': 23,
        'name': 'Straight Cut Suit',
        'category': 'Traditional Wear',
        'price': 4800,
        'image': 'images/gallery_23.jpg'
    },
    {
        'id': 24,
        'name': 'Indo-Western Dress',
        'category': 'Traditional Wear',
        'price': 5500,
        'image': 'images/gallery_24.jpg'
    }
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', products=products)

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'image': product['image']
        })
        session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    for i, item in enumerate(cart):
        if item['id'] == product_id:
            cart.pop(i)
            break
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = session.get('cart', [])
    total = sum(item['price'] for item in cart_items)
    
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        if name and phone and address:
            session.pop('cart', None)
            return redirect(url_for('success'))
    
    return render_template('checkout.html', cart_items=cart_items, total=total)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
