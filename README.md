# Dolphin SmartCard

Proyecto de busqueda en archivos .xlsx

## Documentación del proyecto

-

## Instalar
A continuacion los comandos para actualizar el sistema e instalar las dependencias.
### Arch

```bash

sudo pacman -Sy # Actualiza la informacion del software disponible.
sudo pacman -S python-virtualenv

virtualenv venv
source ./venv/bin/activate

pip install -r requirements.txt

```

### Ubuntu

```bash

sudo apt update
sudo apt install python3-virtualenv

virtualenv venv
source ./venv/bin/activate

pip3 install -r requirements.txt

```

## Ejectuar codigo (Ubuntu y Arch)

El archivo **main.py** es un script que busca palabras clave en archivos **.xlsx** entonces nos enviara la ubicacion de donde se encuentran

```bash

source ./venv/bin/activate

python3 main.py

```

## Dependencias
- **apt update**, actualiza la informacion del software disponible
- **virtualenv venv**, crea un directorio llamado _venv_ que contiene un entorno python
- **source _./venv/bin/activate_**, esto activa el entorno para que sea utilizado en lugar del python 

## Requirements
- **pandas**: Biblioteca para análisis de datos
- **openpyxl**: Biblioteca que necesita pandas para abrir un excel
- **unidecode**: 
- **numpy**: 
- **argparse**: 
## TODO
- [x] Hacer un **README**
- [ ] Hacer script ejemplo
- [ ] Hacer excel ejemplo

## Troubleshooting (*Solución de problemas*)
-
## Colabaradores:
- [Johel Hidalgo](https://caroje.com/profile/johelhu/)
## Asesores:
- [Jeancarlo Hidalgo](https://caroje.com/profile/jeancahu/)