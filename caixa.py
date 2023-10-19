from py3dbp import Packer, Bin, Item
import re
def coletar_informacoes_caixa(numero_caixas):
    informacoes_caixas = []

    for i in range(numero_caixas):
        print(f"\nCaixa {i+1}:")
        altura = input("Qual é a altura da caixa em centímetros? ").replace(',', '.')
        largura = input("Qual é a largura da caixa em centímetros? ").replace(',', '.')
        profundidade = input("Qual é a profundidade da caixa em centímetros? ").replace(',', '.')
        peso = input("Qual é o peso da caixa em quilogramas? ").replace(',', '.')

        print("\nEm uma escala de 1 a 5, o quão frágil é a caixa?")
        while True:
            fragilidade = input("Digite um número de 1 a 5 (sendo 1 menos frágil e 5 mais frágil): ").replace(',', '.')
            try:
                fragilidade = float(fragilidade)
                if 1 <= fragilidade <= 5:
                    break
                else:
                    print("Valor inválido! Digite um número entre 1 e 5.")
            except ValueError:
                print("Valor inválido! Digite um número válido.")

        informacoes_caixa = {
            "altura": float(altura),
            "largura": float(largura),
            "profundidade": float(profundidade),
            "peso": float(peso),
            "fragilidade": fragilidade
        }

        informacoes_caixas.append(informacoes_caixa)

    return informacoes_caixas
