from flask import Flask, render_template, session, redirect, url_for, request, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Remember to keep this key safe and private
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydatabase"
mongo = PyMongo(app)

def get_screen_width():
    """Utility function to fetch screen width from request args or session."""
    return session.get('screen_width', request.args.get('width', type=int, default=320))

@app.route('/')
def home():
    return render_template('home.html', screen_width=get_screen_width())

@app.route('/about')
def about():
    return render_template('about.html', screen_width=get_screen_width())

@app.route('/menu')
def menu():
    drink_items = [
    {"name": "Espresso", "price": "$3.00",},
    {"name": "Cappuccino", "price": "$3.50"},
    {"name": "Americano", "price": "$2.50"},
    {"name": "Latte", "price": "$4.00"},
    {"name": "Mocha", "price": "$4.50"},
    {"name": "Macchiato", "price": "$3.75"},
    {"name": "Flat White", "price": "$4.00"},
    {"name": "Cold Brew", "price": "$4.50"},
    {"name": "Iced Coffee", "price": "$4.00"},
    {"name": "Frappuccino", "price": "$5.00"},
    {"name": "Nitro Cold Brew", "price": "$5.50"},
    {"name": "Affogato", "price": "$4.25"},
]
    pastries_items = [
    {"name": "Croissant", "price": "$2.50"},
    {"name": "Chocolate Eclair", "price": "$3.75"},
    {"name": "Cinnamon Roll", "price": "$2.75"},
    {"name": "Danish Pastry", "price": "$2.50"},
    {"name": "Lemon Tart", "price": "$3.00"},
    {"name": "Blueberry Muffin", "price": "$2.25"},
    {"name": "Macarons", "price": "$4.00"},
    {"name": "Opera Cake", "price": "$4.75"},
    {"name": "Palmier", "price": "$2.25"},
    {"name": "Brioche", "price": "$2.75"},
    {"name": "Madeleine", "price": "$2.00"},
    {"name": "Cannoli", "price": "$3.25"},
]

    return render_template('menu.html', drink=drink_items, pastries=pastries_items, screen_width=get_screen_width())

@app.route('/contact')
def contact():
    return render_template('contact.html', screen_width=get_screen_width())

@app.route('/submit_contact', methods=["POST"])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # Saving to MongoDB
    contacts = mongo.db.contacts  # 'contacts' is the collection name
    contacts.insert_one({"name": name, "email": email, "message": message})
    
    flash(f"Thanks for reaching out, {name}! We'll get back to you soon.", 'success')
    return redirect(url_for('contact'))

@app.route('/buynow')
def buynow():
    return render_template('buynow.html', screen_width=get_screen_width())

if __name__ == '__main__':
    app.run(debug=True)
