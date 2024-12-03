from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo": "Game of Thrones",
    "Author": "Estagiario",
    "Ano": 2005
}

livro_02: Dict[str, Any] = {
    "Titulo": "cem anos de solidão",
    "Author": "Gabriel Garcia Marquez",
    "Ano": 1956
}

lista_de_elementos: list = livro.items()
for elemento in lista_de_elementos:
    print(elemento)


lista_de_livros = []
lista_de_livros.append(livro)
lista_de_livros.append(livro_02)

print(lista_de_livros)
lista_de_livros_usando_dict: Dict= {


"livro":{
    "Titulo": "Game of Thrones",
    "Author": "Estagiario",
    "Ano": 2005
},

"livro_02": {
    "Titulo": "cem anos de solidão",
    "Author": "Gabriel Garcia Marquez",
    "Ano": 1956
}

}

print(lista_de_livros_usando_dict["livro"]["Titulo"])
