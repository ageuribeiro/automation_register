from flask import Blueprint

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET','POST'])
def register():
    return "Register Page - Implement your registration logic here"
