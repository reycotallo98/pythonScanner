import glob
import os

# Directorio donde se encuentran los archivos
directorio = '.'  # Puedes cambiar el directorio según sea necesario

# Patrón para buscar archivos
patron = 'open_ports_*.txt'

# Inicializar las cadenas para almacenar las IPs y los puertos
IP = ""
puertos = ""

# Buscar archivos con el patrón especificado
archivos = glob.glob(f"{directorio}/{patron}")

# Leer cada archivo y extraer la IP y los puertos
for archivo in archivos:
    # Extraer la IP del nombre del archivo
    puertos=""
    nombre_archivo = archivo.split('/')[-1]  # Obtener solo el nombre del archivo
    IP = nombre_archivo.split('_')[0]

    # Leer los puertos del archivo y agregarlos a la cadena de puertos
    with open(archivo, 'r') as file:
        for linea in file:
            puertos += linea.strip() + ','  # Agregar el puerto a la cadena de puertos

    # Eliminar la coma adicional al final de la cadena de puertos
    puertos = puertos.rstrip(',')

    # Imprimir las IPs y los puertos
    print("IP:", IP)
    print("Puertos:", puertos)
    comando="proxychains sudo nmap -vv -sVC -n -Pn -T1 -oA scaneoPuertos_"+IP+" -p"+puertos+" "+IP
    os.system(comando)
