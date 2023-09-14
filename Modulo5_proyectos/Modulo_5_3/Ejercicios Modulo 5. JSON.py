 Ejercicios Modulo 5. JSON

 JSON (JavaScript Object Notation)

1) A continuación se muestra un JSON String

import json

# El JSON string proporcionado
json_string = '''
{
  "jefe_proyecto": {
    "Nombre": "Juan",
    "Edad": 28,
    "Experiencia": ["Gestion", "Finanzas", "Bases de datos"],
    "Residencia": "Madrid",
    "HorasProyecto": 3500
  },
  "empleados": [
    {
      "Nombre": "Elena",
      "Edad": 26,
      "Experiencia": ["JavaScript", "Python"],
      "Residencia": "Madrid",
      "HorasProyecto": 500
    },
    {
      "Nombre": "Luis",
      "Edad": 31,
      "Experiencia": ["Django", "Flask", "Pyramid"],
      "Residencia": "Barcelona",
      "HorasProyecto": 1100
    }
  ]
}
'''

# Cargamos el JSON string en un diccionario
data_dict = json.loads(json_string)

# Comprobamos el tipo y mostramos por pantalla
print("Tipo de la estructura:", type(data_dict))
print("Estructura completa:", data_dict)

# Extraemos las horas del jefe y los empleados
horas_jefe = data_dict["jefe_proyecto"]["HorasProyecto"]
horas_empleados = sum(empleado["HorasProyecto"] for empleado in data_dict["empleados"])

# Mostramos las horas del jefe y de los empleados
print("Horas del jefe:", horas_jefe)
print("Horas de los empleados:", horas_empleados)

# Calculamos y mostramos la suma total de horas
suma_total_horas = horas_jefe + horas_empleados
print("Suma total de horas:", suma_total_horas)

2) En el ejercicio anterior has trabajado con un diccionario que tu mismo/a creaste, conviértelo a un formato JSON String, muestra su tipo y los datos por pantalla
¿Para qué nos sirve este formato?

import json

# Diccionario creado a partir del JSON string
data_dict = {
    "jefe_proyecto": {
        "Nombre": "Juan",
        "Edad": 28,
        "Experiencia": ["Gestion", "Finanzas", "Bases de datos"],
        "Residencia": "Madrid",
        "HorasProyecto": 3500
    },
    "empleados": [
        {
            "Nombre": "Elena",
            "Edad": 26,
            "Experiencia": ["JavaScript", "Python"],
            "Residencia": "Madrid",
            "HorasProyecto": 500
        },
        {
            "Nombre": "Luis",
            "Edad": 31,
            "Experiencia": ["Django", "Flask", "Pyramid"],
            "Residencia": "Barcelona",
            "HorasProyecto": 1100
        }
    ]
}

# Convertimos el diccionario a formato JSON String
json_string = json.dumps(data_dict, indent=2)

# Mostramos el tipo y el JSON String por pantalla
print("Tipo de la estructura:", type(json_string))
print("JSON String:", json_string)

3) A veces os encontraréis con JSON que tendréis que modificar. Para ello tenéis que decodificarlos, realizar las modificaciones pertinentes y volver a codificarlo para dejarlo como JSON de nuevo. En el siguiente ejemplo os habéis dado cuenta de que hay algunos errores:
* A Superman le falta como poder "Volar"
* En Batman, la edad es 35, no 350
* En Batman, le sobra el poder de "Rayos en los ojos"
* En Wonder Woman le falta el poder "Lazo de la verdad"
* Después de corregir todo esto, transforma estos datos en un JSON String

# NO TOCAR NADA DE ESTE BLOQUE
superheroes = {
	"nombreEquipo": "Super Hero Squad",
	"ciudad": "Metro City",
	"formado": 2016,
	"baseSecreta": "Super Tower",
	"activo": "Si",
	"miembros": [
		{
			"nombre": "SuperMan",
			"edad": 29,
			"identidadSecreta": "Clart Kent",
			"poderes": [
				"Super fuerza",
				"Super velocidad",
				"Rayos en los ojos"
			]
		},
		{
			"nombre": "Batman",
			"edad": 350,
			"identidadSecreta": "Bruce Wayne",
			"poderes": [
				"Detective",
				"Dinero",
				"Rayos en los ojos"
			]
		},
		{
			"nombre": "Wonder Woman",
			"edad": 900,
			"identidadSecreta": "Diana de Temiscira",
			"poderes": [
				"Super fuerza",
				"Super velocidad"
			]
		}
	]
}


