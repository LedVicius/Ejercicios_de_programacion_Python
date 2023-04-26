if __name__ == '__main__':

	print("Diseñe un algoritmo que lea la cantidad de almunos de redes, arquitectura y programación y determine el porcentaje de alumnos de cada curso")
	print("Cantidad de alumnos de redes")
	var1 = float(input())
	print("Cantidad de alumnos de arquitectura")
	var2 = float(input())
	print("Cantidad de alumnos de programación")
	var3 = float(input())
	suma = var1+var2+var3
	print("Porcentaje de alumnos de redes: %", round(var1*100/suma))
	print("Porcentaje de alumnos de arquitectura: %", round(var2*100/suma))
	print("Porcentaje de alumnos de programación: %", round(var3*100/suma))
