from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# protect against modify cookies and attacks
app.config['SECRET_KEY'] = '3c72ee2b775aff54d0746b9e604c988d'

posts = [
    {
        'author': 'Gonçalves Silva',
        'title': 'Blog Post 1',
        'content': 'Post Content 1',
        'date_posted': 'June 10, 2019'
    },
    {
        'author': 'Fernandes Gonçalves',
        'title': 'Blog Post 2',
        'content': 'Post Content 2',
        'date_posted': 'June 10, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    login = LoginForm()
    return render_template('login.html', title='Login', login=login)


if(__name__ == '__main__'):
    app.run(debug = True)
