from flask import Blueprint, jsonify, render_template

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/mycart', methods=['GET'])
def my_cart_page():
    try:
        return render_template('mycart.html'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
