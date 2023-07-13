# Leer un archivo csv y crear una lista de diccionarios.
# Luego crear un random de faltas de 1 y 15 para luego guardar la nueva lista
# en un nuevo archivo csv

import random

with open("alumnos.csv") as file_in:
    alumnos = []
    linea = file_in.readline()
    while linea != "":
        # alumnos.append([linea.replace("\n", "")])  
        alumnos.append(linea.replace("\n", "").split(","))
        linea = file_in.readline()

# new_alumnos = [alumno.append(random.randint(1, 15)) for alumno in alumnos]

[alumno.append(str(random.randint(1, 15))) for alumno in alumnos]

"""
new_alumnos = []

for alumno in alumnos:
    alumno.append(random.randint(1, 15))
    new_alumnos.append(alumno)
"""
# print(alumnos)

new_alumnos = [",".join(alumno) for alumno in alumnos]
print(new_alumnos)
new_alumnos = "\n".join(new_alumnos)
print(new_alumnos)

with open("new_alumnos.csv", "w") as file_out:
    file_out.write(new_alumnos)
