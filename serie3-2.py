import sys

def calcular_suma(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma

def calcular_promedio(valores):
    suma = calcular_suma(valores)
    promedio = suma / len(valores)
    return promedio

def main():
    if len(sys.argv) < 2:
        print("Por favor, ingrese valores separados por comas como argumentos de línea de comandos.")
        return

    valores_str = sys.argv[1].split(',')
    try:
        valores = [float(valor) for valor in valores_str]
    except ValueError:
        print("Error: Asegúrese de ingresar valores numéricos separados por comas.")
        return

    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)

    print(f"Valores ingresados: {valores}")
    print(f"Suma de los valores: {suma}")
    print(f"Promedio de los valores: {promedio}")

if __name__ == "__main__":
    main()
