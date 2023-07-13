# ARCHIVOS DE ANCHO FIJO

# Id_persona  |  tipo  |  Fecha y hora

# 00010e10MAY2019071530


def fixed_width_parser(datos):
    # print("{0:05d}".format(datos[0]))
    # print(datos[1])
    # print("".join(datos[2].split("/")))
    # print("".join(datos[3].split(":")))
    lista = [
        "{0:05d}".format(datos[0]),
        datos[1],
        "".join(datos[2].split("/")),
        "".join(datos[3].split(":"))
    ]
    # print(lista)
    lista_str = "".join(lista)
    return lista_str

def fixed_width_reader(datos_in):
    lista = [
        int(datos_in[0:5]),
        datos_in[5:6],
        "/".join([datos_in[6:8], datos_in[8:11], datos_in[11:15]]),
        ":".join([datos_in[15:17], datos_in[17:19], datos_in[19:21]])
    ]
    print(lista)

datos = [10, "e", "10/MAY/2019", "07:15:30"]

datos_str = fixed_width_parser(datos)

with open("registro.txt", "w") as output_file:
    output_file.write(datos_str)

with open("registro.txt", "r") as input_file:
    datos_in = input_file.read()

print(datos_in)

fixed_width_reader(datos_in)
