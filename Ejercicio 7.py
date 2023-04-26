if __name__ == '__main__':
	print("Diseñar un algoritmo que dado el tipo de un cliente y el monto a pagar, diga de cuanto es el descuento :1) Cliente VIP descuento 35% 2) Cliente regular descuento 25% 3) Cliente esporádico descuento 10% 4) Cliente nuevo no tiene descuento.")
	print("Seleccione el tipo de cliente")
	print("1. Cliente VIP (descuento del 35%)")
	print("2. Cliente regular (descuento del 25%)")
	print("3. Cliente esporádico (descuento del 10%)")
	print("4. Cliente nuevo no tiene descuento")

	opc = float(input())
	print("Ingrese el monto")
	n1 = float(input())

	if opc==1:
		res = n1*0.65
		print("Cliente VIP (descuento del 35%)")
		print("Monto total a pagar:", int(res))
	elif opc==2:
		res = n1*0.75
		print("Cliente regular (descuento del 25%)")
		print("Monto total a pagar:", int(res))
	elif opc==3:
		res = n1*0.90
		print("Cliente esporádico (descuento del 10%)")
		print("Monto total a pagar: ", int(res))
	elif opc==4:
		print("Cliente nuevo no tiene descuento")
		print("Monto total a pagar: ", int(n1))
	else:
		print("Dato inválido")

