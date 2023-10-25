from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Choose a random key for your app

@app.route('/')
def home():
    nav_open = session.get('nav_open', False)
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    return render_template('home.html', nav_open=nav_open, screen_width=screen_width)



@app.route('/toggle-nav')
def toggle_nav():
    session['nav_open'] = not session.get('nav_open', False)
    return redirect(url_for('home',))

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/menu')
def menu():
    nav_open = session.get('nav_open', False)
    screen_width = request.args.get('width', type=int, default=320)
    session['screen_width'] = screen_width
    menu_items = [

        {"name": "Espresso", "price": "$3.00"},
        {"name": "Cappuccino", "price": "$3.50"},
    ]
    return render_template('menu.html', items=menu_items, nav_open=nav_open, screen_width=screen_width)



@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/buynow')
def buynow():
    return render_template('buynow.html')






if __name__ == '__main__':
    app.run(debug=True)
