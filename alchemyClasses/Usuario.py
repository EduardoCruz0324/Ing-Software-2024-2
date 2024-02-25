from sqlalchemy import Column, Integer, String, SmallInteger, LargeBinary

from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(45))
    ap_pat = Column(String(45))
    ap_mat = Column(String(45), nullable=True)
    email = Column(String(60))
    password = Column(String(64), nullable=True)
    profilePicture = Column(LargeBinary, nullable= True)
    superUser = Column(SmallInteger, nullable=True)


    def __init__(self, nombre, apPat, email, apMat=None, password=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.ap_pat = apPat
        self.ap_mat = apMat
        self.email = email
        self.password = password
        self.profilePicture = profilePicture 
        self.superUser = superUser