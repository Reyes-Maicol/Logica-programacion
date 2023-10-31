import random

minusculas="abcdefghijklmnñopqrstuvwxyz"
mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros="0123456789"
simbolos="._-*@#//&%"

uso=minusculas +mayusculas + numeros + simbolos

longitud=int(input("Ingrese la longitud de la contraseña: "))

contraseña="".join(random.sample(uso,longitud))

print(contraseña)
