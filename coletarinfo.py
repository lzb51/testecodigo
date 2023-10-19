from py3dbp import Packer, Bin, Item
import re
def coletar():
    # Coletar informações sobre as caixas
    num_caixas = int(input("Quantas caixas você deseja empacotar? "))
    caixas_info = coletar_informacoes_caixa(num_caixas)

    #TO-DO add validation on parameters

    # Coletar informações sobre o recipiente (bin) e calcular o peso do bin
    bin_info = coletar_informacoes_bin(caixas_info)
    return (caixas_info, bin_info)