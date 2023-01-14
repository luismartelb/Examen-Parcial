dato = true
acum=0
acum2=0
while(dato){
    var a = prompt("Ingrese el valor de a : ")
    var b = prompt("Ingrese el valor de b : ")
    op = a - b
    document.write("El resultado de la resta es:", op,"<br>")
    acum = acum + op
    acum2 = acum2 + 1
    var n = prompt("Desea realizar otra resta: si[1] o no [2] ")
    if (n = 2)
        dato = false
}
document.write("La cantidad de veces restadas son: ",acum2, "<br>")
document.write("La suma de los resultados obtenidos son: ", acum,"<br>")