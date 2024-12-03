from typing import Dict, Any

produto_o1: Dict [ str, [str]]

import json
produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list = []
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop()
produtos.remove(produto)
numeros = []
numeros.extend(range(0,5))
print(produtos)
print(numeros)


lista =  ["sapato", 39, 10.12 , True]

produto_01: Dict[str, Any] = {
    "nome": "Sapato" ,
    "quantidade":39,
    "preco" :10.12,
    "Disponibilidade": True,

}

carrinho: list = []
carrinho.append(produto_01)
print(carrinho)


carrinho_json = json.dumps(carrinho)
print(carrinho_json)