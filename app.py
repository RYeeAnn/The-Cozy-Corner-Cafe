from flask import Flask, render_template, session, redirect, url_for, request, flash

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

    return render_template('menu.html', items=menu_items, screen_width=screen_width)

@app.route('/contact')
def contact():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('contact.html', screen_width=screen_width)

@app.route('/submit_contact', methods=["POST"])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # TODO: Handle the form data (e.g., save it to a database, send an email, etc.)
    # For now, just flash a success message
    flash("Thanks for reaching out, {}! We'll get back to you soon.".format(name), 'success')
    return redirect(url_for('contact'))

@app.route('/buynow')
def buynow():
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('buynow.html', screen_width=screen_width)






if __name__ == '__main__':
    app.run(debug=True)
