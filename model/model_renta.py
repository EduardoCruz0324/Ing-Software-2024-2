from alchemyClasses.Renta import Renta
from alchemyClasses import db

def borrar_renta(idRentar):
    renta = Renta.query.filter(Renta.idRentar).first()
    db.session.delete(renta)
    db.session.commit()

def crear_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus):
    nueva_renta = Renta(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)
    db.session.add(nueva_renta)
    db.session.commit()
    print("Renta agregada exitosamente.")

def obtener_renta_por_id(idRentar):
    renta = Renta.query.get(idRentar)
    if renta:
        print(f"Información de la renta (ID {idRentar}):")
        print(f"ID Usuario: {renta.idUsuario}")
        print(f"ID Película: {renta.idPelicula}")
        print(f"Fecha de renta: {renta.fecha_renta}")
        print(f"Días de renta: {renta.dias_de_renta}")
        print(f"Estatus: {renta.estatus}")
    else:
        print("No se encontró ninguna renta con el ID proporcionado.")

def actualizar_renta(idRentar, idUsuario=None, idPelicula=None, fecha_renta=None, dias_de_renta=None, estatus=None):
    renta = Renta.query.get(idRentar)
    if renta:
        if idUsuario is not None:
            renta.idUsuario = idUsuario
        if idPelicula is not None:
            renta.idPelicula = idPelicula
        if fecha_renta is not None:
            renta.fecha_renta = fecha_renta
        if dias_de_renta is not None:
            renta.dias_de_renta = dias_de_renta
        if estatus is not None:
            renta.estatus = estatus

        db.session.commit()
        print("Información de la renta actualizada exitosamente.")
    else:
        print("La renta con el ID proporcionado no existe.")

def actualizar_fecha_renta(idRentar, nueva_fecha_renta):
    renta = Renta.query.get(idRentar)
    if renta:
        renta.fecha_renta = nueva_fecha_renta
        db.session.commit()
        print("Fecha de renta actualizada exitosamente.")
    else:
        print("La renta con el ID proporcionado no existe.")

def borrar_todos_los_registros_renta():
    db.session.query(Renta).delete()
    db.session.commit()
    print("Todos los registros de la tabla Renta han sido borrados exitosamente.")

def filtrar_todos_los_registros_renta():
    rentas = Renta.query.all()
    if rentas:
        print("Registros de la tabla Renta:")
        for renta in rentas:
            print(f"ID: {renta.idRentar}, ID Usuario: {renta.idUsuario}, ID Película: {renta.idPelicula}")
    else:
        print("No hay registros en la tabla Renta.")

def filtrar_renta_por_id(idRentar):
    renta = Renta.query.get(idRentar)
    if renta:
        print(f"Información de la renta con ID {idRentar}:")
        print(f"ID Usuario: {renta.idUsuario}")
        print(f"ID Película: {renta.idPelicula}")
    else:
        print("No se encontró ninguna renta con el ID proporcionado.")