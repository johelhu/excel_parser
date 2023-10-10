import argparse
from sys import exit

parser = argparse.ArgumentParser()

parser.add_argument(
    '-e', '--excel-file',
    help='nombre del archivo Excel',
    required=True,
    type=str,
)

parser.add_argument(
    '-c', '--code',
    help='codigo del artefacto',
    required=True,
    type=str,
)


args = parser.parse_args()

if not '.xlsx' in args.excel_file:
    print("Mal formato")
    exit(1)

# Empieza el script

print(args.excel_file)
print(args.code)