def voto(ano):
    from datetime import date
    data = date.today().year
    idade = data - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÒRIO.'


print('-' * 30)
nasc = int(input('Em que ano voçê nasceu? '))
print(voto(nasc))
