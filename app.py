from flask import Flask, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from blueprints.accounts.login import login_bp
from blueprints.accounts.register import register_bp
from blueprints.accounts.myaccount import myaccount_bp
from blueprints.helps.faqs import help_bp
from blueprints.carts.cart import cart_bp
import config
import time

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

app.config['DEBUG'] = config.DEBUG
app.config['ENV'] = config.FLASK_ENV
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)
 
# Inicializando os controllers passando o blueprint
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(myaccount_bp)
app.register_blueprint(help_bp)
app.register_blueprint(cart_bp)

# rota inicial
@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
# rotas para API´s
# rota para a api
@app.route('/api/data', methods=['GET'])   
def get_data():
    data = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

