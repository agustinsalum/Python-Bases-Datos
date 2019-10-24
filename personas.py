
def Menu():
	import os,sys
	print ('Estas en el menu principal!!')
	print("")
	print ('1, Crear tabla')
	print ('2, Agregar cliente')
	print ('3, Eliminar cliente')
	print ('4, Ver todos los clientes')
	print ('5, Buscar cliente por dni')
	print ('6, Modificar datos de un cliente')
	print ('7, Eliminar tabla')
	print ('8, Salir del programa')
	
	#ASEGURAMOS QUE INGRESE 1..8
	try:
		opcion = int(input('Ingrese un numero de la opciones: '))
	except (ValueError):
		print ('No ingreso un numero. Vuelva a intentarlo')
		print ("")
		Menu()
	
	os.system('clear')
	if (opcion == 1):
		CrearTabla()
	elif (opcion == 2):
		Agregar()
	elif (opcion == 3):
		Eliminar()
	elif (opcion == 4):
		VerTodos()
	elif (opcion == 5):
		Buscar()
	elif (opcion == 6):
		Modificar()
	elif (opcion == 7):
		EliminarTabla()
	elif (opcion == 8):
		Salir()
	else:
		print ('Por favor digite un numero de los mencionados')
		Menu()
		

def CrearTabla():
	import os,sys,sqlite3
	clear = False
	#CONECTAMOS LA BASE DE DATOS
	con = sqlite3.connect('CLIENTES.s3db')
	print ('"""Estas en el menu de crear la base de datos"""')
	print ("")
	
	cursor = con.cursor()
	try:
		cursor.execute('''CREATE TABLE DATOS
		(ID INTEGER PRIMARY KEY NOT NULL,
		NOMBRE VARCHAR(20) NOT NULL,
		APELLIDO VARCHAR(20) NOT NULL,
		EDAD INTEGER,
		DNI INTEGER )                ''')
	#Por si la tabla ya fue creada!!
	except sqlite3.OperationalError as e:
		os.system('clear')
		clear = True
		message = e.args[0]
		if message.startswith("table DATOS already exists"):
			print("Advertencia!! La tabla ya fue creada!!")
			exists = False
		else:
			raise
			
	if (not clear):
		os.system('clear')
		print ('Se creo la tabla!!')
	
	con.commit()
	con.close()
	Menu()

def Agregar():
	import os,sys,sqlite3
	#CONECTAMOS LA BASE DE DATOS
	con = sqlite3.connect('CLIENTES.s3db')
	print ('Estas en el menu agregar')
	print ('')
	
	nombre = input ('Nombre: ')
	apellido = input ('Apellido: ')
	edad = int(input ('Edad: '))
	dni = int(input ('Dni: '))
	#LIMPIAMOS PANTALLA
	os.system('clear')
	cursor = con.cursor()
	#INSERTAMOS EN LA TABLA
	cursor.execute("INSERT INTO Datos(Nombre, Apellido, Edad, Dni) VALUES(?, ?, ?, ?)",(nombre, apellido, edad, dni))
	print ('Se agrego a la persona de manera correcta!!')
	con.commit()
	con.close()
	Menu()
	

def Eliminar():
	import os,sys,sqlite3
	con = sqlite3.connect('CLIENTES.s3db')
	cursor = con.cursor()
	cursor.execute('select * from Datos')
	print ('Estas en la opcion eliminar!!')
	print ('')
	print ('\t \t  Cod \t \t Nombre \t Apellido  \t Edad  \t \t Dni')
	print ('--------------------------------------------')
	for productos in cursor:
		#PRODUCTOS ES UNA LISTA
		product = '\t' '\t' + str(productos[0]) + '\t' '\t' + str(productos[1]) + '\t' '\t' + str(productos[2] + '\t' '\t' + str(productos[3]) + '\t' '\t' + str(productos[4]))
		print (str(product))
		print ('')
	
	
	cod = input ('Ingrese el codigo a eliminar: ')
	#ID en linux / COD en windows
	sql = 'delete from Datos where id='+cod
	cursor.execute(sql)
	con.commit()
	con.close()
	#LIMPIAMOS PANTALLA
	os.system('clear')
	print ('El producto ha sido eliminado')
	print ('')
	Menu()
	
	
def VerTodos():
	import os,sys,sqlite3
	con = sqlite3.connect('CLIENTES.s3db')
	cursor = con.cursor()
	cursor.execute('select * from Datos')
	print ('Estas en la opcion ver todos los clientes!!')
	print ('')
	print ('\t \t  Cod \t \t Nombre \t Apellido  \t Edad  \t \t Dni')
	print ('--------------------------------------------')
	for productos in cursor:
		#PRODUCTOS ES UNA LISTA
		product = '\t' '\t' + str(productos[0]) + '\t' '\t' + str(productos[1]) + '\t' '\t' + str(productos[2] + '\t' '\t' + str(productos[3]) + '\t' '\t' + str(productos[4]))
		print (str(product))
		print ('')
	
	con.commit()
	con.close()
	print ('')
	print ('Presione una tecla para continuar')
	input('')
	os.system('clear')
	Menu()	
	
	
def Buscar():
	import os,sys,sqlite3
	con = sqlite3.connect('CLIENTES.s3db')
	cursor = con.cursor()
	
	print ('Estas en la opcion buscar cliente por dni!!')
	print ('')
	
	dni = input ('Ingrese el dni: ')
	cursor.execute("""select * from Datos where dni=?""", (dni,))
	
	print ('\t \t  Cod \t \t Nombre \t Apellido  \t Edad  \t \t Dni')
	print ('--------------------------------------------')
	for productos in cursor:
		#PRODUCTOS ES UNA LISTA
		product = '\t' '\t' + str(productos[0]) + '\t' '\t' + str(productos[1]) + '\t' '\t' + str(productos[2] + '\t' '\t' + str(productos[3]) + '\t' '\t' + str(productos[4]))
		print (str(product))
		print ('')
	
	con.commit()
	con.close()
	print ('')
	print ('Presione una tecla para continuar')
	input('')
	os.system('clear')
	Menu()	
	
	
def Modificar():
	pass
	
	

	
def EliminarTabla():
	import os,sys,sqlite3
	#CONECTAMOS LA BASE DE DATOS
	con = sqlite3.connect('CLIENTES.s3db')
	print ('"""Estas en el menu de eliminar la base de datos"""')
	print ("")
	
	cursor = con.cursor()
	
	cursor.execute('DROP TABLE DATOS')
	os.system('clear')
	print ('Se elimino la tabla datos!!')
	con.commit()
	con.close()
	Menu()
	
	
def Salir():
	import os,sys
	print ('Has elegido salir!!')
	sys.exit()


	
"""PROGRAMA PRINCIPAL"""

Menu()
