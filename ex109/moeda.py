def moeda(preço=0, moeda='R$'):
    """
    -> Função que acrecenta cifrão ao preço
    :param preço: para ler o preço
    :param moeda: insere o cifrão caso 'True'
    :return: 'True' preço formatado 'False' sem formato
    """
    return f'{moeda}{preço:>.2f}'. replace('.', ',')


def aumentar(preço=0, taxa=0, cifr=False):
    """
    -> Funação para acrecentar procentagem
    :param preço: valor inicial
    :param taxa: porcentagem a ser aumentada
    :param cifr: 'True' com cifrão  'False' sem cifrão
    :return: valor final
    """
    res = preço + preço * (taxa / 100)
    return res if not cifr else moeda(res)


def diminuir(preço=0, taxa=0, cifr=False):
    """
    -> Função para diminuir porcentagem
    :param preço: valor inicial
    :param taxa: porcentagem a ser descontada
    :param cifr: 'True' com cifrão  'False' sem cifrão
    :return: valor final
    """
    res = preço - preço * (taxa/100)
    return res if not cifr else moeda(res)



def dobro(preço=0, cifr=False):
    """
    -> Função para dobrar o valor
    :param preço: valor inicial
    :param cifr: 'True' com cifrão  'False' sem cifrão
    :return: valor final
    """
    res = preço * 2
    return res if not cifr else moeda(res)


def metade(preço=0, cifr=False):
    """
    -> Função para mostrar metade do preço
    :param preço: valor inicial
    :param cifr: 'True' com cifrão  'False' sem cifrão
    :return: valor final
    """
    res = (preço / 2)
    return res if not cifr else moeda(res)


