from random import randint
from datetime import datetime

# letras = ('0', '1', '2', '3', '4', '5', '6', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',)

# senha = ''
# for a in range(5):
#     senha += str(letras[randint(2, 8)])
# print(senha)

dataEHoraAtual = datetime.now()


def retornarValidade(categoria='clientes'):
    mesAtualNr = dataEHoraAtual.strftime('%m')
    anoAtual = dataEHoraAtual.strftime('%Y')
    
    if categoria == 'clientes':
        quartomes = int(mesAtualNr) + 4
        if quartomes > 12:
            valAno = int(anoAtual) + 1
            valMes = quartomes - 12 
            if valMes < 10:
                valMes = f"0{quartomes - 12}"
        else:
            valMes = quartomes
            valAno = anoAtual
    
    validade = f"{dataEHoraAtual.strftime('%d')}.{valMes}.{valAno}"
    return validade


def retornarHora(value='HM'):
    if value == 'HM':
        hora = dataEHoraAtual.strftime('%H:%M')
    else:
        hora = dataEHoraAtual.strftime('%H:%M:%S')
        
    return hora


h = retornarHora('full')
print(h)
        


# va = retornarValidade()
# print(va)



