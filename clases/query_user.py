from clases.database import Database
from Models.users import Users as modelUser

class Query:

    def createUser(self, data):
    
        db = Database()
        user_exists = db.session.query(modelUser).filter(
            modelUser.email == data['email']
        ).first()

        if user_exists == None:
            db.session.bulk_insert_mappings(modelUser, [data])
            db.session.commit()
            db.session.close()
            
            return 'Usuario creado'

        else:
            return 'Usuario existente'


    def loginUser(self, data):

        db = Database()
        user = db.session.query(modelUser).filter(
            modelUser.email == data['email']
        ).filter(
            modelUser.password == data['password']
        ).first()
        db.session.close()

        if user != None:
            return 'Sección iniciada'
        else:
            return 'Correo o contraseña incorrecta'