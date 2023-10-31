print("1.Sumar numeros\n2.Restar Numeros\n3.Multiplicacion\n4.Division\n5.Hallar un factorial\n6.Salir")
opciones=int(input("Elija una opcion del menu para continuar: "))

while opciones<=0 or opciones >6:
    print("No es una opcion valida por favor escoja una opcion valida")
    print("1.Sumar numeros\n2.Restar Numeros\n3.Multiplicacion\n4.Division\n5.Hallar un factorial\n6.Salir")
    opciones=int(input("Elija una opcion del menu para continuar: "))

if opciones==1:
    cantidad=int(input("Cuantos valores va a registrar?: "))
    resultado=0
    for i in range(1,cantidad+1):
        num=float(input(f"Ingrese la nota numero {i}: "))
        resultado+=num
    print(f"La Resultado de la suma es {resultado}")
    print("*******************************************")

if opciones==2:
    cantidad=int(input("Cuantos valores va a registrar?: "))
    resultado=float(input("Ingrese el primer valor: "))
    for i in range(2,cantidad+1):
        num=float(input(f"Ingrese el valor numero {i}: "))
        resultado = resultado - num
    print(f"La Resultado de la resta es {resultado}")
    print("*******************************************")

if opciones==3:
    cantidad=int(input("Cuantos valores va a registrar?: "))
    resultado=float(input("Ingrese el primer valor: "))
    for i in range(2,cantidad+1):
        num=float(input(f"Ingrese el valor numero {i}: "))
        resultado = resultado * num
    print(f"La resultado de la multiplicacion es {resultado}")
    print("*******************************************")

if opciones==4:
    divisor=float(input("Ingrese el divisor: "))
    dividendo = float(input("Ingrese el dividendo: "))
    resultado = divisor/dividendo
    print(f"El resultado de la division es {resultado}")
    print("*******************************************")

if opciones==5:
    numero=int(input("Ingrese el numero del que quiere saber el factorial: "))

    fac=1
    for i in range(1,numero+1,1):
        fac=fac * i
    print(fac)
    print("*******************************************")

if opciones==6:

    print("¡¡¡Hasta Pronto!!!")
    
    print("*******************************************")


        