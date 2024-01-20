
function faturaNaoEncontrada(){
    swal({
        icon: "warning",
        title: "A fatura anterior não foi encontrada.",
        text: "O campo de leitura anterior será liberado para inserir a leitura anterior."
    })
}

function lAnteriorMaior(){
    swal({
        icon: "error",
        title: "A leitura anterior não deve ser maior que a leitura atual",
        text: "Verifique os valores e preencha novamente."
    })
}

function definicoesAcao(acao='salvas'){
    swal({
        icon: "success",
        title: `Definições ${acao} com sucesso`,
    })
}

function campoNaoPreenchido(){
    swal({
        icon: "error",
        title: 'O campo de leitura atual não está preenchido',
        text: 'Por favor, preencha o campo'
    })
};

function camposNaoPreenchidos(){
    swal({
        icon: "error",
        title: 'Há campos não preenchidos',
        text: 'Por favor, preencha todos os campos'
    })
};

function lAnteriorNEncontrada(){
    swal({
        icon: "error",
        title: 'Leitura anterior não encontrada',
        text: 'Por favor, seleciona em cliente para obter a leitura anterior'
    })
}

function clientSemReciboOuPagas(){
    swal({
        icon: "info",
        title: 'Sem faturas a pagar',
        text: 'Este cliente não tem faturas não pagas'
    })
}

function faturaDoMesJaCriada(){
    swal({
        icon: "error",
        title: 'Fatura do mês corrente encontrada',
        text: 'Pode criar duas faturas do mesmo mês.'
    })
}

function valorAserPagoMaior(){
    swal({
        icon: "error",
        title: 'O valor é maior',
        text: 'O valor a ser pago não deve ser maior que o valor que deve ser pago.'
    })  
}

function pagamentoFeitoComSucesso(){
    swal({
        icon: "success",
        title: 'O pagamento foi feito com sucesso!',
    })    
}

function faturaNaoPodeSerEditada(){
    swal({
        icon: "info",
        title: 'Está fatura não pode ser edita.',
        text: 'Pois já se efetou o pagamento da mesma.'
    })    
}

function criadoComSucesso(objecto, genero='o'){
    swal({
        icon: "success",
        title: `${objecto} criad${genero} com sucesso!`,
    })    
}

function userCadastradoComSucesso(senha){
    swal({
        icon: "success",
        title: 'Usuário adicionado com sucesso!',
        text: `A senha inicial é ${senha}`
    })    
}

function faturaEditadaComSucesso(){
    swal({
        icon: "info",
        title: 'Fatura atualizada com sucesso!',
    })    
}

function atividadeNaoEncontrada(){
    swal({
        icon: "warning",
        title: 'Atividade não encontrada',
        text: `Não houve atividade nas datas seleciondas`
    })    
}