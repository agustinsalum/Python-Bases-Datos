

def menu():
	import os,sys
	print ('Estas en el menu principal de la tienda!!')
	print("")
	print ('1,  Agregar articulo')
	print ('2,  Modificar articulo')
	print ('3,  Eliminar articulo')
	print ('4,  Ver todos los articulos')
	print ('5,  Realizar sumatoria')
	print ('6,  Buscar articulo por nombre')
	print ('7,  Creditos')
	print ('8,  Salir')
	
	#ASEGURAMOS QUE INGRESE 1..5
	try:
		opcion = int(input('Ingrese un numero de la opciones: '))
	except (ValueError):
		print ('No ingreso un numero. Vuelva a intentarlo')
		print ("")
		menu()
	
	os.system('clear')
	if (opcion == 1):
		agregar()
	elif (opcion == 2):
		modificar()
	elif (opcion == 3):
		eliminar()
	elif (opcion == 4):
		ver()
	elif (opcion == 5):
		sumatoria()
	elif (opcion == 6):
		verNombre()
	elif (opcion == 7):
		creditos()
	elif (opcion == 8):
		salir()
	else:
		print ('Por favor digite un numero de los mencionados')
		menu()
		
def agregar():
	import os,sys,sqlite3
	#CONECTAMOS LA BASE DE DATOS
	con = sqlite3.connect('ARTICULOS.s3db')
	print ('Estas en el menu agregar')
	print ('')
	
	nombre   = input ('Nombre del articulo: ')
	cantidad = input ('Cantidad del articulo: ')
	precio   = input ('Precio del articulo: ')
	#LIMPIAMOS PANTALLA
	os.system('clear')
	cursor = con.cursor()
	#INSERTAMOS EN LA TABLA EL PRODUCTO
	cursor.execute("insert into Productos (Nombre, Precio, Cantidad) values ('"+nombre+"','"+precio+"','"+cantidad+"')")
	print ('Se agrego el producto de manera correcta!!')
	con.commit()
	con.close()
	menu()

def ver():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from productos')
	print ('Estas en la opcion ver!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio \t Cantidad')
	print ('---------------------------------')
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2]) + '\t' + str(productos[3])
		print (str(product))
	
	con.commit()
	con.close()
	print ('')
	menu()
	
def verNombre():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	print ('Estas en la opcion de filtrar producto por nombre!!')
	print ('')
	nombre = input ('Nombre del articulo: ')
	print ('')
	print ('\t Cod \t Nombre \t Precio \t Cantidad')
	print ('---------------------------------')
	
	cursor.execute("""select * from Productos where nombre=?""", (nombre,)) 
	
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2]) + '\t' + str(productos[3])
		print (str(product))
				
	con.commit()
	con.close()
	
	menu()
	
	
	
	
def eliminar():
	import os,sys,sqlite3
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from productos')
	print ('Estas en la opcion eliminar!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio \t Cantidad')
	print ('---------------------------------')
	for productos in cursor:
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2]) + '\t' + str(productos[3])
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
	menu()
	
def modificar():
	import os,sys,sqlite3
	producto = []
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from Productos')
	print ('Estas en la opcion modificar!!')
	print ('')
	print ('\t Cod \t Nombre \t Precio \t Cantidad')
	print ('---------------------------------')
	for productos in cursor:
		#Se usa lista producto en el for
		producto.append(productos)
		product = '\t' + str(productos[0]) + '\t' + str(productos[1]) + '\t' + str(productos[2]) + '\t' + str(productos[3])
		print (str(product))
		print ('')
	cod = input('Digite el codigo del producto a modificar: ')
	#productos: Tabla de la base de datos
	#producto: Lista
	for productos in producto:
		if (int(productos[0] == int(cod))):
			nombre   = productos[1]
			precio   = productos[2]
			cantidad = productos[3]
			encontrado = True
			break
	nombre   = input('Digite el nombre nuevo'   +nombre+ ':')
	precio   = input('Digite el precio nuevo'   +str(precio)+ ':')
	cantidad = input('Digite la cantidad nueva' +str(cantidad)+ ':')
	sql = "update Productos set Nombre='"+nombre+"', Precio='"+precio+"', Cantidad='"+cantidad+"' where cod="+cod
	cursor.execute(sql)
	con.commit()
	con.close()
	os.system('clear')
	print ('El producto ha sido modificado!!')
	print ('')
	menu()
	
def sumatoria():
	import os,sys,sqlite3
	total=0.0
	con = sqlite3.connect('ARTICULOS.s3db')
	cursor = con.cursor()
	cursor.execute('select * from Productos')
	print ('Estas en la opcion de mostrar el total!!')
	print ('')
	print ('')
	print ('\t Total')
	print ('---------------------------------') 
	
	for productos in cursor:
		total =  total + (productos[2]) * (productos[3]) 
	print ('La sumatoria es: ' ,round(total,2), ' !')
				
	con.commit()
	con.close()
	
	menu()
	
def creditos():
	print ('Programador: Agustin Salum')
	print ('Contacto:  agustinsalum92@hotmail.com')
	print ('Programa para control de pedidos: ctrlPed')
	print ('Version: 1.0')
	menu()

def salir():
	import os,sys
	print ('Has elegido salir!!')
	sys.exit()
	
	
menu()
