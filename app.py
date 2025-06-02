from dice import roll
import time

def lanzar_dados(amount, sides):
    resultados = []
    for i in range(amount):
        resultado = roll(f'd1{str(sides)}')
        resultados.append(resultado)
        print(f"Resultado del lanzamiento {i+1}: {resultado}")
        time.sleep(5)
    return resultados

lanzar_dados(amount=5, sides=6)
