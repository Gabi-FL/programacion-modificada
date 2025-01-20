from programa import Luz
import time

if __name__ == "__main__":
    contador = 0
    semaforo = Luz()
    while contador < 6:
        print(semaforo.cambia_color())
        contador += 1
        time.sleep(2)
        print(semaforo.cambia_color())
        contador += 1
        time.sleep(2)
        print(semaforo.cambia_color())
        contador += 1
        time.sleep(2)
