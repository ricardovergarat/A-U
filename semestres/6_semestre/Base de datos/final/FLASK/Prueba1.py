import random
import cx_Oracle
from flask import Flask
from flask import render_template, url_for, redirect, request
from flask_login import LoginManager
from flask_login import current_user, login_user, logout_user
from Usuario import Usuario

app = Flask(__name__)
#connect() recibe como parametros el usuario la contraseña , el host con el puerto y con el tipo de base de datos.
conexion = cx_Oracle.connect("TRABAJO_FINAL", "1234", "localhost:1521/XE")#mantenedor/Pagina
conexion2 = cx_Oracle.connect("TRABAJO_FINAL", "1234", "localhost:1521/XE") #digitalizador
#conex_cliente = cx_Oracle.connect("CLIENTE", "CLIENTE","localhost:1521/XE") #comprador

login_manager = LoginManager(app)

@login_manager.user_loader

def load_user(rut):
	cur = conexion.cursor()
	cur.execute('SELECT NOMBRE_CLIENTE, RUT FROM CLIENTE WHERE RUT = :RUT', [rut])
	fetch = cur.fetchone()
	if (fetch == None):
		return None

	else:
		return Usuario(fetch[0], fetch[1])

app.config["SECRET_KEY"]= 'Cualquier_Cosa'

@app.route('/iniciasesion', methods = ['GET', 'POST'])

def iniciasesion():
	#conexion para clientes y administradores
	global conexion2
	mensaje=""
	if current_user.is_authenticated:
		return redirect(url_for("Inicio"))
	else:

		if request.method == "POST":
			rut = request.form["Rut_C"]
			contraseña = request.form["Contraseña_C"]

			cur= conexion.cursor()
			cur.execute('SELECT NOMBRE_CLIENTE, RUT, ADMINISTRADOR, CONTRASEÑA FROM CLIENTE WHERE RUT= :RUT AND CONTRASEÑA = :CONTRASENA', [rut, contraseña])
			fetch = cur.fetchone()
			cur.execute('SELECT RUT FROM CLIENTE WHERE RUT = :RUT',[rut])
			fetch2 = cur.fetchone()

			if fetch2 == None:
				mensaje = "Usuario no encontrado"
			elif fetch == None:
				mensaje = "Contraseña Incorrecta"

			else:
				login_user(Usuario(fetch[0], fetch[1]))
				if fetch[2] == "si":
					conexion2 = cx_Oracle.connect("ADMINISTRADOR","ADMINISTRADOR","localhost:1521/XE")
				else:
					conexion2 = cx_Oracle.connect("CLIENTE","CLIENTE","localhost:1521/XE")
				return redirect(url_for('Inicio'))

	return render_template("iniciasesion.html", mensaje=mensaje)

@app.route('/cerrarsesion')

def cerrarsesion():
	if current_user.is_authenticated:
		logout_user()

	return redirect(url_for("Inicio"))
	


#app.route es para asignar una ruta, se le puede asignar distintos metodos, los usados seran get y post, get para solicitar informacion, post para entregar informacion
@app.route('/Carrito', methods=['GET','POST'])

