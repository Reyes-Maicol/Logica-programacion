import random

NumeroAle= random.randrange(1,100,1)

intentos=1

while intentos<=3:
    print(f"Intento Numero {intentos}")
    NumeroIntroducido = int(input("Ingrese un numero del 1 al 100: "))
    if NumeroIntroducido == NumeroAle:
        print (f"Felicidades has acertado en {intentos} intentos, eres un crack")
    elif NumeroIntroducido != NumeroAle:
        print ("Lo siento no haz acertado, pero sigues adelante")
        intentos+=1

if intentos>3:
    print("El numero aleatorio es ", NumeroAle)
        