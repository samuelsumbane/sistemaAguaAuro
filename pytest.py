from random import randint
from datetime import datetime

# letras = ('0', '1', '2', '3', '4', '5', '6', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)

# senha = ''
# for a in range(5):
#     senha += str(letras[randint(2, 8)])
# print(senha)

dataEHoraAtual = datetime.now()


def retornarHora(value='HM'):
    if value == 'HM':
        hora = dataEHoraAtual.strftime('%H:%M')
    else:
        hora = dataEHoraAtual.strftime('%H:%M:%S')        
    return hora


s = dataEHoraAtual.strftime('%d%m%H%M%S')
print(s)




# va = retornarValidade()
# print(va)



