# Mahek Fashion's Showroom

A premium e-commerce showroom website for **Mahek Fashion's**, a leading ethnic wear boutique located in Meena Bazaar, Bur Dubai. This platform showcases an exquisite collection of Pakistani Kurtis, luxury Sarees, and traditional bridal wear.

## Key Features
- **Modern UI/UX**: Designed with a high-end glassmorphism aesthetic and 3D interactive navigation.
- **Dynamic Gallery**: A curated product gallery featuring 24+ unique female fashion items.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop viewing.
- **Tech Stack**: Built using Flask (Python), Jinja2, and custom CSS3/JavaScript.

## Deployment on Render
This project is configured for deployment on Render.
1. Connect your GitHub repository to Render.
2. Use the following settings:
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn mahek_fashions.app:app`

## Local Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python mahek_fashions/app.py`
