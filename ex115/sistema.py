from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExist(arq):
    criarArq(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sitema'])
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArq(arq)
    elif resposta == 2:
        #Opção para cadastrar pessoas!
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastro(arq, nome, idade)
    elif resposta == 3:
        titulo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
