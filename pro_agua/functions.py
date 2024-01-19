from datetime import datetime
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
        
    elif categoria == 'infinity':
        validade = '-'
         
    return validade

def retornarHora(value='HM'):
    if value == 'HM':
        hora = dataEHoraAtual.strftime('%H:%M')
    else:
        hora = dataEHoraAtual.strftime('%H:%M:%S')
        
    return hora

