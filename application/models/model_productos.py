import config as config 

db = config.db

def select_productos():
	try:
		return db.select('productos')
	except Exception as e:
		print "Model select_productos Error{}",format(e.args)
		print "Model select_productos Message{}",format(e.message)
		return None

def select_nombre_prod(nombre_prod):
	try:
		return db.select('productos',
		where='nombre_prod=$nombre_prod',
		vars=locals())[0]
	except Exception as e:
		print "Model select_nombre_prod Error{}",format(e.args)
		print "Model select_nombre_prod Message{}",format(e.message)
		return None

def insert_producto(nombre_prod,tipo,descripcion,marca,origen):
	try:
		return db.insert('productos',
		nombre_prod=nombre_prod,
		tipo=tipo,
		descripcion=descripcion,
		marca=marca,
		origen=origen)
	except Exception as e:
		print "Model insert_producto Error{}",format(e.args)
		print "Model insert_producto Message{}",format(e.message)
		return None

def delete_producto(nombre_prod):
	try:
		return db.delete('productos',
		where='nombre_prod=$nombre_prod',
		vars=locals())
	except Exception as e:
		print "Model delete_producto Error{}",format(e.args)
		print "Model delete_producto Message{}",format(e.message)
		return None

def update_producto(nombre_prod,tipo,descripcion,marca,origen):
	try:
		return db.update('productos',
		tipo=tipo,
		descripcion=descripcion,
		marca=marca,
		origen=origen,
		where='nombre_prod=$nombre_prod',
		vars=locals())
	except Exception as e:
		print "Model update_producto Error{}",format(e.args)
		print "Model update_producto Message{}",format(e.message)
		return None		