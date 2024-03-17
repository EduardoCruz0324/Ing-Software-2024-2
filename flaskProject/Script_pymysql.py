import pymysql
from datetime import datetime, timedelta

def conectar_bd():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='lab',
            password='Developer123!',
            database='lab_ing_software',
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def insertar_registros(connection):
    try:
        with connection.cursor() as cursor:
            # Insertar usuarios si no existen
            sql = "INSERT IGNORE INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)"
            for i in range(1, 6):
                email = f"Lalo{i}@example.com"
                cursor.execute(sql, ('Eduardo', 'Cruz', 'Campos', '240603', email))
            connection.commit()
            
            # Insertar películas si no existen
            sql = "INSERT IGNORE INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, ('Anabelle', 'Terror', 120, 5))
            connection.commit()

            # Obtener el id del primer usuario insertado
            sql = "SELECT idUsuario FROM usuarios LIMIT 1"
            cursor.execute(sql)
            usuario_id = cursor.fetchone()['idUsuario']

            # Obtener el id de la primera película insertada
            sql = "SELECT idPelicula FROM peliculas LIMIT 1"
            cursor.execute(sql)
            pelicula_id = cursor.fetchone()['idPelicula']

            # Insertar rentas solo si existen usuarios y películas
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta) VALUES (%s, %s, %s)"
            cursor.execute(sql, (usuario_id, pelicula_id, datetime.now()))
            connection.commit()

        print("Registros insertados correctamente.")
    except Exception as e:
        print(f"Error al insertar registros: {e}")


def filtrar_usuarios_por_apellido(connection, apellido):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s"
            cursor.execute(sql, ('%' + apellido,))
            result = cursor.fetchall()
            if result:
                print("Usuarios encontrados:")
                for row in result:
                    print(row)
            else:
                print("No se encontraron usuarios con ese apellido.")
    except Exception as e:
        print(f"Error al filtrar usuarios: {e}")

def cambiar_genero_pelicula(connection, nombre_pelicula, nuevo_genero):
    try:
        with connection.cursor() as cursor:
            # Verificar si la película existe
            sql = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql, (nombre_pelicula,))
            result = cursor.fetchone()
            if result:
                # Actualizar el género de la película
                sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql, (nuevo_genero, nombre_pelicula))
                connection.commit()
                print("Género de la película actualizado correctamente.")
            else:
                print("La película especificada no existe.")
    except Exception as e:
        print(f"Error al cambiar género de película: {e}")

def eliminar_rentas_antiguas(connection):
    try:
        with connection.cursor() as cursor:
            # Calcular la fecha límite (hoy - 3 días)
            fecha_limite = datetime.now() - timedelta(days=3)
            # Eliminar rentas anteriores a la fecha límite
            sql = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql, (fecha_limite,))
            connection.commit()
            print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        print(f"Error al eliminar rentas antiguas: {e}")

if __name__ == "__main__":
    connection = conectar_bd()
    if connection:
        insertar_registros(connection)
        apellido = input("Ingrese el apellido para filtrar usuarios: ")
        filtrar_usuarios_por_apellido(connection, apellido)
        nombre_pelicula = input("Ingrese el nombre de la película: ")
        nuevo_genero = input("Ingrese el nuevo género de la película: ")
        cambiar_genero_pelicula(connection, nombre_pelicula, nuevo_genero)
        eliminar_rentas_antiguas(connection)
        connection.close()



