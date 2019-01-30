import web
import config as config 

class Insert:
	def __init__(self):
		pass

	def GET(self):
		return config.render.insert()

	def POST(self):
		formulario = web.input()
		nombre = formulario['nombre']
		ap_paterno =formulario['ap_paterno']
		ap_materno = formulario['ap_materno']
		email = formulario['email']
		direccion = formulario['direccion']
		config.model_clientes.insert_cliente(nombre,ap_paterno,ap_materno,email,direccion)
		raise web.seeother('/')