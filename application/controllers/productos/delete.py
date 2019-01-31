import web
import config as config

class Delete:
	def __init__(self):
		pass

	def GET(self,nombre_prod):
		productos = config.model_productos.select_nombre(nombre_prod)
		return config.render.delete(productos)

	def POST(self,nombre_prod):
		formulario = web.input()
		nombre_prod = formulario['nombre_prod']
		tipo = formulario ['tipo']
		descripcion = formulario ['descripcion']
		marca = formulario ['marca']
		origen = formulario ['origen']
		config.model_productos.delete_producto(nombre_prod)
		raise web seeother('/')