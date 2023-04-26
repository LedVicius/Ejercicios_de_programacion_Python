
if __name__ == '__main__': 
	print("Dado dos valores para sumar y multiplicar, verifique que el primer valor sea un número positivo")
	print("Ingrese dos números para sumar y multiplicar")
	num1 = float(input())
	num2 = float(input())
	if num1>0:
		suma = num1+num2
		multi = num1*num2
	else:
		print("Acción no válida")
		print("Recuerde que el primer valor debe ser un número positivo para que haga los calculos")
	print("El resultado de la suma es: ",int(suma))
	print("El resultado de la multiplicación es: ",int(multi))

