import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL de la API
url = "http://localhost:8080/microgastosapp/v1/gastos/usuario/8"

# Consumir la API: Este muestra los datos recibidos desde la API
response = requests.get(url)
print("Código:", response.status_code)
print("Respuesta:", response.text)

# Convertir JSON: Transforma la respuesta de la API en una estructura que Python puede manipular
gastos = response.json()

# Lista para almacenar datos
datos = []

# Recorrer gastos
for gasto in gastos:
    datos.append({
        "descripcion": gasto["descripcion"],
        "fecha": gasto["fecha"],
        "valor": gasto["valor"]
    })

# Crear DataFrame
df = pd.DataFrame(datos)

# Mostrar datos
print(df)

# GRÁFICA 1 - Gastos por descripción
gastos_descripcion = df.groupby("descripcion")["valor"].sum()

gastos_descripcion.plot(kind="bar")

plt.title("Gastos por Descripción")
plt.xlabel("Descripción")
plt.ylabel("Valor")

plt.tight_layout()
plt.show()

# GRÁFICA 2 - Gastos por fecha
gastos_fecha = df.groupby("fecha")["valor"].sum()

gastos_fecha.plot(kind="line", marker="o")

plt.title("Gastos por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Valor")

plt.tight_layout()
plt.show()