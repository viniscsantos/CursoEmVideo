def aumentar(preço, taxa):
    res = float(preço + preço * (taxa/100))
    return res


def diminuir(preço, taxa):
    res = float(preço - preço * (taxa/100))
    return res


def dobro(preço):
    res = float(preço * 2)
    return res


def metade(preço):
    res = float(preço / 2)
    return res
