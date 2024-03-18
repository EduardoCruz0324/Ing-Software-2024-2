from flask import Blueprint, request, render_template, flash, redirect, url_for
from random import randint

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/')
def ver_rentas():
    return "select * from renta"

@renta_blueprint.route('/id/<int:id_renta>')
def ver_renta_id(id_renta):
    return f"Se hace el query con el id {id_renta}"

@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('agregar_renta.html')
    else:
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        fecha_renta = request.form['fecha_renta']
        dias_de_renta = request.form['dias_de_renta']
        estatus = request.form['estatus']
        
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('renta.agregar_renta')
        
        return render_template('añadido_renta.html', idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)

@renta_blueprint.route('/editar/<int:id_renta>', methods=['GET', 'POST'])
def editar_renta(id_renta):
    if request.method == 'GET':
        # Aquí cargarías la renta con el ID id_renta desde la base de datos
        # Supongamos que obtienes una renta llamada renta de la base de datos
        renta = {'idRenta': id_renta, 'idUsuario': 'ID Usuario', 'idPelicula': 'ID Película', 'fecha_renta': 'Fecha de Renta', 'dias_de_renta': 'Días de Renta', 'estatus': 'Estatus'}
        return render_template('editar_renta.html', renta=renta)
    else:
        # Aquí actualizarías la renta en la base de datos con la información del formulario
        flash("Renta actualizada correctamente")
        return redirect(url_for('renta.ver_rentas'))

@renta_blueprint.route('/borrar/<int:id_renta>')
def borrar_renta(id_renta):
    # Aquí eliminarías la renta con el ID id_renta de la base de datos
    flash("Renta eliminada correctamente")
    return redirect(url_for('renta.ver_rentas'))

@renta_blueprint.route('/borrar_todas')
def borrar_todas_las_rentas():
    # Aquí eliminarías todas las rentas de la base de datos
    flash("Todas las rentas han sido eliminadas")
    return redirect(url_for('renta.ver_rentas'))


