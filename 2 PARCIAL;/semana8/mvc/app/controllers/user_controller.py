from flask import Blueprint, request, redirect, url_for
# Importamos la vista de usuarios
from views import user_view
# Importamos el modelo de usuario
from models.user_model import User
from datetime import datetime


# Un Blueprint es un objeto que agrupa rutas y vistas
user_bp = Blueprint('user', __name__)
#
# Definimos las rutas "/" asociada a la funcion usuarios
# que nos devuelve la vista de usuarios
@user_bp.route('/')
def usuarios():
    # Obtenemos todos los usuario0s
    users = User.get_all()
    # Llamamos a la vista de usuarios
    return user_view.usuarios(users)

# Definimos la ruta "/users" asociada a la función registro
# que nos devuelve la vista de registro
@user_bp.route('/users', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email=request.form['email']
        contraseña=request.form['contraseña']
        fecha_nacimiento_str=request.form['fecha_nacimiento']
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, '%Y-%m-%d').date()
       # Creamos un nuevo usuario
        user = User(first_name, last_name,email,contraseña,fecha_nacimiento)
        # Guardamos el usuario
        user.save()
        # Redirigimos a la vista de usuarios
        return redirect(url_for('user.usuarios'))
    # Llamamos a la vista de registro
    return user_view.registro()

    