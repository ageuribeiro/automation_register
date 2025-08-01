from flask import Blueprint, render_template, jsonify

myaccount_bp = Blueprint('myaccount_bp', __name__)


@myaccount_bp.route('/myaccount', methods=['GET'])
def my_account_page():
    try:
        return render_template('myaccount.html'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

