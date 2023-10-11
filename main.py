import argparse
import openpyxl

parser = argparse.ArgumentParser()

parser.add_argument(
    '-e', '--excel-file',
    help='nombre del archivo Excel',
    required=True,
    type=str,
)

parser.add_argument(
    '-c', '--code',
    help='ID, apellido o nombre del paciente a buscar',
    required=True,
    type=str,
)

args = parser.parse_args()

if not args.excel_file.endswith('.xlsx'):
    print("Formato de archivo no válido. Se esperaba un archivo con extensión .xlsx")
    exit(1)

print("Archivo Excel:", args.excel_file)
print("Código, apellido o nombre del paciente a buscar:", args.code)

workbook = openpyxl.load_workbook(args.excel_file)
sheet = workbook.active

def buscar_paciente(codigo):
    for row in sheet.iter_rows(min_row=2):
        print("Leyendo fila:", [cell.value for cell in row])
        if len(row) >= 3 and (
                (row[0].value and str(row[0].value).lower() == str(codigo)) or
                (row[1].value and str(row[1].value).lower() == str(codigo)) or
                (row[2].value and str(row[2].value) == str(codigo))):
            return row

    return None

print(buscar_paciente(args.code))
resultado = buscar_paciente(args.code)


if resultado:
    nombre_paciente = resultado[0].value
    apellido_paciente = resultado[1].value
    print('Paciente encontrado - Nombre:', nombre_paciente, ', Apellido:', apellido_paciente, ', ID:', args.code)
else:
    print('Paciente no encontrado.')
