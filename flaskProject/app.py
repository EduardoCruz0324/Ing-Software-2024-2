from flask import Flask, redirect, render_template, request, url_for

from alchemyClasses import db
from contollers.ControllerUsuario import usuario_blueprint
from contollers.ControllerPelicula import pelicula_blueprint
from contollers.ControllerRenta import renta_blueprint

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Develooper123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(pelicula_blueprint)
app.register_blueprint(renta_blueprint)


@app.route('/')
def index():
    return render_template('_Index_.html')


@app.route('/menu_usuario')
def menu_usuario():
    return render_template('menu_usuario.html')


@app.route('/menu_pelicula')
def menu_pelicula():
    return render_template('menu_pelicula.html')


@app.route('/menu_renta')
def menu_renta():
    return render_template('menu_renta.html')


@app.route('/ver_usuarios', methods=['GET'])
def ver_usuarios():
    # Lógica para mostrar los usuarios
    return "Lista de usuarios"


@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('agregar_usuario.html')
    elif request.method == 'POST':
        # Lógica para agregar un nuevo usuario
        return "Usuario agregado"


@app.route('/editar_usuario/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):
    if request.method == 'GET':
        # Lógica para obtener el usuario con el ID proporcionado y mostrar el formulario de edición
        return f"Editar usuario con ID {id_usuario}"
    elif request.method == 'POST':
        # Lógica para editar el usuario con el ID proporcionado
        return f"Usuario con ID {id_usuario} editado"


@app.route('/eliminar_usuario/<int:id_usuario>', methods=['GET'])
def eliminar_usuario(id_usuario):
    # Lógica para eliminar el usuario con el ID proporcionado
    return f"Usuario con ID {id_usuario} eliminado"


@app.route('/ver_peliculas')
def ver_peliculas():
    # Lógica para mostrar las películas
    return "Lista de películas"


@app.route('/agregar_pelicula', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('agregar_pelicula.html')
    elif request.method == 'POST':
        # Lógica para agregar una nueva película
        return "Película agregada"


@app.route('/editar_pelicula/<int:id_pelicula>', methods=['GET', 'POST'])
def editar_pelicula(id_pelicula):
    if request.method == 'GET':
        # Lógica para obtener la película con el ID proporcionado y mostrar el formulario de edición
        return f"Editar película con ID {id_pelicula}"
    elif request.method == 'POST':
        # Lógica para editar la película con el ID proporcionado
        return f"Película con ID {id_pelicula} editada"


@app.route('/eliminar_pelicula/<int:id_pelicula>', methods=['GET'])
def eliminar_pelicula(id_pelicula):
    # Lógica para eliminar la película con el ID proporcionado
    return f"Película con ID {id_pelicula} eliminada"


@app.route('/ver_rentas')
def ver_rentas():
    # Lógica para mostrar las rentas
    return "Lista de rentas"


@app.route('/agregar_renta', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('agregar_renta.html')
    elif request.method == 'POST':
        # Lógica para agregar una nueva renta
        return "Renta agregada"


@app.route('/editar_renta/<int:id_renta>', methods=['GET', 'POST'])
def editar_renta(id_renta):
    if request.method == 'GET':
        # Lógica para obtener la renta con el ID proporcionado y mostrar el formulario de edición
        return f"Editar renta con ID {id_renta}"
    elif request.method == 'POST':
        # Lógica para editar la renta con el ID proporcionado
        return f"Renta con ID {id_renta} editada"


@app.route('/eliminar_renta/<int:id_renta>', methods=['GET'])
def eliminar_renta(id_renta):
    # Lógica para eliminar la renta con el ID proporcionado
    return f"Renta con ID {id_renta} eliminada"


if __name__ == '__main__':
    app.run()

