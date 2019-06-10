from flask import Flask, render_template
app = Flask(__name__)

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

if(__name__ == '__main__'):
    app.run(debug = True)
