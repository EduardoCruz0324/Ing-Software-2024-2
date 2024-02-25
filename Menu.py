from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_pelicula import mostrar_registros as mostrar_registros_pelicula
from model.model_pelicula import mostrar_registro_por_id as filtrar_pelicula_por_id
from model.model_pelicula import actualizar_nombre_pelicula as actualizar_nombre_pelicula_pelicula
from model.model_pelicula import borrar_pelicula as borrar_pelicula_pelicula
from model.model_pelicula import borrar_todos_los_registros_pelicula as borrar_todos_los_registros_pelicula

from model.model_renta import filtrar_todos_los_registros_renta as mostrar_registros_renta
from model.model_renta import filtrar_renta_por_id as filtrar_renta_por_id
from model.model_renta import actualizar_fecha_renta as actualizar_fecha_renta_renta
from model.model_renta import borrar_renta as borrar_renta_renta
from model.model_renta import borrar_todos_los_registros_renta as borrar_todos_los_registros_renta

from model.model_usuario import filtrar_todos_los_registros_usuario as mostrar_registros_usuario
from model.model_usuario import filtrar_usuario_por_id as filtrar_usuario_por_id
from model.model_usuario import actualizar_nombre_usuario as actualizar_nombre_usuario_usuario
from model.model_usuario import borrar_usuario as borrar_usuario_usuario
from model.model_usuario import borrar_todos_los_registros_usuario as borrar_todos_los_registros_usuario

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def mostrar_menu():
    print("Menú:")
    print("1. Ver registros de una tabla")
    print("2. Filtrar registros por ID")
    print("3. Actualizar la columna nombre de un registro / Modificar fecha de renta")
    print("4. Eliminar un registro por ID")
    print("5. Eliminar todos los registros de una tabla")
    print("6. Salir")

def ejecutar_opcion(opcion):
    with app.app_context():
        if opcion == "1":
            tabla = input("Ingrese el nombre de la tabla (pelicula, renta, usuario): ")
            if tabla == "pelicula":
                mostrar_registros_pelicula()
            elif tabla == "renta":
                mostrar_registros_renta()
            elif tabla == "usuario":
                mostrar_registros_usuario()
            else:
                print("Tabla no válida.")
        elif opcion == "2":
            tabla = input("Ingrese el nombre de la tabla (pelicula, renta, usuario): ")
            if tabla == "pelicula":
                id_pelicula = int(input("Ingrese el ID de la película a filtrar: "))
                filtrar_pelicula_por_id(id_pelicula)
            elif tabla == "renta":
                id_renta = int(input("Ingrese el ID de la renta a filtrar: "))
                filtrar_renta_por_id(id_renta)
            elif tabla == "usuario":
                id_usuario = int(input("Ingrese el ID del usuario a filtrar: "))
                filtrar_usuario_por_id(id_usuario)
            else:
                print("Tabla no válida.")
        elif opcion == "3":
            tabla = input("Ingrese el nombre de la tabla (pelicula, renta, usuario): ")
            if tabla == "pelicula":
                id_pelicula = int(input("Ingrese el ID de la película a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                actualizar_nombre_pelicula_pelicula(id_pelicula, nuevo_nombre)
            elif tabla == "renta":
                id_renta = int(input("Ingrese el ID de la renta a actualizar: "))
                nueva_fecha_renta = input("Ingrese la nueva fecha de renta (YYYY-MM-DD): ")
                actualizar_fecha_renta_renta(id_renta, nueva_fecha_renta)
            elif tabla == "usuario":
                id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
                nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                actualizar_nombre_usuario_usuario(id_usuario, nuevo_nombre)
            else:
                print("Tabla no válida.")
        elif opcion == "4":
            tabla = input("Ingrese el nombre de la tabla (pelicula, renta, usuario): ")
            if tabla == "pelicula":
                id_pelicula = int(input("Ingrese el ID de la película a eliminar: "))
                borrar_pelicula_pelicula(id_pelicula)
            elif tabla == "renta":
                id_renta = int(input("Ingrese el ID de la renta a eliminar: "))
                borrar_renta_renta(id_renta)
            elif tabla == "usuario":
                id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
                borrar_usuario_usuario(id_usuario)
            else:
                print("Tabla no válida.")
        elif opcion == "5":
            tabla = input("Ingrese el nombre de la tabla (pelicula, renta, usuario): ")
            if tabla == "pelicula":
                borrar_todos_los_registros_pelicula()
            elif tabla == "renta":
                borrar_todos_los_registros_renta()
            elif tabla == "usuario":
                borrar_todos_los_registros_usuario()
            else:
                print("Tabla no válida.")
        elif opcion == "6":
            print("¡Hasta luego!")
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        ejecutar_opcion(opcion)
        if opcion == "6":
            break
