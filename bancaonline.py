saldo=0
while True:
  print(""" 1. Ingresar dinero
            2. Retirar dinero
            3. Consultar saldo
            4. Reiniciar cuenta
            5. Salir """)
  opcion = int(input("Introduce una opción:"))

  if opcion == 4 and saldo != 0:
    saldo = 0
    print ("Se ha reiniciado su cuenta. Su saldo actual es 0€")
      


