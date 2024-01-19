from flask import Blueprint


api = Blueprint('api', __name__)


@api.route('/records', methods=['GET', 'POST'])
def get_records():
    return {}