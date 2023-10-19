from caixa import coletar_informacoes_caixa
from bin import coletar_informacoes_bin
from coletarinfo import coletar
from coordenada import bin_packing
from py3dbp import Packer, Bin, Item
import re

quantidade_caixas = int(input("Quantas caixas você gostaria de inserir? "))
caixas_info = coletar_informacoes_caixa(quantidade_caixas)  # Passe a quantidade de caixas como argumento
bin_info = coletar_informacoes_bin(caixas_info)  # Passe a quantidade de caixas como argumento
solution = bin_packing(bin_info, caixas_info)
for i, coordinates in enumerate(solution):
    x, y, z = coordinates
    print(f"Caixa {i + 1} - Coordenadas (x, y, z): ({x}, {y}, {z})")
