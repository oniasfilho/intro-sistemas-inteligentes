# 1) Dada duas listas, uma com a idade e outra com o peso das pessoas,
# faça uma função que retorne quantas pessoas com mais de 40 anos
# possuem peso superior à média dos pesos dessas pessoas.
import random


def primeiro_exercicio(idades, pesos):
    lista_pessoas = []
    lista_pessoas_acima_40 = []
    lista_pesos_acima_40 = []
    peso_medio = 0
    individuos_acima_40_acima_media = 0
    tamanho_lista = 0;

    class pessoa:
        def __init__(self, *peso, **idade):
            self.idade = idade
            self.peso = peso

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
print("Primeiro exercicio: \n Quantidade de pessoas com mais de 40 anos que possuem peso superior à média dos pesos "
      "dessas pessoas -> ", primeiro_exercicio(lista_idade, lista_peso), "\n\n")


# 2) Faça uma função que receba dois parâmetros: linhas e colunas.
# A função deve desenhar uma moldura usando os caracteres '-', '|' e '*',
# como abaixo para 1 linha e 3 colunas.
# *---*
# |   |
# *---*
def segundo_exercicio(linhas, colunas):
    def cria_coluna(coluna):
        line = '+'
        for x in range(coluna):
            line += '-'
        line += '+'
        print(line)

    def cria_linha(linha, coluna):
        for y in range(coluna):
            column = '|'
            column += ' ' * linha
            column += '|'
            print(column)

    def desenha_moldura(linhas, colunas):
        cria_coluna(colunas)
        cria_linha(colunas, linhas)
        cria_coluna(colunas)
        print("\n\n")

    desenha_moldura(linhas, colunas)


print("Segundo exercicio:")
segundo_exercicio(1, 3)


# 3) Faça uma função que receba uma string como parâmetro e
# retorne quantas palavras há na string.
def terceiro_exercicio(string):
    return len(string.split())


print("Terceiro exercicio: \n Quantidade de palavras -> ", terceiro_exercicio("Good morning, my name is Onias, very "
                                                                              "nice to meet you"), "\n\n")


# 4) Crie um programa que gere 100 valores aleatórios entre
# 1 e 10. Mostre qual número que menos apareceu e qual o que
# mais apareceu, com suas respectivas frequências.
def quarto_exercicio():
    valores_randomicos = []
    for x in range(100):
        valores_randomicos.append(random.randint(1, 10))
    maior_frequencia = max(set(valores_randomicos), key=valores_randomicos.count)
    menor_frequencia = min(set(valores_randomicos), key=valores_randomicos.count)
    maior_frequencia_vezes = valores_randomicos.count(maior_frequencia)
    menor_frequencia_vezes = valores_randomicos.count(menor_frequencia)
    print("Quarto exercicio: \n Numeros aleatórios: ", valores_randomicos, "\n")
    print("Numero de maior frequencia: ", maior_frequencia, "| Frequencia: ", maior_frequencia_vezes, "\n")
    print("Numero de menor_frequencia: ", menor_frequencia, "| Frequencia: ", menor_frequencia_vezes, "\n")


quarto_exercicio()
