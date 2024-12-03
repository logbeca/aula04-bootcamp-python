#idade: int = 30
#altura: float = 1.54
#nome: str = "Alice"
#is_estudante: bool = True

nome_valido: bool  = False
salario_valido: bool  = False
bonus_valido: bool  = False

while nome_valido is  False:
    try:
        nome_user: float = input("Digite seu nome:")

        if nome_user.isdigit():
            print("você digitou seu nome errado")
        elif nome_user.isspace():
            print("você digitou só espaço")

        elif len(nome_user)==0 :
            print("você não digitou nada ")
        else: 
            nome_valido = True
            print("ok")

    except ValueError as e:
        print(e)
    