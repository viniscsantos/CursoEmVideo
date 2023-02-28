def leiaDinheiro(msg):
    while True:
        val = str(input(msg)).replace(',', '.').strip()
        if val.isalpha() or val == '':
            print(f'\033[31mERRO: "{val}" é um preço invalido!\033[m')
        else:
            break
    return float(val)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor
