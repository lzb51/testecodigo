from py3dbp import Packer, Bin, Item
import re
def bin_packing(bin, caixas):
    packer = Packer()
    packer.add_bin(Bin('large-box', bin["largura"], bin["altura"], bin["profundidade"], bin["peso"]))

    for i, caixa in enumerate(caixas):
        packer.add_item(Item(f'caixa {i}', caixa["largura"], caixa["altura"], caixa["profundidade"], caixa["peso"]))

    packer.pack()

    responses = []

    for b in packer.bins:
        for item in b.items:
            responses.append(item.string())

    for item in b.unfitted_items:
        print("====> ", item.string())

    # Extrair os valores de x, y e z para cada caixa
    coordenadas_caixas = []
    for response in responses:
        # Usar expressão regular para extrair as coordenadas
        match = re.search(r'pos\((.*?)\)', response)
        if match:
            coordenadas_caixa = match.group(1)
            coordenadas_caixa = re.findall(r'-?\d+', coordenadas_caixa)[:3]  # Extrair os três primeiros números inteiros
            coordenadas_caixa = [int(coord) if coord else 0 for coord in coordenadas_caixa]  # Substituir por 0 se não houver número
            coordenadas_caixa += [0] * (3 - len(coordenadas_caixa))  # Adicionar zeros para garantir três números
            coordenadas_caixas.append(coordenadas_caixa)

    return coordenadas_caixas