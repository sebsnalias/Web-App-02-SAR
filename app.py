import web

urls= ('/','application.controllers.clientes.index.Index',
	'/insert','application.controllers.clientes.insert.Insert',
	'/update(.*)','application.controllers.clientes.update.Update',
	'/delete(.*)','application.controllers.clientes.delete.Delete',
	'/view/(.*)','application.controllers.clientes.view.View',
	'/productos','application.controllers.productos.index.Index',
	'/insertProd','application.controllers.productos.insert.Insert',
	'/updateProd(.*)','application.controllers.productos.update.Update',
	'/deleteProd(.*)','application.controllers.productos.delete.Delete',
	'/viewProd/(.*)','application.controllers.productos.view.View',
	)

if __name__=='__main__':
	web.config.debug = False
	app=web.application(urls,globals())
	app.run()