from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Choose a random key for your app

@app.route('/')
def home():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('home.html', screen_width=screen_width)

@app.route('/about')
def about():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('about.html', screen_width=screen_width)

@app.route('/menu')
def menu():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    menu_items = [
    {"name": "Espresso", "price": "$3.00", "image": "images/espresso.jpg"},
    {"name": "Cappuccino", "price": "$3.50"},
    {"name": "Americano", "price": "$2.50"},
    {"name": "Latte", "price": "$4.00"},
    {"name": "Mocha", "price": "$4.50"},
    {"name": "Macchiato", "price": "$3.75"},
    {"name": "Flat White", "price": "$4.00"},
    {"name": "Ristretto", "price": "$3.25"},
    {"name": "Cortado", "price": "$3.75"},
    {"name": "Doppio", "price": "$3.50"},
    {"name": "Cold Brew", "price": "$4.50"},
    {"name": "Iced Coffee", "price": "$4.00"},
    {"name": "Frappuccino", "price": "$5.00"},
    {"name": "Nitro Cold Brew", "price": "$5.50"},
    {"name": "Café au Lait", "price": "$3.75"},
    {"name": "Affogato", "price": "$4.25"},
    {"name": "Viennese Coffee", "price": "$4.50"},
    {"name": "Turkish Coffee", "price": "$4.00"},
    {"name": "Café Breve", "price": "$4.25"},
    {"name": "Café Con Leche", "price": "$3.75"},
    {"name": "Café Corretto", "price": "$4.50"},
    {"name": "Café Cubano", "price": "$3.50"},
    {"name": "Long Black", "price": "$3.00"},
    {"name": "Lungo", "price": "$3.25"},
    {"name": "Galão", "price": "$4.00"}
]

    return render_template('menu.html', items=menu_items, screen_width=screen_width)

@app.route('/contact')
def contact():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('contact.html', screen_width=screen_width)

@app.route('/buynow')
def buynow():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('buynow.html', screen_width=screen_width)






if __name__ == '__main__':
    app.run(debug=True)
