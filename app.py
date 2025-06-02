from dice import roll
import time

def lanzar_dados(amount, sides):
    resultados = []
    for i in range(amount):
        resultado = roll(f'd1{str(sides)}')
        resultados.append(resultado)
        print(f"Lanzamiento {i+1} número obtenido {resultado}")
        time.sleep(5)
    return resultados

lanzar_dados(amount=6, sides=6)

