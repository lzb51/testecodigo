from py3dbp import Packer, Bin, Item

import re
def coletar_informacoes_bin(caixas):
    bin = {}
    altura = input("Qual é a altura do local que vai colocar as caixas, em centímetros? ").replace(',', '.')
    largura = input("Qual é a largura do local que vai colocar as caixas, em centímetros? ").replace(',', '.')
    profundidade = input("Qual é a profundidade do local que vai colocar as caixas, em centímetros? ").replace(',', '.')

    try:
        altura = float(altura)
        largura = float(largura)
        profundidade = float(profundidade)
    except ValueError:
        print("Valores inválidos! Certifique-se de digitar números válidos.")
        return None

    # Calcular o peso do bin como 10 vezes o peso da caixa mais pesada
    peso_caixa_mais_pesada = max(caixas, key=lambda x: x["peso"])["peso"]
    peso_bin = peso_caixa_mais_pesada * 10

    bin["altura"] = altura
    bin["largura"] = largura
    bin["profundidade"] = profundidade
    bin["peso"] = peso_bin

    return bin