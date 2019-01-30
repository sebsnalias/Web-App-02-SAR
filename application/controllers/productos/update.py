import web
import config as config 

class Update:
	def __init__(self):
		pass

	def GET(self,nombre_prod):
		cliente = config.model_productos.select_nombre_prod(nombre_prod)
		return config.render.update(producto)

	def POST(self,tipo,descripcion,marca,origen):
		formulario = web.input()
		nombre_prod = formulario['nombre_prod']
		tipo = formulario ['tipo']
		descripcion = formulario ['descripcion']
		marca = formulario ['marca']
		origen = formulario ['origen']
		config.model_productos.update_producto(nombre_prod,tipo,descripcion,marca,origen)
		raise web.seeother('/')