from datetime import datetime
dataEHoraAtual = datetime.now()


def mesvalidade(mesAtualNr, anoAtual, qtd):
    mesA = int(mesAtualNr) + qtd
    if(mesA > 12):
        valAno = int(anoAtual) + 1
        valMes = mesA - 12
        if valMes < 10:
            valMes = f"0{valMes}"
    else:            
        valMes = mesA
        valAno = anoAtual
        
    return f"{dataEHoraAtual.strftime('%d')}.{valMes}.{valAno}"
    
        
def retornarValidade(categoria='clientes'):
    mesAtualNr = dataEHoraAtual.strftime('%m')
    anoAtual = dataEHoraAtual.strftime('%Y')
    
    if categoria == 'clientes':
        validade = mesvalidade(mesAtualNr,anoAtual, 4)        
    elif categoria == 'infinity':
        validade = '-'
    elif categoria == 'loginlogout':
        validade = mesvalidade(mesAtualNr,anoAtual, 2)        
                 
    return validade

def retornarHora(value='HM'):
    if value == 'HM':
        hora = dataEHoraAtual.strftime('%H:%M')
    else:
        hora = dataEHoraAtual.strftime('%H:%M:%S')
        
    return hora

