##Diseña un algoritmo en el que se ingrese 2 digitos para restarlos y el programa 
# los contabilice y los acumule usando el while.
acum = 0
acum2 = 0
dato = True
op = int()
while(dato):
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    op = a-b
    print("El resultado de la resta es: ", op)
    acum = acum + op
    acum2 = acum2 + 1
    n = str(input("Desea realizar otra resta: "))
    if n == 'si':
        dato = True
    else:
        dato = False
print("La cantidad de veces de restas realizadas son: ", acum2)
print("La suma de las restas realizadas son: ", acum)