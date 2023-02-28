print('-=-' * 10)
print('Analizador de Triângulos')
print('-=-' * 10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
 print('Os segmentos acima PODEM FORMAR triângulo')
else:
 print('Os segmentos acima NÃO PODEM FORMAR triângulo')





