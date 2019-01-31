import web 
import config as config 

class Insert:
	def __init__(self):
		pass

	def GET(self):
		return config.render.insert()

	def POST(self):
		formulario = web.input()
		nombre_prod = formulario['nombre_prod']
		tipo = formulario['tipo']
		descripcion = formulario['descripcion']
		marca = formulario['marca']
		origen = formulario['formulario']
		config.model_productos.insert_producto(nombre_prod,tipo,descripcion,marca,origen)
		raise web.seeother('/')