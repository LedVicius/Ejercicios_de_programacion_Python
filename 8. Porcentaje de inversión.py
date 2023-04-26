if __name__ == '__main__':

	print("3 personas desean invertir su dinero para formar una empresa, cada una de ellas invierte una cantidad distinta. Hacer un algoritmo que imprima un porcentaje que cada quien invierte con respecto al total de la inversi�n")
	print("Inversión número 1")
	var1 = float(input())
	print("Inversión número 2")
	var2 = float(input())
	print("Inversión número 3")
	var3 = float(input())
	suma = var1+var2+var3
	print("Total de la inversión:", round(suma))
	print("Porcentaje del primer inversor:" , round(var1*100/suma) ,"%")
	print("Porcentaje del segundo inversor:" , round(var2*100/suma) ,"%")
	print("Porcentaje del tercer inversor:" , round(var3*100/suma) ,"%")

