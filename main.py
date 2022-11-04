# Flask
from flask import Flask, request

# Validators
from utils.validators import Validate

# Querys
from clases.query_user import Query


query_users = Query()
validate = Validate()


app = Flask(__name__)


@app.route('/users/create', methods=['POST'])
def create_user():
    """
    Create User

    This is the endpoint to create a new user and save it in the database.

    Request Body:
        - A json with fullname, email, password, address and phone_number.

    Return a success message if the data is correct otherwise return an error message.
    """
    try:
        data = request.json
        val = validate.val_create_user(data)

        if val['status'] == 200:
            res = query_users.createUser(data)
            return res
        else:
            return val

    except Exception as e:
        return {'Error': str(e)}


@app.route('/users/login', methods=['POST'])
def login_user():
    """
    Login User

    This is the endpoint to login user and allow login.

    ---
    Request Body:
        - A json with email and password.


    Return a success message if the data is correct otherwise return an error message.
    """
    try:
        data = request.json
        val = validate.val_login_user(data)
        if val['status'] == 200:
            res = query_users.loginUser(data)
            return res
        else:
            return val
    except Exception as e:
        return {'Error': str(e)}


if __name__ == '__main__':
    app.run(debug = True)
