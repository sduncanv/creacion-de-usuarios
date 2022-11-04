Este proyecto trata de una API que permite crear usuarios en una base de datos, también permite realizar inicio de sesión según los datos registrados.

El proyecto está hecho con el framewrok Flask, usando la librería SQLAlchemy para la conexión con la base de datos SQLite.


Cuerpo del proyecto:
- clases
    - database.py
    - query_user.py
- Models
    - users.py
- utils
    - validators.py
- database.sb
- main.py
- README
- requirements.txt

La carpeta 'clases' contiene el archivo database.py y query_user.py que hace la conexión a la base de datos y las consultas, respectivamente.

La carpeta 'Models' tiene el archivo users.py que tiene la clase Users que crea la tabla en la base de datos.

La carpeta 'utils' contiene el arcivo que valida los datos para poder crear e iniciar sesión.

En el archivo requirements.txt están las dependencias necesarias para el funcionamiento del proyecto.