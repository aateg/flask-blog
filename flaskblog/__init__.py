import os
from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt # para encryptar a senha
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

# protect against modify cookies and attacks
app.config['SECRET_KEY'] = '3c72ee2b775aff54d0746b9e604c988d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # database
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' # verifica se está logado para acessar a rota account
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = '587'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog.users.routes import users
from flaskblog.posts.routes import posts
from flaskblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
