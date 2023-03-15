sum : int = 0
bandera : bool = True
while bandera or num != 0:
  bandera = False
  num = int(input("Ingrese un entero o  0 para salir: "))
  sum += num
  print("La suma de los numeros ingresados es " + str(sum))
print("Ciclo terminado")