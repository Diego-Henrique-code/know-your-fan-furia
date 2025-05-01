import json
import os
import re
from datetime import datetime

def salvar_dados_usuario(nome, cpf, endereco, interesses, eventos, compras, data_nascimento, instagram=None, twitter=None, facebook=None, outros_links=None):
    if not os.path.exists("dados"):
        os.makedirs("dados")

    dados = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "interesses": interesses,
        "eventos": eventos,
        "compras": compras,
        "data_nascimento": str(data_nascimento),
        "instagram": instagram,
        "twitter": twitter,
        "facebook": facebook,
        "outros_links": outros_links,  
        "data_registro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    # Sanitização do nome e verificação de duplicatas
    base_nome = re.sub(r'[^\w\-_.]', '_', nome)[:50]
    nome_arquivo = f"{base_nome}.json"
    caminho_arquivo = os.path.join("dados", nome_arquivo)

    contador = 1
    while os.path.exists(caminho_arquivo):
        nome_arquivo = f"{base_nome}_{contador}.json"
        caminho_arquivo = os.path.join("dados", nome_arquivo)
        contador += 1

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    return caminho_arquivo
