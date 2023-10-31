
FinalSerie = int(input("Hasta qué número quiere que la serie de Fibonacci llegue: "))

numero1 = 0
numero2 = 1

while numero1 <= FinalSerie:
    print(numero1)
    numero1, numero2 = numero2, numero1 + numero2
