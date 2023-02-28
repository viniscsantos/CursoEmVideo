pessoas = {'nome': 'Vinis', 'sexo': 'masculino', 'idade': 32}
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas.items():
    #print(k)

#pessoas['peso'] = 88.5
#del pessoas['sexo']



#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[1]['uf'])

#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#from operator import itemgetter
#ranking = sorted(j.items(), key=itemgetter(1), reverse=True)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
      print(v, end='  ')
    print()


