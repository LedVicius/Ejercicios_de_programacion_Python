if __name__ == '__main__':
	print("Dada una compra, si su valor es mayor de 1000 Bs tendrá un descuento del 20% de lo contrario un descuento del 5%")
	print("Precio de la compra")
	compra = float(input())

if compra> 1000:
	Des= 0.8
	print ("Se aplica un 20% de descuento")  
	print ("Monto total:" , int(Des*compra))
else:
	Des2= 0.95
	print ("Se aplica un 5% de descuento")
	print ("Monto total:" , int(Des2*compra))

