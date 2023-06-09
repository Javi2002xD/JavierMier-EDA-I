#UNIVERSIDAD NACIONAL AUTÓNOMA DE MEXICO
#FACULTAD DE INGENIERIA
#ESTRUCTURA DE DATOS Y ALGORITMOS 
#JAVIER MIER RAMIREZ
#PROYECTO FINAL: SISTEMA DE SUPERMERCADO

class Producto:
	def __init__(self, nombre, precio, codigo):
		self.nombre = nombre
		self.precio = precio
		self.codigo = codigo

class Productodef:
	def __init__(self, nombredef, codigodef, queja):
		self.nombredef = nombredef
		self.codigodef = codigodef
		self.queja = queja

class Trabajador:
	def __init__(self, nombreT, codigoT, puesto):
		self.nombreT = nombreT
		self.codigoT = codigoT
		self.puesto = puesto

#Inventario base 
list_inventario = []
producto = Producto("Arroz", 25, 1001) 
list_inventario.append(producto)
producto = Producto("Azucar", 23, 1002) 
list_inventario.append(producto)
producto = Producto("Harina", 15, 1003) 
list_inventario.append(producto)
producto = Producto("Pan", 7, 1004) 
list_inventario.append(producto)
producto = Producto("Aceite", 52, 1005) 
list_inventario.append(producto)
producto = Producto("Mayonesa", 70, 1006) 
list_inventario.append(producto)
producto = Producto("Agua", 10, 1007) 
list_inventario.append(producto)
producto = Producto("Cafe", 45, 1008) 
list_inventario.append(producto)
producto = Producto("Cerveza", 17, 1009) 
list_inventario.append(producto)
producto = Producto("Jugo", 20, 1010) 
list_inventario.append(producto)
producto = Producto("Jabon", 13, 1011) 
list_inventario.append(producto)
producto = Producto("Crema", 30, 1012) 
list_inventario.append(producto)
producto = Producto("Leche", 25, 1013) 
list_inventario.append(producto)
producto = Producto("Huevo", 34, 1014) 
list_inventario.append(producto)
producto = Producto("Atun", 15, 1015) 
list_inventario.append(producto)
producto = Producto("Frijol", 35, 1016) 
list_inventario.append(producto)
producto = Producto("Sal", 13, 1017) 
list_inventario.append(producto)
producto = Producto("Pollo", 44, 1018) 
list_inventario.append(producto)
producto = Producto("Papel", 20, 1019) 
list_inventario.append(producto)
producto = Producto("Salchicha", 30, 1020) 
list_inventario.append(producto)

#Personal base
list_personal = []
trabajador = Trabajador("Ramirez Gomez Juan", 2001, "limpieza")
list_personal.append(trabajador)
trabajador = Trabajador("Martinez Solano Adan", 2002, "venta")
list_personal.append(trabajador)
trabajador = Trabajador("Hernandez Salvador Luis", 2003, "caja")
list_personal.append(trabajador)

def menu():
	print("\tSistema de administración de puma abarrotero S.A de C.V\n")
	print("\t 1. Administracion de inventario.\n\t 2. Atención a clientes\n\t 3. Administraciónde personal\n\t 4. Salir\n")

def inventario():
	while True:
		print("\t\t 1. Agregar suministros.\n\t\t 2. Quitar suministros.\n\t\t 3. Ordenar sumnistros (por precio) ")
		print("\t\t 4. Ver lista de inventario. \n\t\t 5. Ver lista inventario ordenada (primero hay que ordenarla). \n\t\t 6. Salir\n")
		opinventario = int(input("\t\tInserte la opcion que desee: "))

		if opinventario == 1:
			addsuministros(list_inventario)
		elif opinventario == 2:
			quitsuministros(list_inventario)
		elif opinventario == 3:
			list_inventario_ordenada = sortsuministros(list_inventario)
		elif opinventario == 4:
			ver_lista_inventario(list_inventario)
		elif opinventario == 5:
			ver_inventario_ordenado(list_inventario_ordenada)
		elif opinventario == 6:
			print("\n\tGracias\n")
			break
		else:
			print("\n\t\tElija una opcion correcta\n")

def addsuministros(list_inventario):
	nombre = input("\t Ingrese el nombre del producto (iniciando con mayuscula): ")
	precio = int(input("\t Ingrese el precio unitario: "))
	codigo = int(input("\t Ingrese el codigo del producto: "))
	producto = Producto(nombre, precio, codigo)
	list_inventario.append(producto)

def quitsuministros(list_inventario):
	nombre = input("\t Ingrese el nombre del producto que desea eliminar: ")
	for producto in list_inventario:
		if producto.nombre == nombre:
			list_inventario.remove(producto)
			return
	print("\tEl producto no se encontro en la lista\n")

def sortsuministros(list_inventario):
    if len(list_inventario) <= 1:
        return list_inventario
    
    pivote = list_inventario[len(list_inventario) // 2]
    menor = [x for x in list_inventario if x.precio < pivote.precio]
    igual = [x for x in list_inventario if x.precio == pivote.precio]
    mayor = [x for x in list_inventario if x.precio > pivote.precio]
    
    return sortsuministros(menor) + igual + sortsuministros(mayor)

list_cliente = []
quejas = []

def clientes():
	while True:
		print("\t\t 1. Cobro de productos.\n\t\t 2. Atencion a clientes (quejas). ")
		print("\t\t 3. Ver lista de productos comprados. \n\t\t 4. Ver lista de quejas. \n\t\t 5. Salir\n")
		opclientes = int(input("\t\t Inserte la opcion que desee: "))

		if opclientes == 1:
			ver_lista_inventario(list_inventario)
			op1 = int(input("\t\tDesea comprar ingresando el codigo o el nombre del producto? 1. Nombre, 2. Codigo: "))

			if op1 == 1:
				n=1
				while n==1:
					co_productos_nombre(list_cliente)
					print("\t\t Total: ", monto())
					op2 = int(input("\t\tDesea seguir ingresando productos? 1. Si, 2.No: "))

					if op2 == 1:
						n=1
					elif op2 == 2:
						n=2
					else:
						print("\t\tElija una ocion correcta\n")

			elif op1 == 2:
				n=1
				while n==1:
					co_productos_codigo(list_cliente)
					print("\t\t Total: ", monto())
					op2 = int(input("\t\tDesea seguir ingresando productos? 1. Si, 2.No: "))

					if op2 == 1:
						n=1
					elif op2 == 2:
						n=2
					else:
						print("\t\tElija una ocion correcta\n")


		elif opclientes == 2:
			ate_clientes(quejas)
		elif opclientes == 3:
			ver_lista_cliente(list_cliente)
		elif opclientes == 4:
			ver_lista_quejas(quejas)
		elif opclientes == 5:
			print("\t\tGracias\n")
			break
		else:
			print("\n\t\tElija una opcion valida\n")

def co_productos_nombre(list_cliente):
	nombre_producto = input("\t\t Ingrese el nombre del produto a comprar: ")
	for producto in list_inventario:
		if producto.nombre == nombre_producto:
			list_cliente.append(producto)

def co_productos_codigo(list_cliente):
	codigo_producto = int(input("\t\t Ingrese el codigo del producto a comprar: "))
	for producto in list_inventario:
		if producto.codigo == codigo_producto:
			list_cliente.append(producto)

def monto():
	total = 0
	for producto in list_cliente:
		total += producto.precio

	return total

def ate_clientes(quejas):
	print("\t\tLamentamos las molestias\n")
	codigodef = int(input("\t\t Ingrese el codigo del producto defectuso: "))
	queja = input("\t\t Ingrese la inconformidad al comprar al producto: ")
	for producto in list_inventario:
		if producto.codigo == codigodef:
			productodef = Productodef(producto.nombre, codigodef, queja)
			quejas.append(productodef)

def ver_lista_inventario(list_inventario):
    print("\tInventario: ")
    for producto in list_inventario:
        print(f"\t\tprecio: ${producto.precio} codigo: {producto.codigo} nombre: {producto.nombre}")

def ver_inventario_ordenado(list_inventario_ordenada):
    print("\tInventario ordenado por precio: ")
    for producto in list_inventario_ordenada:
        print(f"\t\tprecio: ${producto.precio} codigo: {producto.codigo} nombre: {producto.nombre}")

def ver_lista_cliente(list_cliente):
    print("\tSu lista de compra es:")
    for producto in list_cliente:
        print(f"\t\tprecio: ${producto.precio} codigo: {producto.codigo} nombre: {producto.nombre}")

    print(f"\t\t Total: ${monto()} ")

def ver_lista_quejas(quejas):
	print("\tQuejas: ")
	for productodef in quejas:
		print(f"\t\t Producto defectuso: {productodef.nombredef}, codigo: {productodef.codigodef}, queja: {productodef.queja}")

def personal():
    while True:
        print("\t\t 1. Altas. \n\t\t 2. Bajas. \n\t\t 3. Cambios de puesto.\n\t\t 4. Ver lista de trabajadores.\n\t\t 5. Salir")
        opcionp = int(input("\t\tInserte la opción que desee: "))
        
        if opcionp == 1:
            altas(list_personal)
        elif opcionp == 2:
            op1 = int(input("\t\tDesea buscar al trabajador por 1. Nombre, 2. Código: "))
            
            if op1 == 1:
                bajas_nombre(list_personal)
            elif op1 == 2:
                bajas_codigo(list_personal)
            else:
                print("\t\tElija una opción correcta\n")
                
        elif opcionp == 3:
            op2 = int(input("\t\tDesea buscar al trabajador por 1. Nombre, 2. Código: "))
            
            if op2 == 1:
                cambios_nombre(list_personal)
            elif op2 == 2:
                cambios_codigo(list_personal)
            else:
                print("\t\tElija una opción correcta\n")	
                
        elif opcionp == 4:
            ver_lista_personal(list_personal)
       	elif opcionp == 5:
       		print("\t\tGracias\n")
       		break
        else:
            print("\t\tElija una opción correcta\n")

def altas(list_personal):
	nombreT = input("\t\tIngrese el nombre completo, empezando por apellido: ")
	codigoT = int(input("\t\tIngrese el codigo del trabajador: "))
	puesto = input("\t\tIngrese el puesto actual: ")
	trabajador = Trabajador(nombreT, codigoT, puesto)
	list_personal.append(trabajador)

def bajas_nombre(list_personal):
    nombreT = input("\t\tIngrese el nombre del trabajador: ")
    for trabajador in list_personal:
        if trabajador.nombreT == nombreT:
            list_personal.remove(trabajador)
            print("\t\tTrabajador dado de baja.\n")
            return
    print("\t\tEl trabajador no se encontró en la lista.\n")

def bajas_codigo(list_personal):
    codigoT = int(input("\t\tIngrese el nombre del trabajador: "))
    for trabajador in list_personal:
        if trabajador.codigoT == codigoT:
            list_personal.remove(trabajador)
            print("\t\tTrabajador dado de baja.\n")
            return
    print("\t\tEl trabajador no se encontró en la lista.\n")

def cambios_nombre(list_personal):
    nombreT = input("\t\tIngrese el nombre del trabajador: ")
    for trabajador in list_personal:
        if trabajador.nombreT == nombreT:
            trabajador.puesto = input("\t\tIngrese el nuevo puesto: ")
            print("\t\tPuesto cambiado correctamente.\n")
            return
    print("\t\tEl trabajador no se encontró en la lista.\n")

def cambios_codigo(list_personal):
    codigoT = int(input("\t\tIngrese el codigo del trabajador: "))
    for trabajador in list_personal:
        if trabajador.codigoT == codigoT:
            trabajador.puesto = input("\t\tIngrese el nuevo puesto: ")
            print("\t\tPuesto cambiado correctamente.\n")
            return
    print("\t\tEl trabajador no se encontró en la lista.\n")

def ver_lista_personal(list_personal):
	print("\t Personal: ")
	for trabajador in list_personal:
		print(f"\t\t Trabajador: {trabajador.nombreT}, codigo: {trabajador.codigoT}, puesto: {trabajador.puesto}")

while True:
    menu()
    opcion = int(input("\tInserte la opción que desee: "))

    if opcion == 1:
        inventario()
    elif opcion == 2:
    	clientes()
    elif opcion == 3:
    	personal()
    elif opcion == 4:
        print("\tGracias por su tiempo\n")
        break
    else:
        print("\tOpción inválida, seleccione una opción válida\n")

