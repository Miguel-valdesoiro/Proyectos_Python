 Ejercicios Modulo 5. CSV (Enunciado)

 CSV

Ejercicio nº6:

import csv

# Ruta al archivo CSV
archivo_csv = "02_CSV_data.csv"

# Listas para almacenar los datos de cada columna
mpg_list = []
cylinders_list = []
displacement_list = []
horsepower_list = []
weight_list = []
acceleration_list = []
model_year_list = []
origin_list = []

# Leer y procesar el archivo CSV
with open(archivo_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera fila de encabezados
    
    for row in csv_reader:
        mpg_list.append(float(row[0]))
        cylinders_list.append(int(row[1]))
        displacement_list.append(float(row[2]))
        horsepower_list.append(float(row[3]))
        weight_list.append(float(row[4]))
        acceleration_list.append(float(row[5]))
        model_year_list.append(int(row[6]))
        origin_list.append(int(row[7]))

# Imprimir algunos datos para comprobar
print("mpg:", mpg_list[:10])
print("cylinders:", cylinders_list[:10])
print("displacement:", displacement_list[:10])
print("horsepower:", horsepower_list[:10])
print("weight:", weight_list[:10])
print("acceleration:", acceleration_list[:10])
print("model_year:", model_year_list[:10])
print("origin:", origin_list[:10])

Ejercicio nº7:

import csv

# Ruta al archivo CSV
archivo_csv = "02_CSV_data.csv"

# Listas para almacenar los datos de cada columna
mpg_list = []
cylinders_list = []
displacement_list = []
horsepower_list = []
weight_list = []
acceleration_list = []
model_year_list = []
origin_list = []

# Leer y procesar el archivo CSV
with open(archivo_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera fila de encabezados
    
    for row in csv_reader:
        mpg_list.append(row[0])
        cylinders_list.append(row[1])
        displacement_list.append(row[2])
        horsepower_list.append(row[3])
        weight_list.append(row[4])
        acceleration_list.append(row[5])
        model_year_list.append(row[6])
        origin_list.append(row[7])

# Eliminar el primer elemento de cada lista y convertir a float
mpg_list = list(map(float, mpg_list[1:]))
cylinders_list = list(map(float, cylinders_list[1:]))
displacement_list = list(map(float, displacement_list[1:]))
horsepower_list = list(map(float, horsepower_list[1:]))
weight_list = list(map(float, weight_list[1:]))
acceleration_list = list(map(float, acceleration_list[1:]))
model_year_list = list(map(float, model_year_list[1:]))
origin_list = list(map(float, origin_list[1:]))

# Imprimir algunos datos para comprobar
print("mpg:", mpg_list[:10])
print("cylinders:", cylinders_list[:10])
print("displacement:", displacement_list[:10])
print("horsepower:", horsepower_list[:10])
print("weight:", weight_list[:10])
print("acceleration:", acceleration_list[:10])
print("model_year:", model_year_list[:10])
print("origin:", origin_list[:10])

Ejercicio nº8:

import statistics as stats
# Completa el ejercicio aquíimport csv

import statistics as stats

# Ruta al archivo CSV
archivo_csv = "02_CSV_data.csv"

# Listas para almacenar los datos de cada columna
mpg_list = []
cylinders_list = []
displacement_list = []
horsepower_list = []
weight_list = []
acceleration_list = []
model_year_list = []
origin_list = []

# Leer y procesar el archivo CSV
with open(archivo_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Saltar la primera fila de encabezados
    
    for row in csv_reader:
        mpg_list.append(row[0])
        cylinders_list.append(row[1])
        displacement_list.append(row[2])
        horsepower_list.append(row[3])
        weight_list.append(row[4])
        acceleration_list.append(row[5])
        model_year_list.append(row[6])
        origin_list.append(row[7])

# Eliminar el primer elemento de cada lista y convertir a float
mpg_list = list(map(float, mpg_list[1:]))
cylinders_list = list(map(float, cylinders_list[1:]))
displacement_list = list(map(float, displacement_list[1:]))
horsepower_list = list(map(float, horsepower_list[1:]))
weight_list = list(map(float, weight_list[1:]))
acceleration_list = list(map(float, acceleration_list[1:]))
model_year_list = list(map(float, model_year_list[1:]))
origin_list = list(map(float, origin_list[1:]))

# Funciones para mostrar estadísticas
def mostrar_estadisticas(nombre, datos):
    print(f"Estadísticas para {nombre}:")
    print("Cantidad de observaciones:", len(datos))
    print("Mínimo:", min(datos))
    print("Máximo:", max(datos))
    print("Media:", stats.mean(datos))
    print("Mediana:", stats.median(datos))
    print("Desviación Estándar:", stats.stdev(datos))
    print()

# Mostrar estadísticas para cada lista
mostrar_estadisticas("mpg", mpg_list)
mostrar_estadisticas("cylinders", cylinders_list)
mostrar_estadisticas("displacement", displacement_list)
mostrar_estadisticas("horsepower", horsepower_list)
mostrar_estadisticas("weight", weight_list)
mostrar_estadisticas("acceleration", acceleration_list)
mostrar_estadisticas("model_year", model_year_list)
mostrar_estadisticas("origin", origin_list)


