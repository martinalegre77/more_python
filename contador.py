"""
Contador - cuenta regresiva

1.- Lógica que me dé la hora actual 
"""

from datetime import datetime
from time import sleep

Path = "cuenta.txt"

def cero_adelante(num):
    if num < 10:
        return f"0{num}"
    else:
        return f"{num}"
        

f_actual = datetime.now()
f_fin = datetime.strptime("23:00:00", "%H:%M:%S" )

while f_fin <= f_actual:
    diferencia = f_fin-f_actual

    # print(diferencia.seconds) 

    horas = diferencia.seconds // 3600
    minutos = (diferencia.seconds // 60) % 60
    segundos = diferencia.seconds % 60

    #print(f"{cero_adelante(horas)}:{cero_adelante(minutos)}:{cero_adelante(segundos)}")
    diff_str = f"{cero_adelante(horas)}:{cero_adelante(minutos)}:{cero_adelante(segundos)}"

    with open(Path, "w") as f:
        f.write(diff_str)
        
    sleep(1)
    f_actual = datetime.now()






