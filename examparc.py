acum = 0
acum2 = 0
op = int()

n = int(input("Cuantas veces desea restar: "))
for i in range(1,n+1,1):
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    op = a-b
    print("El resultado de la resta es: ", op)
    acum = acum + op
    acum2 = acum2 + 1 
print("La cantidad de veces de restas realizadas son: ", acum2)
print("La suma de las restas realizadas son: ", acum)