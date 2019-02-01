import config as config

db = config.db

def select_clientes():
	try:
		return db.select('clientes')
	except Exception as e:
		print "Model select_clientes Error {}",format(e.args)
		print "Model select_clientes Message {}",format(e.message)
		return None 

def select_nombre(cliente):
	try:
		return db.select('clientes',
			where='nombre=$cliente',
			vars=locals())[0]
	except Exception as e:
		print "Model select_nombre Error {}",format(e.args)
		print "Model select_clientes Message {}",format(e.message)
		return None 

def insert_cliente(nombre,ap_paterno,ap_materno,email,direccion):
	try:
		return db.insert ('clientes',
		nombre=nombre,
		ap_paterno=ap_paterno,
		ap_materno=ap_materno,
		email=email,
		direccion=direccion)
	except Exception as e:
		print "Model insert_cliente Error {}",format(e.args)
		print "Model insert_cliente Message {}",format(e.message)
		return None

def delete_cliente(nombre):
	try:
		return db.delete('clientes',
		where ='nombre=$nombre',
		vars=locals())
	except Exception as e:
		print "Model delete_cliente Error {}",format(e.args)
		print "Model delete_cliente Message {}",format(e.message)
		return None

def update_cliente(nombre,ap_paterno,ap_materno,email,direccion):
	try:
		return db.update('clientes',
		ap_paterno=ap_paterno,
		ap_materno=ap_materno,
		email=email,
		direccion=direccion,
		where ='nombre=$nombre',
		vars=locals())
	except Exception as e:
		print "Model update_cliente Error {}",format(e.args)
		print "Model update_cliente Message {}",format(e.message)
		return None


