if __name__ == '__main__':

	print("un vendedor tiene un sueldo base de 6.000bs, recibe una comision del 10% del total de ventas del mes, cuanto ganaría en un mes que obtuvo 3 ventas")
	print("Precio de la Primera venta")
	venta1 = float(input())

	print("Precio de la Segunda venta")
	venta2 = float(input())

	print("Precio de la Tercera venta")
	venta3 = float(input())
	
	suma = venta1+venta2+venta3
	comi = suma*0.10
	Salario = 6000

print ("Salario mensual más la comision:", int(comi+Salario) ,"Bs")
