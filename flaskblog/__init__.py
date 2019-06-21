from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
from flask_bcrypt import Bcrypt # para encryptar a senha
from flask_login import LoginManager

app = Flask(__name__)

# protect against modify cookies and attacks
app.config['SECRET_KEY'] = '3c72ee2b775aff54d0746b9e604c988d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # database
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # verifica se está logado para acessar a rota account
login_manager.login_message_category = 'info'

from flaskblog import routes
