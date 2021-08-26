from flask_login import UserMixin

class Usuario(UserMixin):
	def __init__(self, nombre, rut):
		self.nombre = nombre
		self.rut = rut
		self.id = rut

	def __repr__(self):
		return '<Usuario {self.rut}>'.format()