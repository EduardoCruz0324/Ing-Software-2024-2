from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def borrar_pelicula(idPelicula):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula).first()
    db.session.delete(pelicula)
    db.session.commit()

def agregar_pelicula(nombre, genero, duracion, inventario):
    nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
    db.session.add(nueva_pelicula)
    db.session.commit()
    print("Película agregada exitosamente.")

def actualizar_pelicula(idPelicula, nombre=None, genero=None, duracion=None, inventario=None):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula).first()
    if pelicula:
        if nombre is not None:
            pelicula.nombre = nombre
        if genero is not None:
            pelicula.genero = genero
        if duracion is not None:
            pelicula.duracion = duracion
        if inventario is not None:
            pelicula.inventario = inventario

        db.session.commit()
        print("Pelicula actualizada exitosamente.")
    else:
        print("La película con el ID proporcionado no existe.")

def actualizar_genero(idPelicula, nuevo_genero):
    pelicula = Pelicula.query.filter_by(idPelicula=idPelicula).first()
    if pelicula:
        pelicula.genero = nuevo_genero
        db.session.commit()
        print("Género de la película actualizado exitosamente.")
    else:
        print("La película con el ID proporcionado no existe.")

def mostrar_registros():
    peliculas = Pelicula.query.all()
    if peliculas:
        print("Registros de películas:")
        for pelicula in peliculas:
            print(f"ID: {pelicula.idPelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Duración: {pelicula.duracion}, Inventario: {pelicula.inventario}")
    else:
        print("No hay registros de películas.")

def mostrar_registro_por_id(idPelicula):
    pelicula = Pelicula.query.filter_by(idPelicula=idPelicula).first()
    if pelicula:
        print(f"ID: {pelicula.idPelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Duración: {pelicula.duracion}, Inventario: {pelicula.inventario}")
    else:
        print("No se encontró ninguna película con el ID proporcionado.")

def actualizar_nombre_pelicula(idPelicula, nuevo_nombre):
    pelicula = Pelicula.query.filter_by(idPelicula=idPelicula).first()
    if pelicula:
        pelicula.nombre = nuevo_nombre
        db.session.commit()
        print("Nombre de la película actualizado exitosamente.")
    else:
        print("La película con el ID proporcionado no existe.")

def borrar_todos_los_registros_pelicula():
    db.session.query(Pelicula).delete()
    db.session.commit()
    print("Todos los registros de la tabla Pelicula han sido borrados exitosamente.")