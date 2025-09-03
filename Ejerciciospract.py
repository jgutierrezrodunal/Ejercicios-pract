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

#Ejercicio 16

print("-- Ejercicio #16 --")

n = 1

for i in range(1,21):
    n *= i

print("Números del 1 al 20 multiplicados: ", n)


#Ejercicio 21

print("-- Ejercicio #21 -- \n Número menor y mayor de dos números")

num21A = float(input("Ingrese el primer numero: "))
num21B = float(input("Ingrese el segundo numero: "))

if(num21A < num21B):
    print("El número ", num21A , " es el numero menor \nEl número ", num21B , " es el numero mayor") 
else:
    print("El número ", num21B , " es el numero menor \nEl número ", num21A , " es el numero mayor")

#Ejercicio 26

print("-- Ejercicio #21 -- \n Número menor y mayor de tres números")

num21A = float(input("Ingrese el primer numero: "))
num21B = float(input("Ingrese el segundo numero: "))
num21C = float(input("Ingrese el tercer numero: "))

if(num21A < num21B and num21A < num21C):
    print("El número ", num21A , " es el numero menor") 

if(num21B < num21A and num21B < num21C):
    print("El número ", num21B , " es el numero menor")

if(num21C < num21A and num21C < num21B):
    print("El número ", num21C , " es el numero menor") 

if(num21A > num21B and num21A > num21C):
    print("El número ", num21A , " es el numero mayor") 

if(num21B > num21A and num21B > num21C):
    print("El número ", num21B , " es el numero mayor")

if(num21C > num21A and num21C > num21B):
    print("El número ", num21C , " es el numero mayor") 


#Ejercicio 27

print("-- Ejercicio #27 -- \n Temperatura Farenheit a Celsius \n (Ingrese 999 como valor de temperatura para finalizar el programa)")
tfar = 0
tcel = 0
tfar = float(input("Ingrese únicamente el número de la temperatura en escala Farenheit: "))
working = 1

while working == 1:
    match tfar:
        case 999:
            print("Finalizando ejercicio...")
            working = 0

        case _:
            tcel = (5 / 9) * (tfar - 32)
            print(tfar,"grados farenheit equivalen a ", tcel, "grados celsius")
            tfar = float(input("Ingrese la temperatura en escala Farenheit: "))
        
        
