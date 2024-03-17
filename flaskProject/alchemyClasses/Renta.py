from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, SmallInteger
from datetime import datetime

from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

class Renta(db.Model):
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey(Usuario.idUsuario) )
    idPelicula = Column(Integer, ForeignKey(Pelicula.idPelicula))
    fecha_renta = Column(DateTime, default=datetime.now)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(SmallInteger, default=0)

    def __init__(self, idRentar, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
        self.idRentar = idRentar
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus