def binario(n):
	if n > 0:
		return binario(n // 2) + str(n % 2)
	else:
		return ''

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [1, 0]
    else:
        fibo = fibonacci(n - 1)
        fibo.append(fibo[-1] + fibo[-2])
        return fibo

def menu():
	print("Bienvenido, puede realizar las siguientes operaciones")
	print("1)Conversion de bases, 2)Serie de Fibonacci, 3)salir")
	opcion = int(input("Inserte la opcion: "))
	return opcion


option = menu()
if option==1:
	numero = int(input("Ingrese un número natural: "))
	binario = binario(numero)
	print(f"El número binario es: {binario}")

elif option==2:
	N = int(input("Ingrese un número entero: "))
	fibonacci_inv = fibonacci(N)
	print("La serie es: ")
	for term in fibonacci_inv[::-1]:
    		print(term, end=" ")

elif option==3:
	print("Gracias")
