import time

def cronometro(tiempo_total):
    tiempo_inicial = time.time()  # Obtiene el tiempo inicial
    tiempo_transcurrido = 0

    while tiempo_transcurrido < tiempo_total:
        tiempo_transcurrido = time.time() - tiempo_inicial  # Calcula el tiempo transcurrido
        minutos, segundos = divmod(int(tiempo_transcurrido), 60)  # Divide el tiempo en minutos y segundos
        print(f"Tiempo transcurrido: {minutos:02d}:{segundos:02d}", end='\r')
        time.sleep(1)  # Espera 1 segundo

    print("\n¡Tiempo finalizado!")

if __name__ == "__main__":
    tiempo_total = int(input("Ingresa el tiempo en segundos: "))
    cronometro(tiempo_total)




