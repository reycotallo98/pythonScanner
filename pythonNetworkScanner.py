import argparse
import socket
import concurrent.futures
from tqdm import tqdm

def scan_port(ip, port, open_ports):
    try:
        # Crear un objeto socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Configurar un tiempo de espera para la conexión
        sock.settimeout(0.1)  # Reducimos el tiempo de espera para un escaneo más rápido
        # Intentar conectar al puerto en la dirección IP
        result = sock.connect_ex((ip, port))
        # Si el puerto está abierto, agregarlo a la lista de puertos abiertos
        if result == 0:
            open_ports.append(port)
        # Cerrar el socket
        sock.close()
    except socket.error:
        pass

def scan_ports(ip, ports):
    open_ports = []
    # Escanear los puertos especificados para la dirección IP dada
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, ip, port, open_ports) for port in ports]
        # Mostrar una barra de progreso mientras se realizan los escaneos
        for _ in tqdm(concurrent.futures.as_completed(futures), total=len(ports), desc=f"Scanning {ip}"):
            pass
    return open_ports

def save_to_file(ip, open_ports):
    # Guardar los puertos abiertos en un archivo
    with open(f"open_ports_{ip}.txt", "w") as file:
        file.write("\n".join(map(str, open_ports)))

def main():
    # Argumentos de línea de comandos
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("file", help="File containing IP addresses")
    args = parser.parse_args()

    # Leer las direcciones IP del archivo
    with open(args.file, "r") as file:
        ips = file.read().splitlines()

    # Puertos a escanear
    ports = range(1, 65536)  # Escanea todos los puertos posibles

    # Escanear cada dirección IP en paralelo
    for ip in ips:
        open_ports = scan_ports(ip, ports)
        save_to_file(ip, open_ports)
if __name__ == "__main__":
    main()
