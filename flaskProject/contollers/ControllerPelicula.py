from flask import Blueprint, request, render_template, flash, redirect, url_for
from random import randint

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/')
def ver_peliculas():
    return "select * from pelicula"

@pelicula_blueprint.route('/id/<int:id_pelicula>/<string:nombre>')
def ver_pelicula_id(id_pelicula, nombre):
    return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('agregar_pelicula.html')
    else:
        name = request.form['name']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('pelicula.agregar_pelicula')
        
        return render_template('añadido_pelicula.html', name=name, genero=genero, duracion=duracion, inventario=inventario)

@pelicula_blueprint.route('/editar/<int:id_pelicula>', methods=['GET', 'POST'])
def editar_pelicula(id_pelicula):
    if request.method == 'GET':
        # Aquí cargarías la película con el ID id_pelicula desde la base de datos
        # Supongamos que obtienes una película llamada pelicula de la base de datos
        pelicula = {'idPelicula': id_pelicula, 'nombre': 'Nombre Película', 'genero': 'Género'}
        return render_template('edit_movie.html', pelicula=pelicula)
    else:
        # Aquí actualizarías la película en la base de datos con la información del formulario
        flash("Película actualizada correctamente")
        return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/borrar/<int:id_pelicula>')
def borrar_pelicula(id_pelicula):
    # Aquí eliminarías la película con el ID id_pelicula de la base de datos
    flash("Película eliminada correctamente")
    return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/borrar_todos')
def borrar_todas_las_peliculas():
    # Aquí eliminarías todas las películas de la base de datos
    flash("Todas las películas han sido eliminadas")
    return redirect(url_for('pelicula.ver_peliculas'))

