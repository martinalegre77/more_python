"""
Leer de un archivo .json y pasar su contenido a una estructura de python.
Luego crear un nuevo elemento y guardarlo en un archivo json
"""

import json

with open("persona.json") as f_in:
    persona = json.loads(f_in.read())

martin = {
    "nombre" : "martin",
    "edad" : 45,
    "hobbies" : [
        "escuchar musica",
        "programar",
        "leer"
    ],
    "hijos" : [
        "martina",
        "rodrigo"
    ]
}

with open("persona_yo.json", "w") as f_out:
    json.dump(martin, f_out)

