# os + shutil - Copiando arquivos com Python
# 1 - Vamos copiar arquivos de uma pasta para outras
# Copiar -> shutil.copy

import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'EXEMPLO')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')
print(DESKTOP)

os.makedirs(NOVA_PASTA, exist_ok=True) # ele cria o diretorio

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
           root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        print(caminho_novo_diretorio)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)



    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
           root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)