if __name__ == '__main__':
	print("Diseñar un algoritmo que lea un número de tres cifras y determine si es o no capicúa")
	n = int()
	a = int()
	b = int()
	print("Dame un número de tres digitos")
	n = int(input())
	a = int(n/100)
	b = n%10
	if a==b:
		print("El número ",n," es un número capicúa")
	else:
		print("El número ",n," no es un número capicúa")

