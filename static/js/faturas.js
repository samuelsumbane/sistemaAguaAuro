$('document').ready(function() {
    $("#tabela").on('click', ".printButton", function(){
        let fatid = $(this).attr('id')
    
        $.ajax({
            type: 'GET',
            url: '{% url "selecionarUmaFaturaPorId"  %}',
            data: {id:fatid},
            dataType:"json",
            success: function (response){
                let fatdata = response['data']
                document.querySelector('#docnomecliente').textContent = fatdata['fat_nome']
                document.querySelector('#docbairro').textContent = fatdata['fat_bairro']
                document.querySelector('#docleituraatual').textContent = fatdata['leituraatual']
                document.querySelector('#docquantidade').textContent = fatdata['consumofaturado']
                document.querySelector('#docvalorfaturado').textContent = fatdata['valordafatura']
                document.querySelector('#docmulta').textContent = fatdata['']
                document.querySelector('#docmes').textContent = fatdata['fat_mes']
                document.querySelector('#docano').textContent = fatdata['fat_ano']
                document.querySelector('#docleituraanterior').textContent = parseInt(fatdata['leituraatual']) - parseInt(fatdata['consumofaturado'])
                document.querySelector('#faturaDoc').style.display = 'block'
                printContent('faturaDoc')
                document.querySelector('#faturaDoc').style.display = 'none'
            }, error: function(response){
                console.log('Erro: ', response)
            }
        })
    })
    
});


