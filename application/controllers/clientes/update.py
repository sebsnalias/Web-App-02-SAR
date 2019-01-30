import web
import config as config

class Update:
	def __init__(self):
		pass

	def GET(self,nombre):
		cliente = config.model_clientes.select_nombre(nombre)
		return config.render.update(persona)

	def POST(self,ap_paterno,ap_materno,email,direccion):
		formulario = web.input()
		nombre = formulario['nombre']
		ap_paterno = formulario['ap_paterno']
		ap_materno = formulario['ap_materno']
		email = formulario['email']
		direccion = formulario['direccion']
		config.model_clientes.update_cliente(nombre,ap_paterno,ap_materno,email,direccion)
		raise web.seeother('/')