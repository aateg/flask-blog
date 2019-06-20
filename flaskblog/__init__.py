from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)

# protect against modify cookies and attacks
app.config['SECRET_KEY'] = '3c72ee2b775aff54d0746b9e604c988d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # database

from flaskblog import routes
