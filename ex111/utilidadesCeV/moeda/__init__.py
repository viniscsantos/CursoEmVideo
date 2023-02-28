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


def resumo(preço, aumento, redução):
    """
    -> Função para mostrar resumo de cálculo
    :param preço: valor inicial
    :param aumento: taxa de aumento
    :param redução: taxa de desconto
    :return: sem retorno
    """
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{redução}% de redução: \t{diminuir(preço, redução, True)}')
    print('-' * 30)