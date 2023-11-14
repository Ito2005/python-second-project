from assets.biblioteca import *
from index_biblioteca import *

diretorio_usuarios = 'python-second-project\\assets\\usuario'

caminho_arquivo = os.path.join(diretorio_usuarios, 'contas.txt')

def criar_diretorio():
    if not os.path.exists(diretorio_usuarios):
        os.makedirs(diretorio_usuarios)

def escrita():
    criar_diretorio()

    caminho_arquivo = os.path.join(diretorio_usuarios, 'contas.txt')
    
    with open(caminho_arquivo, 'w') as contas:
        for linha in range(1, 101):
            contas.write(f"{linha}\n")

def leitura():
    with open(caminho_arquivo, 'r') as contas:
        for linha in contas.readlines():
            print(linha.strip())