def carrito():
	mensaje=""
	cur = conexion.cursor()
	cur.execute("SELECT CODIGO_PRODUCTO, CANTIDAD, TOTAL FROM SUPERMERCADO.CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT ORDER BY CODIGO_CARRO" ,[current_user.rut] )
	mostrar = cur.fetchall()
	cur.execute("SELECT NOMBRE, CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE CODIGO_PRODUCTO IN (SELECT CODIGO_PRODUCTO FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT)",[current_user.rut] )
	mostrar2 = cur.fetchall()
	for i in range(len(mostrar)):
		for j in range(len(mostrar)):
			try:
				if mostrar[i][0] == mostrar2[j][1]:
					mostrar[i] = mostrar[i] + mostrar2[j]
			except:
				pass
	cur.execute("SELECT SUM(TOTAL) FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT",[current_user.rut])
	totalC = cur.fetchall()
	if "Opcion" in request.form:
		if request.form["Opcion"] == "Pagar":
			cur = conexion.cursor()
			cur.execute("SELECT * FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT",[current_user.rut])
			revision = cur.fetchone()
			if revision == None:
				mensaje="No hay nada en el Carrito"
			else:
				return redirect(url_for('credito'))
	for i in mostrar:
		if "Opcion " + i[3] in request.form:
			cur.execute("SELECT CODIGO_CARRO FROM SUPERMERCADO.CARRO_TEMPORAL WHERE CODIGO_PRODUCTO = (SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE NOMBRE = :NOMBRE) AND RUT_CLIENTE = :RUT",[i[3],current_user.rut])
			Codigo_Carro = cur.fetchall()
			cur.execute("SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE NOMBRE = :NOMBRE",[i[3]])
			Codigo_Producto = cur.fetchall()
			Cantidad_Nueva = request.form["Cantidad_Nueva"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_CANTIDAD_VENTA(:CODIGO_CARRO,:CODIGO_PRODUCTO,:CANTIDAD_NUEVA, :MENSAJE)",[Codigo_Carro[0][0], Codigo_Producto[0][0] , Cantidad_Nueva, mensaje])
			mensaje = mensaje.getvalue()
			cur = conexion.cursor()
			cur.execute("SELECT CODIGO_PRODUCTO, CANTIDAD, TOTAL FROM SUPERMERCADO.CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT ORDER BY CODIGO_CARRO" ,[current_user.rut] )
			mostrar = cur.fetchall()
			cur.execute("SELECT NOMBRE, CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE CODIGO_PRODUCTO IN (SELECT CODIGO_PRODUCTO FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT)",[current_user.rut] )
			mostrar2 = cur.fetchall()
			for i in range(len(mostrar)):
				for j in range(len(mostrar)):
					try:
						if mostrar[i][0] == mostrar2[j][1]:
							mostrar[i] = mostrar[i] + mostrar2[j]
					except:
						pass
			cur.execute("SELECT SUM(TOTAL) FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT",[current_user.rut])
			totalC = cur.fetchall()
		elif "Quitar " +i[3] in request.form:
			cur.execute("SELECT CODIGO_CARRO FROM SUPERMERCADO.CARRO_TEMPORAL WHERE CODIGO_PRODUCTO = (SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE NOMBRE = :NOMBRE) AND RUT_CLIENTE = :RUT",[i[3],current_user.rut])
			Codigo_Carro = cur.fetchall()
			cur.execute("CALL ELIMINAR_CARRO(:CODIGO, :MENSAJE)",[Codigo_Carro[0][0] , mensaje])
			cur.execute("SELECT CODIGO_PRODUCTO, CANTIDAD, TOTAL FROM SUPERMERCADO.CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT ORDER BY CODIGO_CARRO" ,[current_user.rut] )
			mostrar = cur.fetchall()
			cur.execute("SELECT NOMBRE, CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE CODIGO_PRODUCTO IN (SELECT CODIGO_PRODUCTO FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT)",[current_user.rut] )
			mostrar2 = cur.fetchall()
			for i in range(len(mostrar)):
				for j in range(len(mostrar)):
					try:
						if mostrar[i][0] == mostrar2[j][1]:
							mostrar[i] = mostrar[i] + mostrar2[j]
					except:
						pass
			cur.execute("SELECT SUM(TOTAL) FROM CARRO_TEMPORAL WHERE RUT_CLIENTE = :RUT",[current_user.rut])
			totalC = cur.fetchall()
	
	return render_template("Carrito.html", carrito = mostrar, mensaje=mensaje, TotalC=totalC)

@app.route('/registro', methods = ['GET','POST'])

def registro():
	cur = conexion.cursor()
	cur.execute("SELECT RUT FROM CLIENTE WHERE ADMINISTRADOR = 'si'")
	Administradores = cur.fetchall()
	Admins = []
	for i in range(len(Administradores)):
		Admins.append(Administradores[i][0])
	mensaje = "	"
	if request.method == 'POST':
		Admin = "NO"
		if "Ingresar_Admin" in request.form:
			Admin ="SI"
		Rut_C = request.form["Rut_C"]
		Contrasena = request.form["Contrasena"]
		Nombre_C = request.form["Nombre_C"]
		Apellido_C = request.form["Apellido_C"]
		FechaNac_C = request.form["FechaNac_C"] 
		Telefono1_C = request.form["Telefono1_C"]
		Comuna_C = request.form["Comuna_C"]
		Calle_C = request.form["Calle_C"]
		Num_Casa_C = request.form["Num_Casa_C"]
		Num_Depa_C = request.form["Num_Depa_C"]
		Bloque_Depa_C = request.form["Bloque_Depa_C"]
		Email_C = request.form["Email_C"]
		cur = conexion.cursor()
		mensaje = cur.var(str)
		try:
			cur.execute("CALL INGRESAR_CLIENTE(:RUT,:CONTRASENA,:ADMIN,:NOMBRE,:APELLIDO,:FECHA,:TELEFONO1,:COMUNA,:CALLE,:NUMCASA,:NUMDEPA,:BLOQUEDEPA,:CORREO,:MENSAJE)",[Rut_C, Contrasena, Admin, Nombre_C, Apellido_C, FechaNac_C, Telefono1_C, Comuna_C, Calle_C, Num_Casa_C, Num_Depa_C, Bloque_Depa_C, Email_C,mensaje])
			mensaje = mensaje.getvalue()
		except:
			mensaje = "HA OCURRIDO UN ERROR, INTENTELO NUEVAMENTE Y REVISE SUS DATOS"
		cur.close()
	
	return render_template("registrar.html", mensaje=mensaje, Admins=Admins)

@app.route('/', methods = ['GET', 'POST'])

def Inicio():
	mensaje=""
	cur = conexion.cursor()
	cur.execute('SELECT NOMBRE, PRECIO, STOCK, CODIGO_PRODUCTO FROM PRODUCTO WHERE STOCK > 0 ')
	mostrar = cur.fetchall()
	cur.execute("SELECT NOMBRE_CATEGORIA FROM CATEGORIA")
	mostrar_Categorias = cur.fetchall()
	cur.execute("SELECT NOMBRE FROM PRODUCTO")
	nombres = cur.fetchall()
	lista_Producto = []
	for i in range(len(nombres)):
		lista_Producto.append(nombres[i][0])

	cur.execute("SELECT NOMBRE_CATEGORIA FROM CATEGORIA")
	lista_Categoria = []
	nombres = cur.fetchall()
	for i in range(len(nombres)):
		lista_Categoria.append(nombres[i][0])
	cur.execute("SELECT RUT FROM CLIENTE WHERE ADMINISTRADOR = 'si'")
	Administradores = cur.fetchall()
	Admins = []
	for i in range(len(Administradores)):
		Admins.append(Administradores[i][0])
	if request.method == 'POST':
		if "Categoria" in request.form:
			for i in lista_Categoria:
				if request.form["Categoria"] == i:
					cur = conexion.cursor()
					cur.execute("SELECT NOMBRE, PRECIO, STOCK, CODIGO_PRODUCTO FROM PRODUCTO WHERE CODIGO_CATEGORIA IN (SELECT CODIGO_CATEGORIA FROM CATEGORIA WHERE NOMBRE_CATEGORIA = :NOMBRE_CATEGORIA )",[i] )
					mostrar = cur.fetchall()
		elif "Agregar al Carrito" in request.form:
			for i in lista_Producto:
				if request.form["Agregar al Carrito"] == 'Agregar al carrito ' + i:
					cur = conexion.cursor()
					cur.execute("SELECT CODIGO_PRODUCTO FROM PRODUCTO WHERE :NOMBRE = NOMBRE", [i])
					mostrar = cur.fetchall()
					mensaje= cur.var(str)
					cur.execute("CALL INGRESAR_CARRO_TEMPORAL(:RUT, :CODIGO, :CANTIDAD, :MENSAJE)",[float(current_user.rut) , float(mostrar[0][0]), float(request.form["Cantidad"]),mensaje])
					mensaje= mensaje.getvalue()
					cur.close()
					cur = conexion.cursor()
					cur.execute('SELECT NOMBRE, PRECIO, STOCK, CODIGO_PRODUCTO FROM PRODUCTO WHERE STOCK > 0 ')
					mostrar = cur.fetchall()
		cur.close()

	else:
		cur = conexion.cursor()
		cur.execute('SELECT NOMBRE, PRECIO, STOCK, CODIGO_PRODUCTO FROM PRODUCTO WHERE STOCK > 0 ')
		mostrar = cur.fetchall()
		cur.close()
	return render_template("Inicio.html", fila= mostrar, Admins= Admins, mensaje=mensaje, mostrar_Categorias=mostrar_Categorias)


@app.route('/Boleta', methods=['GET','POST'])

def Boleta():
	cur = conexion2.cursor()
	cur.execute('SELECT CODIGO_BOLETA, CODIGO_SEGUIMIENTO, FECHA_BOLETA,b.TIPO_PAGO.NOMBRE_PAGO, TOTAL FROM SUPERMERCADO.BOLETA b WHERE CODIGO_SEGUIMIENTO IN (SELECT MAX(CODIGO_SEGUIMIENTO) FROM SUPERMERCADO.DESPACHO WHERE RUT_CLIENTE = :RUT)', [current_user.rut])
	mostrar = cur.fetchall()
	cur.execute('SELECT ESTADO, TIEMPO_ENTREGA, COSTO_DESPACHO FROM SUPERMERCADO.DESPACHO WHERE RUT_CLIENTE = :RUT',[current_user.rut])
	despacho = cur.fetchall()
	cur.execute('SELECT R.NOMBRE_REPARTIDOR.NOMBRE, R.NOMBRE_REPARTIDOR.APELLIDO FROM SUPERMERCADO.REPARTIDOR R WHERE RUT IN (SELECT RUT_REPARTIDOR FROM SUPERMERCADO.DESPACHO WHERE CODIGO_SEGUIMIENTO = :CODIGO)',[mostrar[0][1]])
	repartidor= cur.fetchall()
	print(repartidor)
	cur.execute('SELECT NOMBRE FROM SUPERMERCADO.PRODUCTO WHERE CODIGO_PRODUCTO IN (SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.DETALLE WHERE CODIGO_BOLETA = :CODIGO)',[mostrar[0][0]])
	NombreP = cur.fetchall()
	cur.execute('SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.PRODUCTO WHERE CODIGO_PRODUCTO IN (SELECT CODIGO_PRODUCTO FROM SUPERMERCADO.DETALLE WHERE CODIGO_BOLETA = :CODIGO)',[mostrar[0][0]])
	CodProducto = cur.fetchall()
	cur.execute('SELECT TOTAL FROM SUPERMERCADO.DETALLE WHERE CODIGO_BOLETA = :CODIGO',[mostrar[0][0]])
	Total = cur.fetchall()
	cur.execute('SELECT COUNT(*) FROM SUPERMERCADO.DETALLE WHERE CODIGO_BOLETA = :CODIGO',[mostrar[0][0]])
	cantidad = cur.fetchone()
	return render_template("Boleta.html", mostrar = mostrar, despacho=despacho, repartidor=repartidor, NombreP=NombreP, Total=Total, CodProducto=CodProducto, Cantidad=cantidad)


@app.route('/credito', methods=['GET','POST'])
def credito():
	mensaje = ""
	mensaje2 = ""
	if request.method == "POST":
		if "Tipo_Pago" in request.form:
			if request.form["Tipo_Pago"] == "Credito":
				mensaje2 = "Credito"
			elif request.form["Tipo_Pago"] == "Debito":
				mensaje2="Debito"
		else:
			if "Pago_Credito" in request.form:
				cur = conexion.cursor()
				mensaje=cur.var(str)
				cur.execute("SELECT RUT FROM REPARTIDOR")
				nombres = cur.fetchall()
				lista_repartidor = []
				for i in range(len(nombres)):
					lista_repartidor.append(nombres[i][0])
				rutr = int(random.choice(lista_repartidor))
				numtarjeta = request.form["Numero_Tarjeta"]
				fexpiracion = request.form["Fecha_Expiracion"]
				cvv = request.form["CVV"]
				cur.execute("CALL INGRESAR_CARRO(:RUT, :RUTR,'En Proceso','Credito',:NUMEROTARJETA,:FECHAEXPIRACION,:CVV,:MENSAJE )",[current_user.rut, rutr, numtarjeta, fexpiracion, cvv, mensaje])
				mensaje = mensaje.getvalue()
				cur.close()
			elif "Pago_Debito" in request.form:
				cur = conexion.cursor()
				mensaje=cur.var(str)
				cur.execute("SELECT RUT FROM REPARTIDOR")
				nombres = cur.fetchall()
				lista_repartidor = []
				for i in range(len(nombres)):
					lista_repartidor.append(nombres[i][0])
				rutr = int(random.choice(lista_repartidor))
				numtarjeta = request.form["Rut_Tarjeta"]
				cur.execute("CALL INGRESAR_CARRO(:RUT, :RUTR,'En Proceso','Debito',:NUMEROTARJETA,'12-12-2030',NULL,:MENSAJE )",[current_user.rut, rutr, numtarjeta, mensaje])
				mensaje = mensaje.getvalue()
				cur.close()


	return render_template("credito.html", mensaje=mensaje, mensaje2=mensaje2)

@app.route('/Admin', methods=['GET','POST'] )
def admin():
	#Mensaje sera para los errores y mensaje2 sera para los botones
	cur = conexion.cursor()
	cur.execute("SELECT RUT FROM CLIENTE WHERE ADMINISTRADOR = 'si'")
	Administradores = cur.fetchall()
	Admins = []
	for i in range(len(Administradores)):
		Admins.append(Administradores[i][0])
	if current_user.rut in Admins:
		mensaje=""
		mensaje2=""
		cur = conexion2.cursor()
		cur.execute("SELECT * FROM SUPERMERCADO.CATEGORIA")
		categorias = cur.fetchall()
		if request.method == 'POST':
			if "Ingresar" in request.form:
				#Producto
				if request.form["Ingresar"] == "Ingresar Producto":
					Nombre_Producto = request.form["Nombre_Producto"]
					Precio_Producto = request.form["Precio"]
					Codigo_Categoria = request.form["Codigo_Categoria"]
					Restringido = request.form["Restringido"]
					Stock = request.form["Stock"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.INGRESAR_PRODUCTO(:Nombre,:Precio,:Codigo,:Restringido,:Stock,:MENSAJE)",[Nombre_Producto, Precio_Producto, Codigo_Categoria, Restringido, Stock, mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Actualizar Nombre":
					cur = conexion2.cursor()
					Nombre_Producto = request.form["Nombre_Producto"]
					Codigo_Producto = request.form["Codigo_Producto"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_NOMBRE_PRODUCTO(:CODIGO, :NOMBRE, :MENSAJE)",[Codigo_Producto, Nombre_Producto, mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Actualizar Precio":
					cur = conexion2.cursor()
					Precio_Producto = request.form["Precio"]
					Codigo_Producto = request.form["Codigo_Producto"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_PRECIO(:CODIGO, :PRECIO, :MENSAJE)",[Codigo_Producto, Precio_Producto, mensaje])
					mensaje= mensaje.getvalue()
				elif request.form["Ingresar"] == "Actualizar Estado":
					cur = conexion2.cursor()
					Restringido = request.form["Restringido"]
					Codigo_Producto = request.form["Codigo_Producto"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_RESTRICION(:CODIGO,:RESTRICCION, :MENSAJE)",[Codigo_Producto, Restringido,mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Agregar Stock":
					cur = conexion2.cursor()
					Stock = request.form["Stock"]
					Codigo_Producto = request.form["Codigo_Producto"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.AGREGAR_STOCK(:CODIGO,:STOCK,:MENSAJE)",[Codigo_Producto,Stock,mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Eliminar Stock":
					cur = conexion2.cursor()
					Stock = request.form["Stock"]
					Codigo_Producto = request.form["Codigo_Producto"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.QUITAR_STOCK(:CODIGO,:STOCK,:MENSAJE)",[Codigo_Producto,Stock,mensaje])
					mensaje = mensaje.getvalue()
				#Categoria
				elif request.form["Ingresar"] == "Ingresar Categoria":
					cur = conexion2.cursor()
					Nombre_Categoria = request.form["NombreCategoria"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.INGRESAR_CATEGORIA(:Nombre, :MENSAJE)",[Nombre_Categoria, mensaje])
					mensaje = mensaje.getvalue()
					cur.execute("SELECT * FROM SUPERMERCADO.CATEGORIA")
					categorias = cur.fetchall()
				elif request.form["Ingresar"] == "Actualizar Nombre de Categoria":
					cur = conexion2.cursor()
					Nombre_c = request.form["Actualizar_Categoria"]
					Codigo_c = request.form["Codigo_Categoria"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_NOMBRE_CATEGORIA(:CODIGO, :NOMBRE, :MENSAJE)", [Codigo_c, Nombre_c, mensaje])
					mensaje = mensaje.getvalue()
					cur.execute("SELECT * FROM SUPERMERCADO.CATEGORIA")
					categorias = cur.fetchall()
				#Repartidor
				elif request.form["Ingresar"] == "Ingresar Repartidor":
					cur = conexion2.cursor()
					Rut_Repartidor= request.form["Rut_Repartidor"]
					Nombre_Repartidor = request.form["Nombre_Repartidor"]
					Apellido_Repartidor = request.form["Apellido_Repartidor"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.INGRESAR_REPARTIDOR(:RUT, :NOMBRE, :APELLIDO, :MENSAJE)",[Rut_Repartidor,Nombre_Repartidor,Apellido_Repartidor, mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Actualizar Nombre_Repartidor":
					cur = conexion2.cursor()
					Rut_Repartidor = request.form["Rut_Repartidor"]
					Nombre_Repartidor = request.form["Nombre_Repartidor"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_NOMBRE_REPARTIDOR(:RUT, :NOMBRE, :MENSAJE)",[Rut_Repartidor,Nombre_Repartidor,mensaje])
					mensaje = mensaje.getvalue()
				elif request.form["Ingresar"] == "Actualizar Apellido_Repartidor":
					cur = conexion2.cursor()
					Rut_Repartidor = request.form["Rut_Repartidor"]
					Apellido_Repartidor = request.form["Apellido_Repartidor"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.ACTUALIZAR_APELLIDO_REPARTIDOR(:RUT, :APELLIDO, :MENSAJE)",[Rut_Repartidor, Apellido_Repartidor,mensaje])
				#Cliente
				elif request.form["Ingresar"] == "Cambiar a Administrador":
					cur = conexion2.cursor()
					Rut = request.form["Rut_Cliente"]
					mensaje = cur.var(str)
					cur.execute("CALL SUPERMERCADO.CAMBIO_ADMINISTRADOR(:RUT, 'si', :MENSAJE)",[Rut, mensaje])
					mensaje = mensaje.getvalue()
				
			elif "Formulario" in request.form:
				if request.form["Formulario"] == " Ingresar Producto ":
					mensaje2="Ingresar Producto"
				elif request.form["Formulario"] == "Actualizar Producto":
					mensaje2="Actualizar Producto"
				elif request.form["Formulario"] == " Ingresar Categoria ":
					mensaje2="Ingresar Categoria"
				elif request.form["Formulario"] == " Ingresar Repartidor ":
					mensaje2="Ingresar Repartidor"
				elif request.form["Formulario"] == "Actualizar Categoria":
					mensaje2="Actualizar Categoria"
				elif request.form["Formulario"] == "Actualizar Repartidor":
					mensaje2="Actualizar Repartidor"
				elif request.form["Formulario"] == "Actualizar Cliente":
					mensaje2="Actualizar Cliente"
		cur.close()
	else:
		return redirect(url_for("Inicio"))
	return render_template("Admin.html", categorias=categorias, mensaje=mensaje, mensaje2=mensaje2)

@app.route('/Encuesta', methods=['GET','POST'])

def Encuesta():
	if request.method ==  "POST":
		opcion1 = request.form["Pregunta1"]
		opcion2 = request.form["Pregunta2"] 
		opcion3 = request.form["Pregunta3"]
		opcion4 = request.form["Pregunta4"]
		opcion5 = request.form["Pregunta5"]
		cur = conexion.cursor()
		mensaje = cur.var(str)
		cur.execute("CALL INSERTAR_ENCUESTA(:RUT,:OPCION1,:OPCION2,:OPCION3,:OPCION4,:OPCION5,:MENSAJE)",[current_user.rut, opcion1, opcion2, opcion3, opcion4, opcion5, mensaje])
		mensaje = mensaje.getvalue()
		return redirect(url_for("Inicio"))
	return render_template("Encuesta.html")

@app.route('/ActualizarDatos', methods=['GET','POST'])
def ActualizarDatos():
	mensaje=""
	if request.method=="POST":
		if request.form["Ingresar"] == "Actualizar Correo":
			cur = conexion.cursor()
			Correo = request.form["Correo"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_CORREO(:RUT, :CORREO, :MENSAJE)",[current_user.rut, Correo, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Cambiar Contraseña":
			cur = conexion.cursor()
			Contraseña = request.form["Contraseña"]
			Confirmar_Contraseña = request.form["Confirmar_Contraseña"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_CONTRASEÑA(:RUT, :CONTRASEÑA, :CONTRASEÑA2, :MENSAJE)",[current_user.rut, Contraseña, Confirmar_Contraseña, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Actualizar Comuna":
			cur = conexion.cursor()
			Comuna = request.form["Comuna"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_COMUNA(:RUT, :COMUNA, :MENSAJE)",[current_user.rut, Comuna, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Actualizar Calle":
			cur = conexion.cursor()
			Calle = request.form["Calle"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_CALLE(:RUT, :CALLE, :MENSAJE)",[current_user.rut, Calle, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Actualizar Numero Casa":
			cur = conexion.cursor()
			Numero_Casa = request.form["Numero_Casa"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_NUMERO_CASA(:RUT, :NUMERO, :MENSAJE)",[current_user.rut, Numero_Casa, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Actualizar Numero Departamento":
			cur = conexion.cursor()
			Numero_Departamento = request.form["Numero_Departamento"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_NUMERO_DEPARTAMENTO(:RUT, :NUMERO, :MENSAJE)",[current_user.rut, Numero_Departamento, mensaje])
			mensaje = mensaje.getvalue()
		elif request.form["Ingresar"] == "Actualizar Bloque Departamento":
			cur = conexion.cursor()
			Bloque_Departamento = request.form["Bloque_Departamento"]
			mensaje = cur.var(str)
			cur.execute("CALL SUPERMERCADO.ACTUALIZAR_BLOQUE(:RUT,:BLOQUE,:MENSAJE)",[current_user.rut, Bloque_Departamento, mensaje])
			mensaje = mensaje.getvalue()
	return render_template("ActualizarDatos.html", mensaje=mensaje)

@app.route('/MisDatos', methods= ['GET', 'POST'])
def MisDatos() :
	
	cur= conexion2.cursor()
	cur.execute("SELECT RUT, C.NOMBRE_CLIENTE.NOMBRE, C.NOMBRE_CLIENTE.APELLIDO, FECHA_NACIMIENTO, TELEFONO, C.DIRECCION_CLIENTE.COMUNA, C.DIRECCION_CLIENTE.CALLE, C.DIRECCION_CLIENTE.NUMERO_CASA, C.DIRECCION_CLIENTE.NUMERO_DEPARTAMENTO, C.DIRECCION_CLIENTE.BLOQUE, CORREO  FROM SUPERMERCADO.CLIENTE c WHERE RUT= :RUT", [current_user.rut])
	Datos = cur.fetchall()
	cur.close()

	return render_template("MisDatos.html", Datos=Datos)

if __name__  == "__main__":

	app.run(host="0.0.0.0",port=80, debug=True)