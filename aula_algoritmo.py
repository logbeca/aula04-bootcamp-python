lista_de_numeros: list = [40, 5, 60,70, 0 ,-599,1, 39]


def ordernar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()
    
    for i in range (len(nova_lista_de_numeros)):
        for j in range(i+1, len(nova_lista_de_numeros)):
             if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j],  nova_lista_de_numeros[i]
    return nova_lista_de_numeros

nova_lista = ordernar_lista_de_numeros(lista_de_numeros)
#print(nova_lista)