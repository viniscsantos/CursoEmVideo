a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and a == c:
        tipo = 'EQUILÁTERO'
    elif a == b or a == c or b == c:
        tipo = 'ISÓCELES'
    else:
        tipo = 'ESCALENO'
    print('Os segmentos acima PODEM FORMAR um triângulo {}.'.format(tipo))
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triãngulo.')
