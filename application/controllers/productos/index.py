import web
import config as config 

class Index:
	def __init__(self):
		pass

	def GET(self):
		productos = config.model_productos.select_productos().list()
		return config.render.index(productos)