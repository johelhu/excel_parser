import argparse
import openpyxl

from administradorDatos import inicializar_datos 

#parser = argparse.ArgumentParser()

#parser.add_argument(
 #   '-e', '--excel-file',
  #  help='nombre del archivo Excel',
   # required=True,
    #type=str,
#)

#parser.add_argument(
 #   '-c', '--code',
  #  help='ID, apellido o nombre del paciente a buscar',
   # required=True,
    #type=str,
#)

#args = parser.parse_args()

df = inicializar_datos("pacientes.xlsx") # Sacamos la variable df de la funcion inicializar_datos
print(df)