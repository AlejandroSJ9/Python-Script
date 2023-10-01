import pandas as pd
import openpyxl

# Cargar el JSON desde el archivo
json_file_path = 'data.json'  # Asegúrate de proporcionar la ruta correcta al archivo JSON
data = pd.read_json(json_file_path)

# Filtrar solo las actividades de tipo "Ride" (carrera en bicicleta)
filtered_data = data[data['type'] == 'Ride']

# Crear un archivo de Excel y escribir datos
workbook = openpyxl.Workbook()
sheet = workbook.active

# Encabezados
sheet.append(["Nombre de la actividad", "Distancia (metros)", "Tiempo (segundos)", "Velocidad promedio (m/s)"])

# Iterar sobre las actividades filtradas y escribir datos
for _, row in filtered_data.iterrows():
    activity_name = row.get("name", "N/A")
    distance = row.get("distance", 0)
    moving_time = row.get("moving_time", 0)
    average_speed = row.get("average_speed", 0)

    sheet.append([activity_name, distance, moving_time, average_speed])

# Guardar el archivo de Excel
workbook.save("actividades_strava.xlsx")
print("Datos guardados exitosamente en actividades_strava.xlsx")
