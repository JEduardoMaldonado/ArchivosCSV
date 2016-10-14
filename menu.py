# coding utf-8
import csv
import sys

print "----------------MENU---------------"
print "1. INSERTAR"
print "2. LEER"
print "3. SALIR"

opcion=int(input("Elige una opcion "))

if opcion == 1:
    nombre = raw_input("Ingresa Nombre: ")
    email = raw_input("Ingresa Email: ")
    with open ('data.csv','a') as file:
        dat = csv.writer(file, delimiter=",")
        dat.writerow([''+str(nombre), ''+(email)])

if opcion == 2:
    with open ('data.csv', 'r') as file:
        data = csv.reader(file, delimiter=',')
        for line in data:
            print line

if opcion == 3:
    sys.exit(0)    




