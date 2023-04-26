if __name__ == '__main__':
	print("Diseñe un programa que lea el peso de un hombre en libras y nos devuelva el equivalente en Kg y g")
	print("Ingresar peso en libras")
	peso = float(input())
	multi = peso*0.45
	print("Peso total en kilos es:" , round(multi,2), "Kg")
	print("Peso total en gramos es:", round(multi*1000), "g")

