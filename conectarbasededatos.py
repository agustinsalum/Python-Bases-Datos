
def agregar():
	import sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute("""insert into Productos values (10, 'detergente', 70)""") 
	con.commit()
	con.close()
	

def consultar():
	import sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	
	nombre = input('Ingrese nombre a buscar: ')
	
	cursor.execute("""select * from Productos where nombre=?""", (nombre,))
	
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2])
		print (str(product))
	
	con.commit()
	con.close()
	
agregar()
consultar()
