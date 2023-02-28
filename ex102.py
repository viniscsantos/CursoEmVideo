print('-' * 40)


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """

    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


# Programa principal
print(fatorial(5, False))
