import subprocess

import json

import re

import argparse

from concurrent.futures import ThreadPoolExecutor, as_completed

from tqdm import tqdm



# Función para ejecutar nbtscan y guardar los resultados en un archivo de log

def run_nbtscan(ip):

    try:

        result = subprocess.run(['nbtscan', ip], capture_output=True, text=True, check=True)

        return result.stdout

    except subprocess.CalledProcessError as e:

        return f"Error scanning {ip}: {e}"

    except Exception as e:

        return f"Unexpected error scanning {ip}: {e}"



# Función para leer y procesar los resultados del escaneo

def parse_nbtscan_output(output):

    results = []

    for line in output.splitlines():

        if line.startswith('IP address'):

            continue  # Skip header line

        match = re.match(r'(\d+\.\d+\.\d+\.\d+)\s+(.+?)\s+<.+?>\s+(.+)', line)

        if match:

            ip, name, mac = match.groups()

            results.append({

                'IP Address': ip,

                'Name': name.strip(),

                'MAC Address': mac.strip()

            })

    return results



# Función principal

def main(network_range, log_file, json_file):

    network_prefix = ".".join(network_range.split('.')[:3])

    ips = [f"{network_prefix}.{i}" for i in range(1, 255)]  # Generar el rango de IP

    all_results = []



    with ThreadPoolExecutor(max_workers=10) as executor:

        future_to_ip = {executor.submit(run_nbtscan, ip): ip for ip in ips}

        for future in tqdm(as_completed(future_to_ip), total=len(ips)):

            result = future.result()

            all_results.extend(parse_nbtscan_output(result))

    

    with open(log_file, 'w') as f:

        for result in all_results:

            f.write(f"{result['IP Address']}\t{result['Name']}\t{result['MAC Address']}\n")



    with open(json_file, 'w') as f:

        json.dump(all_results, f, indent=4)



    print(f'Resultados guardados en {json_file}')



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Escanear una red con nbtscan y guardar los resultados en un log y JSON.')

    parser.add_argument('network_range', help='Rango de IP a escanear (e.g., 172.16.230.0/24)')

    parser.add_argument('--log', default='nbtscan_log.txt', help='Archivo de log para guardar los resultados')

    parser.add_argument('--json', default='nbtscan_results.json', help='Archivo JSON para guardar los resultados')

    args = parser.parse_args()

    main(args.network_range, args.log, args.json)

