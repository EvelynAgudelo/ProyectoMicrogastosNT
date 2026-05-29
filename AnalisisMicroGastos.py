import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL de la API
url = "http://localhost:8080/microgastosapp/v1/gastos/usuario/3"

# Consumir la API
response = requests.get(url)

# Convertir JSON
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

# GRÁFICA 2 - Distribución porcentual de gastos por descripción
gastos_descripcion.plot(kind="pie", autopct="%1.1f%%")

plt.title("Distribución de Gastos")
plt.ylabel("")

plt.show()

# GRÁFICA 3 - Gastos por fecha
gastos_fecha = df.groupby("fecha")["valor"].sum()

gastos_fecha.plot(kind="line", marker="o")

plt.title("Gastos por Fecha")
plt.xlabel("Fecha")
plt.ylabel("Valor")

plt.tight_layout()
plt.show()