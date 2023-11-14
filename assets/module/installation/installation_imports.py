from assets.biblioteca import *

# Lista de pacotes a serem instalados
packages_to_install = ["numpy", "pandas", "PyMySQL"]

# Instalação dos pacotes
for package in packages_to_install:
    subprocess.run(["pip", "install", package])
