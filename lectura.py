from os import write
import re


log_file = r"logfiles.log"
numMaxLineas = 100
contador = 0

with open(log_file, 'r') as file:
    for line in file:
        if contador < numMaxLineas:
            contador+=1
            
            patron = r'(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)" (\d+)'

            resultado = re.match(patron, line)

            if resultado:
                metodo = resultado.group(5)                
                nombre_metodo = metodo.split()[0]
                print(str(contador) + "->" + nombre_metodo)
