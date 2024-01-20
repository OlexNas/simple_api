from flask import Blueprint, request
from .schemas import *
from marshmallow.exceptions import ValidationError
from .models import *


api = Blueprint('api', __name__)


@api.route('/records', methods=['GET', 'POST'])
def get_records():
    if request.method == "POST":
        json_data = request.get_json()

        try:
            user = User.from_dict(UserSchema().load(json_data))

        except ValidationError as err:
            print('ERROR')

        print(json_data)

    return {'ralf':'123'}