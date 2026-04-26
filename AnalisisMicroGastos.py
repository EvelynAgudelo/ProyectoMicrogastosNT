import pandas as pd

print("MicroGastos: Ejercicio de Análisis de Datos")

#Creamos el DataFrame con los datos de gastos
data_gastos = {
    'Descripcion': ['Almuerzo', 'Transporte', 'Mercado', 'Cine', 'Gasolina'],
    'Fecha': ['2026-04-25', '2026-04-24', '2026-04-23', '2026-04-22', '2026-04-21'],
    'Valor': [2000, 18000, 25000, 8000, 30000]
}

# Crear DataFrame
df_gastos = pd.DataFrame(data_gastos)

print("\nDatos de gastos:")
print(df_gastos)

#Filtrar gastos mayores a 15000
gastos_altos = df_gastos[df_gastos['Valor'] > 15000]
print(f"\nGastos mayores a 15000:\n{gastos_altos}\n")

#Top 3 gastos más altos
Top3 = df_gastos.nlargest(3, "Valor")
print(f"Top 3 gastos más altos:\n{Top3}\n")

#Agrupar por fecha
gastos_fecha = df_gastos.groupby("Fecha")["Valor"].sum()
print(f"Total de gastos por fecha:\n{gastos_fecha}\n")

#Crear columna derivada
df_gastos["IVA"] = df_gastos["Valor"] * 0.19
print(f"Gastos con IVA incluido:\n{df_gastos}\n")

#Exportar a CSV
df_gastos.to_csv('gastos_microgastos.csv', index=False)
print("Archivo guardado como gastos_microgastos.csv")