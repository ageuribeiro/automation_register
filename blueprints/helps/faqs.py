from flask import Blueprint, jsonify, render_template

help_bp = Blueprint('help', __name__)

@help_bp.route('/helps', methods=['GET'])
def helps():
    try:
        return render_template('help.html'), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
