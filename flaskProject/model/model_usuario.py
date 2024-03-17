from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def borrar_usuario(idUsuario):
    usuario = Usuario.query.filter(Usuario.idUsuario).first()
    db.session.delete(usuario)
    db.session.commit()

def crear_usuario(nombre, apt_pat, apt_mat, email, password, profilepicture=None, superUser=None):
    nuevo_usuario = Usuario(nombre=nombre, apt_pat=apt_pat, apt_mat=apt_mat, email=email, password=password, profilepicture=profilepicture, superUser=superUser)
    db.session.add(nuevo_usuario)
    db.session.commit()
    print("Usuario creado exitosamente.")

def obtener_usuario_por_id(idUsuario):
    usuario = Usuario.query.get(idUsuario)
    if usuario:
        print(f"Información del usuario (ID {idUsuario}):")
        print(f"Nombre: {usuario.nombre}")
        print(f"Apellido Paterno: {usuario.apt_pat}")
        print(f"Apellido Materno: {usuario.apt_mat}")
        print(f"Email: {usuario.email}")
        print(f"Profile Picture: {usuario.profilepicture}")
        print(f"Super Usuario: {usuario.superUser}")
    else:
        print("No se encontró ningún usuario con el ID proporcionado.")

def actualizar_usuario(idUsuario, nombre=None, apt_pat=None, apt_mat=None, email=None, password=None, profilepicture=None, superUser=None):
    usuario = Usuario.query.get(idUsuario)
    if usuario:
        if nombre is not None:
            usuario.nombre = nombre
        if apt_pat is not None:
            usuario.apt_pat = apt_pat
        if apt_mat is not None:
            usuario.apt_mat = apt_mat
        if email is not None:
            usuario.email = email
        if password is not None:
            usuario.password = password
        if profilepicture is not None:
            usuario.profilepicture = profilepicture
        if superUser is not None:
            usuario.superUser = superUser

        db.session.commit()
        print("Información del usuario actualizada exitosamente.")
    else:
        print("El usuario con el ID proporcionado no existe.")

def borrar_todos_los_registros_usuario():
    db.session.query(Usuario).delete()
    db.session.commit()
    print("Todos los registros de la tabla Usuario han sido borrados exitosamente.")

def filtrar_todos_los_registros_usuario():
    usuarios = Usuario.query.all()
    if usuarios:
        print("Registros de la tabla Usuario:")
        for usuario in usuarios:
            print(f"ID: {usuario.idUsuario}, Nombre: {usuario.nombre}, Email: {usuario.email}")
    else:
        print("No hay registros en la tabla Usuario.")

def filtrar_usuario_por_id(idUsuario):
    usuario = Usuario.query.get(idUsuario)
    if usuario:
        print(f"Información del usuario con ID {idUsuario}:")
        print(f"Nombre: {usuario.nombre}")
        print(f"Email: {usuario.email}")
    else:
        print("No se encontró ningún usuario con el ID proporcionado.")

def actualizar_nombre_usuario(idUsuario, nuevo_nombre):
    usuario = Usuario.query.get(idUsuario)
    if usuario:
        usuario.nombre = nuevo_nombre
        db.session.commit()
        print("Nombre del usuario actualizado exitosamente.")
    else:
        print("El usuario con el ID proporcionado no existe.")