import json

# Diccionario de superhéroes corregido
superheroes = {
    "nombreEquipo": "Super Hero Squad",
    "ciudad": "Metro City",
    "formado": 2016,
    "baseSecreta": "Super Tower",
    "activo": "Si",
    "miembros": [
        {
            "nombre": "SuperMan",
            "edad": 29,
            "identidadSecreta": "Clark Kent",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Volar"  # Agregado el poder "Volar"
            ]
        },
        {
            "nombre": "Batman",
            "edad": 35,  # Corregida la edad de Batman
            "identidadSecreta": "Bruce Wayne",
            "poderes": [
                "Detective",
                "Dinero"
            ]
        },
        {
            "nombre": "Wonder Woman",
            "edad": 900,
            "identidadSecreta": "Diana de Temiscira",
            "poderes": [
                "Super fuerza",
                "Super velocidad",
                "Lazo de la verdad"  # Agregado el poder "Lazo de la verdad"
            ]
        }
    ]
}

# Convertimos el diccionario corregido a formato JSON String
json_string = json.dumps(superheroes, indent=2)

# Mostramos el JSON String por pantalla
print(json_string)

4) En base al ejercicio anterior, modifica la estructura de super para lograr que miembros tenga dos ramas: "miembrosActivos" y "miembrosInactivos", donde cada una de estas ramas, almacenen los héroes que están en activo y los que no. En este caso, introduce a SuperMan y Wonder Woman en la lista de activos y a Batman en la de Inactivos. Esta modificación puedes hacerla como quieras, o bien programando las estructuras de datos e ir componiéndolo o bien cogiendo el JSON y modificándolo sobre él mismo. Al finalizar puedes comprobar tu JSON en un visualizador online (http://jsonviewer.stack.hu/)

import json

# Diccionario de superhéroes con las modificaciones solicitadas
superheroes = {
    "nombreEquipo": "Super Hero Squad",
    "ciudad": "Metro City",
    "formado": 2016,
    "baseSecreta": "Super Tower",
    "activo": "Si",
    "miembros": {
        "miembrosActivos": [
            {
                "nombre": "SuperMan",
                "edad": 29,
                "identidadSecreta": "Clark Kent",
                "poderes": [
                    "Super fuerza",
                    "Super velocidad",
                    "Volar"
                ]
            },
            {
                "nombre": "Wonder Woman",
                "edad": 900,
                "identidadSecreta": "Diana de Temiscira",
                "poderes": [
                    "Super fuerza",
                    "Super velocidad",
                    "Lazo de la verdad"
                ]
            }
        ],
        "miembrosInactivos": [
            {
                "nombre": "Batman",
                "edad": 35,
                "identidadSecreta": "Bruce Wayne",
                "poderes": [
                    "Detective",
                    "Dinero"
                ]
            }
        ]
    }
}

# Convertimos el diccionario modificado a formato JSON String
json_string = json.dumps(superheroes, indent=2)

# Mostramos el JSON String por pantalla
print(json_string)


5) En el siguiente código, accedemos a un JSON de forma remota, a partir de la respuesta, realizar lo siguiente:
* Mostrar el tipo de dato que se ha recibido
* Mostrar los datos recibidos
* Mostrar el número de personas que se encuentran actualmente en el espacio
* Realizar un bucle que recorra a todas esas personas y muestre nombre y nave en la que se encuentra.

import requests

# API que nos comunica cuantas personas se encuentran actualmente en el espacio
response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

# Mostrar el tipo de dato recibido
print("Tipo de dato recibido:", type(data))

# Mostrar los datos recibidos
print("Datos recibidos:", data)

# Mostrar el número de personas en el espacio
number_of_people = data["number"]
print("Número de personas en el espacio:", number_of_people)

# Recorremos las personas y mostramos nombre y nave
for person in data["people"]:
    print("Nombre:", person["name"])
    print("Nave:", person["craft"])
    print("-" * 20)

