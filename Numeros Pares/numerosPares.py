numeros =int (input("Hasta que numero quiere ver los numeros pares: "))


for i in range(0,numeros+1,1):
    if (i % 2 == 0) :
        print(i)
