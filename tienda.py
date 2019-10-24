

def Menu():
	import os,sys
	print ('Estas en el menu principal de la tienda!!')
	print("")
	print ('1, Agregar articulo')
	print ('2, Modificar articulo')
	print ('3, Eliminar articulo')
	print ('4, Ver todos los articulos')
	print ('5, Buscar articulo por nombre')
	print ('6, Salir')
	
	#ASEGURAMOS QUE INGRESE 1..5
	try:
		opcion = int(input('Ingrese un numero de la opciones: '))
	except (ValueError):
		print ('No ingreso un numero. Vuelva a intentarlo')
		print ("")
		Menu()
	
	os.system('clear')
	if (opcion == 1):
		Agregar()
	elif (opcion == 2):
		Modificar()
	elif (opcion == 3):
		Eliminar()
	elif (opcion == 4):
		Ver()
	elif (opcion == 5):
		VerNombre()
	elif (opcion == 6):
		Salir()
	else:
		print ('Por favor digite un numero de los mencionados')
		Menu()
		
def Agregar():
	import os,sys,sqlite3
	#CONECTAMOS LA BASE DE DATOS
	con = sqlite3.connect('ARTICULOS.s3db')
	print ('Estas en el menu agregar')
	print ('')
	
	nombre = input ('Nombre del articulo: ')
	precio = input ('Precio del articulo: ')
	#LIMPIAMOS PANTALLA
	os.system('clear')
	cursor = con.cursor()
	#INSERTAMOS EN LA TABLA EL PRODUCTO
	cursor.execute("insert into Productos (Nombre, Precio) values ('"+nombre+"','"+precio+"')")
	print ('Se agrego el producto de manera correcta!!')
	con.commit()
	con.close()
	Menu()

def Ver():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from productos')
	print ('Estas en la opcion ver!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio')
	print ('---------------------------------')
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2])
		print (str(product))
	
	con.commit()
	con.close()
	print ('')
	Menu()
	
def VerNombre():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	print ('Estas en la opcion de filtrar producto por nombre!!')
	print ('')
	nombre = input ('Nombre del articulo: ')
	print ('')
	print ('\t Cod \t Nombre \t Precio')
	print ('---------------------------------')
	
	cursor.execute("""select * from Productos where nombre=?""", (nombre,)) 
	
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2])
		print (str(product))
				
	con.commit()
	con.close()
	
	Menu()
	
	
	
	
def Eliminar():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from productos')
	print ('Estas en la opcion eliminar!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio')
	print ('---------------------------------')
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2])
		print (str(product))
		print ('')
	
	cod = input ('Ingrese el codigo a eliminar: ')
	sql = 'delete from Productos where cod='+cod
	cursor.execute(sql)
	con.commit()
	con.close()
	#LIMPIAMOS PANTALLA
	os.system('clear')
	print ('El producto ha sido eliminado')
	print ('')
	Menu()
	
def Modificar():
	import os,sys,sqlite3
	producto = []
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from Productos')
	print ('Estas en la opcion modificar!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio')
	print ('---------------------------------')
	for productos in cursor:
		#Se usa lista producto en el for
		producto.append(productos)
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2])
		print (str(product))
		print ('')
	cod = input('Digite el codigo del producto a modificar: ')
	#productos: Tabla de la base de datos
	#producto: Lista
	for productos in producto:
		if (int(productos[0] == int(cod))):
			nombre = productos[1]
			precio = productos[2]
			encontrado = True
			break
	nombre = input('Digite el nombre nuevo' +nombre+ ':')
	precio = input('Digite el nombre nuevo' +str(precio)+ ':')
	sql = "update Productos set Nombre='"+nombre+"', Precio='"+precio+"' where cod="+cod
	cursor.execute(sql)
	con.commit()
	con.close()
	os.system('clear')
	print ('El producto ha sido modificado!!')
	print ('')
	Menu()
	
def Salir():
	import os,sys
	print ('Has elegido salir!!')
	sys.exit()
	
	
Menu()
