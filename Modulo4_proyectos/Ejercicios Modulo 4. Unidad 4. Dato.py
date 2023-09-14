 Ejercicios Modulo 4. Unidad 4. Datos temporales (Soluciones)

1) Dadas las dos siguientes fechas, que corresponden a las fechas de nacimiento de dos hermanos (en la zona horaria de Europe/Madrid), indica cual es la diferencia entre ellos en días, horas, minutos y segundos:

from datetime import datetime
import pytz

hijo1 = datetime(1985, 10, 20, 17, 55)
hijo2 = datetime(1992, 6, 25, 18, 30)
# Completa el ejercicio aquí

# Define la zona horaria de Europe/Madrid
tz = pytz.timezone('Europe/Madrid')

# Asigna la zona horaria a las fechas
hijo1 = tz.localize(hijo1)
hijo2 = tz.localize(hijo2)

# Calcula la diferencia entre las fechas
diferencia = hijo2 - hijo1

# Extrae los componentes de la diferencia
dias = diferencia.days
segundos_totales = diferencia.seconds
horas = segundos_totales // 3600
minutos = (segundos_totales % 3600) // 60
segundos = segundos_totales % 60

# Imprime la diferencia en días, horas, minutos y segundos
print(f"Diferencia: {dias} días, {horas} horas, {minutos} minutos, {segundos} segundos")

2) Crea una función que se llame formato_fecha() que reciba por parámetro una fecha del tipo datetime y nos devuelva el siguiente formato: "20 de Abril del 2020".

En muchas ocasiones nuestros sistemas estan configurados de forma predeterminada en inglés, y no se puede cambiar la localidad a español. Por lo tanto, tenemos que aprender a seleccionar y mostrar los meses en español a pesar de que nuestro sistema se encuentre en inglés o en otro idioma. Crear una tupla para almacenar el listado de meses en español para poder seleccionar el nombre del mes adecuado en función a una fecha que le proporcionemos al programa. Queda prohibído utilizar metodos como locale, setlocale o strftime.

Prueba la función enviándole una fecha predefinida por ti y la fecha actual (now)

from datetime import datetime

def formato_fecha(fecha):
    meses_espanol = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )
    
    dia = fecha.day
    mes = meses_espanol[fecha.month - 1]
    año = fecha.year
    
    fecha_formateada = f"{dia} de {mes} del {año}"
    return fecha_formateada

# Prueba con fechas predefinidas
fecha_predefinida = datetime(2020, 4, 20)
fecha_actual = datetime.now()

print("Fecha predefinida formateada:", formato_fecha(fecha_predefinida))
print("Fecha actual formateada:", formato_fecha(fecha_actual))

3) Utilizando strftime y formatea la fecha actual para que salga con el siguiente formato (sin los puntos):
* Día: 20
* Mes: 04
* Año: 2020
* Hora: 16
* Minutos: 19
* Segundos (y milisegundos): 08.879057

from datetime import datetime

fecha_actual = datetime.now()

formato_dia = fecha_actual.strftime("Día: %d")
formato_mes = fecha_actual.strftime("Mes: %m")
formato_año = fecha_actual.strftime("Año: %Y")
formato_hora = fecha_actual.strftime("Hora: %H")
formato_minutos = fecha_actual.strftime("Minutos: %M")
formato_segundos_milisegundos = fecha_actual.strftime("Segundos (y milisegundos): %S.%f")

print(formato_dia)
print(formato_mes)
print(formato_año)
print(formato_hora)
print(formato_minutos)
print(formato_segundos_milisegundos)
