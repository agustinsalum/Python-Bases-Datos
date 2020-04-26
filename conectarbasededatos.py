import os.path

def agregar():
	import sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute("""insert into Productos values (10, 'detergente', 2 , 70)""") 
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


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "Productos.db")
with sqlite3.connect(db_path) as db:

agregar()
consultar()
