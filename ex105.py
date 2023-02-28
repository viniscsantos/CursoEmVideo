def notas(*n, sit=False):
    """
    -> Função para analizar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional , indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    s = 0
    dados = {}
    for c, num in enumerate(n):
        s += num
        if c == 0:
            mai = num
            men = num
        else:
            if num > mai:
                mai = num
            if num < men:
                men = num
    dados['total'] = len(n)
    dados['maior'] = mai
    dados['menor'] = men
    dados['média'] = s / len(n)
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['média'] >= 5:
            dados['situação'] = 'RAZOAVEL'
        else:
            dados['situação'] = 'BOA'
    return dados


# Programa Principal
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
