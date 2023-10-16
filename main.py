#!/usr/bin/env python 

import argparse
import openpyxl

from administradorDatos import inicializar_datos,inicializar_hojas, mover_datos

df = inicializar_datos("pacientes.xlsx") # Sacamos la variable df de la funcion inicializar_datos
print(df)

# Argumentos del programa
parser = argparse.ArgumentParser(description='Mover datos entre hojas en el archivo de pacientes')
parser.add_argument('-e', '--excel-file', help='nombre del archivo Excel', required=True, type=str)
parser.add_argument('-i', '--id_paciente', help='ID del paciente para identificar la fila', required=True, type=str)
parser.add_argument('-o', '--origen', choices=['Pendientes', 'Terminados'], required=True, help='Hoja de origen')
parser.add_argument('-d', '--destino', choices=['Pendientes', 'Terminados'], required=True, help='Hoja de destino')
args = parser.parse_args()

# Inicializar las hojas
inicializar_hojas(args.excel_file)

# Llamar a la función para mover los datos
mover_datos(args.excel_file, args.id_paciente, args.origen, args.destino)