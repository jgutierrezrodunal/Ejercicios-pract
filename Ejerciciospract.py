# Juan Alberto Gutiérrez Rodríguez
#Primera versión

#1. Estructuras de control
#if, for, while, switch, dowhile

#Prueba


Nota = float(input("Ingrese la calificación de forma numérica entre 0 a 5: "))

if(Nota >= 4.5 ):
    print("Esta nota es meritoria")
else:
    print("Esta nota no es meritoria")

# -----------------> EJERCICIOS <-----------------

#Ejercicio 15

print("-- Ejercicio #15 --\n Cuadrado de los primeros 30 números naturales")

for i in range (1,31):
    print (i,"² = ", i ** 2)
    i + 1


