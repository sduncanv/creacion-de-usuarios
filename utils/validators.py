
class Validate:

    def val_create_user(self, data):
        """
        Validate user creation

        This function validates the data to create a user.

        Data to validate:
            - A json with fullname, email, password, address and phone_number.

        Return a success message if the data is correct otherwise return an error message.
        """

        name = data['fullname'].replace(' ', '')
        email = True if '@' in data['email'] else False
        password = len(data['password']) >= 8
        address = data['address'] != ''
        p_number = data['phone_number'].isdigit()

        if (
            name != '' and
            name.isdigit() == False and
            email == True and
            password == True and 
            address == True and
            p_number == True
        ):
            return { 'status': 200 }
        else:
            return { 'Error': 'Verifique los datos', 'status': 400 }
    

    def val_login_user(self, data):
        """
        Validate login

        This function validates the data to login.

        Data to validate:
            - A json with fullname and password of the database.

        Return a success message if the data is correct otherwise return an error message.
        """

        email = True if '@' in data['email'] else False
        password = len(data['password']) >= 8

        if email == True and password == True:
            return { 'status': 200 }
        else:
            return { 'Error': 'Verifique los datos', 'status': 400 }
    