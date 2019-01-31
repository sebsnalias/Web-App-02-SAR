import web

db = web.database(
	dbn='mysql',
	host='localhost',
	db='ria_iniciales',
	user='ria',
	pw='ria2019',
	port= 3306
	)