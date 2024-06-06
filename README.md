# nbtscan-pro
nbtscan-pro puede escanear redes utilizando protocolo NetBIOS a través de TCP/IP (NetBT), tablas de nombres NetBIOS para el equipo local y equipos remotos, guarda los resultados en un ".log" y los procesa en formato "JSON". Este script es ideal para pentesters y administradores de redes que necesitan mapear y analizar redes de manera eficiente.

#Características

Escaneo de Redes: Utiliza nbtscan para escanear un rango de direcciones IP.

Paralelización: Escaneo paralelo de múltiples direcciones IP para mejorar la velocidad.

Registro y Exportación: Guarda los resultados del escaneo en un archivo de log y los exporta a JSON.

Interfaz de Usuario Mejorada: Admite argumentos de línea de comandos para personalizar el rango de red y los archivos de salida.

Barra de Progreso: Muestra una barra de progreso durante el escaneo.

#Requisitos
Python 3.6 o superior
nbtscan instalado (puedes instalarlo en Ubuntu con sudo apt-get install nbtscan)
Paquetes de Python: subprocess, json, re, argparse, concurrent.futures, tqdm

#Instalación
Clona el repositorio:

git clone https://github.com/espinozan/nbtscan-pro.git
cd nbtscan-pro

Instala las dependencias de Python:

pip install tqdm

#Uso
Ejecuta el script con el rango de IP que deseas escanear y especifica los archivos de salida para el log y los resultados en JSON.

#Comando Básico

python3 nbtscan_pro.py 192.168.1.0/24

#Con Opciones de Línea de Comandos

python3 nbtscan_pro.py 192.168.1.0/24 --log my_log.txt --json my_results.json

#Argumentos
network_range: Rango de IP a escanear (e.g., 192.168.1.0/24).
--log: Archivo de log para guardar los resultados (por defecto nbtscan_log.txt).
--json: Archivo JSON para guardar los resultados (por defecto nbtscan_results.json).

#Ejemplo de Salida

[
    {
        "IP Address": "192.168.1.82",
        "Name": "PC-OBJETIVO",
        "MAC Address": "00:11:22:33:44:55"
    },
    {
        "IP Address": "192.168.1.69",
        "Name": "PC-SITO",
        "MAC Address": "66:77:88:99:AA:BB"
    }
]

#Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus mejoras y sugerencias.

Licencia
Este proyecto está licenciado bajo la MIT License.



