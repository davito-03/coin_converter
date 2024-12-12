import requests

# Función para obtener el tipo de cambio
def obtener_tasa_moneda(base, destino):
    url = f"https://v6.exchangerate-api.com/v6/81350f238bb9c7b10e42af7f/latest/{base}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['conversion_rates'].get(destino)
    else:
        print("Error al obtener los datos")
        return None

# Función para convertir la cantidad de moneda
def convertir_moneda():
    base = input("Ingrese la moneda de origen (ej. USD): ").upper()
    destino = input("Ingrese la moneda de destino (ej. EUR): ").upper()
    cantidad = float(input("Ingrese la cantidad a convertir: "))

    tasa = obtener_tasa_moneda(base, destino)

    if tasa:
        resultado = cantidad * tasa
        print(f"{cantidad} {base} es igual a {resultado:.2f} {destino}")
    else:
        print("No se pudo realizar la conversión")

# Ejecutar el programa
if __name__ == "__main__":
    convertir_moneda()
