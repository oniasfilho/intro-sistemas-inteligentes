# 1) Dada duas listas, uma com a idade e outra com o peso das pessoas,
# faça uma função que retorne quantas pessoas com mais de 40 anos
# possuem peso superior à média dos pesos dessas pessoas.

class pessoa:
    def __init__(self, *peso, **idade):
        self.idade = idade
        self.peso = peso


def primeiro_exercicio(idades, pesos):
    lista_pessoas = []
    lista_pessoas_acima_40 = []
    lista_pesos_acima_40 = []
    peso_medio = 0
    individuos_acima_40_acima_media = 0
    tamanho_lista = 0;

    if len(idades) == len(pesos):
        tamanho_lista = len(idades)
    else:
        raise Exception("Ambas listas devem ter o mesmo tamanho")

    for x in range(0, tamanho_lista):
        nova_pessoa = pessoa()
        nova_pessoa.idade = idades[x]
        nova_pessoa.peso = pesos[x]
        lista_pessoas.append(nova_pessoa)

    for individuo in lista_pessoas:
        if individuo.idade > 40:
            lista_pessoas_acima_40.append(individuo)
            lista_pesos_acima_40.append(individuo.peso)

    peso_medio = sum(lista_pesos_acima_40) / len(lista_pessoas_acima_40)

    for individuo in lista_pessoas_acima_40:
        if individuo.peso > peso_medio:
            individuos_acima_40_acima_media += 1

    return individuos_acima_40_acima_media


lista_idade = [40, 45, 32, 49, 19, 60, 22, 25, 43, 49, 46]
lista_peso = [89, 91, 150, 95, 66, 140, 87, 90, 90, 65, 170]
print(primeiro_exercicio(lista_idade, lista_peso))
