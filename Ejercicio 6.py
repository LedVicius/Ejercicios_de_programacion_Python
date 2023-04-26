
if __name__ == '__main__':
	print("Realice un algoritmo donde el usuario seleccione cualquiera de las cuatro operaciones b�sicas de la calculadora.")
	print(" Seleccione que operacion va a realizar")
	print("1. Sumar")
	print("2. Restar")
	print("3. Multiplicar")
	print("4. division")
	opc = float(input())
	print("Ingrese la primera cantidad")
	n1 = float(input())
	print("Ingrese la segunda cantidad")
	n2 = float(input())
	if opc==1:
		res = n1+n2
		print("El resultado es:", int(res))
	elif opc==2:
		res = n1-n2
		print("el resultado es:", int(res))
	elif opc==3:
		res = n1*n2
		print("El resultado es: ", int(res))
	elif opc==4:
		res = n1/n2
		print("El resultado es: ",res)
	else:
		print("Error de seleccion")

