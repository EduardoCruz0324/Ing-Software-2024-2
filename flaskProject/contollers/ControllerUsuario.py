from flask import Blueprint, request, render_template, flash, redirect, url_for
from random import randint

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/')
def ver_usuarios():
    return "select * from usuario"

@usuario_blueprint.route('/id/<int:id_usuario>/<string:nombre>')
def ver_usuario_id(id_usuario, nombre):
    return f"Se hace el query con el id {id_usuario} y el nombre {nombre}"

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('agregar_usuario.html')
    else:
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        email = request.form['email']
        password = request.form['password']
        superUser = request.form['superUser']
        
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('usuario.agregar_usuario')
        
        return render_template('añadido_usuario.html', name=name, email=email)

@usuario_blueprint.route('/editar/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    if request.method == 'GET':
        # Aquí cargarías el usuario con el ID id_usuario desde la base de datos
        # Supongamos que obtienes un usuario llamado usuario de la base de datos
        usuario = {'idUsuario': id_usuario, 'name': 'Nombre', 'email': 'correo@example.com'}
        return render_template('edit_user.html', usuario=usuario)
    else:
        # Aquí actualizarías el usuario en la base de datos con la información del formulario
        flash("Usuario actualizado correctamente")
        return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/borrar/<int:id_usuario>')
def borrar_usuario(id_usuario):
    # Aquí eliminarías el usuario con el ID id_usuario de la base de datos
    flash("Usuario eliminado correctamente")
    return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/borrar_todos')
def borrar_todos_los_usuarios():
    # Aquí eliminarías todos los usuarios de la base de datos
    flash("Todos los usuarios han sido eliminados")
    return redirect(url_for('usuario.ver_usuarios'))
