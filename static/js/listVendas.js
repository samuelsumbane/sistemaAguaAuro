$(document).ready(function () {
  var table = $('#tabelaVenda').DataTable({
    'processing': true,
    'serverSide': true,
    'ajax': {
      'url': '../src/selectVendas.php',
      "method": "POST"
    },
    'columns': [
      { data: "producto" },
      { data: "pesoliquido" },
      { data: "quantidade" },
      { data: "valorcusto" },
      { data: "valorunico" },
      { data: "valortotal" },
      { data: "desconto" },
      { data: "lucro" },
      { data: "mes" },
      { data: "ano" }
    ],
    "oLanguage": {
      "sProcessing": "Processando...",
      "sLengthMenu": "Mostrar _MENU_ registros",
      "sZeroRecords": "Não foram encontrados resultados",
      "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando de 0 até 0 de 0 registros",
      "sInfoFiltered": "",
      "sInfoPostFix": "",
      "sSearch": "Pesquisar:",
      "sUrl": "",
      "oPaginate": {
        "sFirst": "Primeiro",
        "sPrevious": "Anterior",
        "sNext": "Seguinte",
        "sLast": "Último"
      }
    }
  });

  const selectpros = ()=>{
    var action = "selectallrecordsP"; $.ajax({ url: "barAction.php", method: "POST", data: { action: action }, dataType: "json", success: function (data) { for (var i = 0; i < data.length; i++) { var proC = data[i]["codigo"]; var proN = data[i]["producto"]; var proP = data[i]["pesoliquido"]; var proF = `${proC} - ${proN} - ${proP}`; var selectData = [proF]; $("#sellProComboBox").select2({ data: selectData }); } }, error: function () { alert('Erro') } })
  }

  selectpros()
  $("#cancelPurchase").click(() => { $("#bg-modal").css("top", "-100%"); $(".trtable").remove(); $('.trtablefake').remove(); document.querySelector("#qtddpro").innerHTML = "";document.querySelector("#trocoText").textContent = ""; removeAllStoragecodes() }); $("#sellPageButton").click(() => { var bgModal = document.querySelector(".bg-modal"); bgModal.classList.remove("hideModal"); $("#bg-modal").css("top", "0"); $('#sellForm')[0].reset(); $("#action").val("sellProducts");sessionStorage.removeItem('activeCode') });
  
 
  $("#vRecebido").keyup(() => { var vTotalPro = $('#totalPedido').val(); if (vTotalPro == "") { alert("não tem total pago"); } else { var vRecebido = $('#vRecebido').val(); var trocoCalc = vRecebido - vTotalPro; document.querySelector('#trocoText').innerHTML = `${trocoCalc} MT` } });


  $("#bg-modal").on("submit", "#sellForm", function (e) {
    e.preventDefault()

    var action = $("#action").val()
    var usernamelogged = $("#usernamelogged").val()
    var trtable = document.querySelectorAll(".trtable")
    trtable.forEach(trsun => {
      var codetd = trsun.children[0].innerHTML
      var pronametd = trsun.children[1].innerHTML
      var pltd = trsun.children[2].innerHTML
      var vctd = trsun.children[3].innerHTML
      var vvtd = trsun.children[4].innerHTML
      var qtdtd = trsun.children[5].innerHTML
      var dctd = trsun.children[8].innerHTML
      var totalpro = trsun.children[9].innerHTML

      var trdata = `codetd=${codetd}&pronametd=${pronametd}&pltd=${pltd}&qtdtd=${qtdtd}&totaltd=${totalpro}&vctd=${vctd}&vvtd=${vvtd}&dctd=${dctd}&action=${action}&usernamelogged=${usernamelogged}`

      $.ajax({
        url: "barAction.php",
        method: "POST",
        data: trdata,
        success: function (data) {
          table.ajax.reload();
          $('#tabelaVendaUser').DataTable().ajax.reload()
          swal({
            title: "Venda feita com sucesso!",
            icon: "success",
            button: "Fechar",
          });
          $('#sellForm')[0].reset();
          $(".trtable").remove();
          $('.trtablefake').remove();
          $("#finishPurchase").attr('disabled', true)
          document.querySelector("#trocoText").textContent = ""

          sessionStorage.removeItem('activeCode')
         
        }, error: function () {
          alert('Houve um erro ao salvar os dados!')
        }
      })
  
      let codeList = sessionStorage.getItem('codeList')
      if(codeList){
        let codeListValue = codeList.split(',')
        let codeListLen = codeListValue.length

        if(codeListLen > 0){
          codeListValue.map((thisvalue) => {
            sessionStorage.removeItem(thisvalue)
          })
          sessionStorage.removeItem('codeList')
        }  
      }


    })
  })

  $("#checkDc").click(() =>{document.getElementById("dcInputDiv").classList.toggle("hideDcInputDiv");});$("#dcInput").keyup(()=>{calcDesconto()})


  var counterId = 0
  $("#addSellPro").click(() => {
    cleanSelectBox()
    addRecsTable()
  })

  $('#sellProTable').on('click', '.editProSellRec', function () {
    cleanSellFilds()
    var id = $(this).attr("id");
    var trtable = document.querySelector(`#trtable${id}`);
    var codeStock = trtable.children[0].innerHTML
    var pronametd = trtable.children[1].innerHTML
    var pltd = trtable.children[2].innerHTML
    var sellCombBox = document.querySelector("#sellProComboBox")
    var optiontext = `${pronametd} - ${pltd}`;
    let optionsf = Array.from(sellCombBox.options)
    var toselectf = optionsf.find(item => item.text = optiontext)
    toselectf.selected = true
    codeStock = trtable.children[0].innerHTML;
    sr = trtable.children[7].innerHTML;

    let lastproqtd = trtable.children[5].innerHTML
    if(sessionStorage.getItem(codeStock)){
      let proqtd = sessionStorage.getItem(codeStock)
      let newproqtd = proqtd - parseInt(lastproqtd)
      sessionStorage.setItem(codeStock, newproqtd)
    }

    $('#selectedCode').val(`${codeStock} ${sr}`)
    $("#proCode").val(trtable.children[0].innerHTML)
    $("#nameproinput").val(trtable.children[1].innerHTML)
    $("#plproinput").val(trtable.children[2].innerHTML)
    $("#srestante").val(trtable.children[7].innerHTML)
    $("#valorCustoSell").val(trtable.children[3].innerHTML)
    $("#valorvenda").val(trtable.children[4].innerHTML)
    $("#productQtd").val(trtable.children[5].innerHTML)
    $('#valorTotal').val(trtable.children[6].innerHTML)
    $("#dcInput").val(trtable.children[8].innerHTML)
    $("#afterDc").val(trtable.children[9].innerHTML)

    var recValue = trtable.children[9].innerHTML
    document.querySelector('#totalPedido').value -= recValue
    $(`#trtable${id}`).remove()
    $(`#trtablefake${id}`).remove()
    $("#addSellPro").removeAttr('disabled')
  })

  $('#sellProTable').on('click', '.delProSellRec', function () { var id = $(this).attr("id"); var trtable = document.querySelector(`#trtable${id}`); var recValue = trtable.children[6].textContent; document.querySelector('#totalPedido').value -= recValue; $(`#trtable${id}`).remove(); $(`#trtablefake${id}`).remove(); $('#vRecebido').val(""); document.querySelector('#trocoText').textContent = ''; 
  
  let codeStock = trtable.children[0].innerHTML

  let lastproqtd = trtable.children[5].innerHTML
  if(sessionStorage.getItem(codeStock)){
    let proqtd = sessionStorage.getItem(codeStock)
    let newproqtd = parseInt(proqtd) - parseInt(lastproqtd)
    sessionStorage.setItem(codeStock, newproqtd)
  } 
})

  var sellProComboBox = $("#sellProComboBox");
  sellProComboBox.change(() => {
    cleanSellFilds()
    var action = "productData"
    var selectedOp = $('#sellProComboBox').val()
    var codepro = selectedOp.split('-')[0]
    var namepro = selectedOp.split('-')[1]
    var plpro = selectedOp.split('-')[2]

 
    $("#selectedCode").val(codepro)

    var codeStock = $("#selectedCode").val()
    if(codeStock != ""){
      $.ajax({
        url: "barAction.php",
        method: "POST",
        data: { codeStock: codeStock, action: action },
        dataType: "json",
        success: function (data) {
          if(data[0]['stockrestante'] <= 0 ){
            swal({icon: "warning",title:"Sem productos",text: "Por favor, faz estoque desse producto."})

          }else{
            $('#nameproinput').val(namepro)
            $('#plproinput').val(plpro)
            // 
            $("#valorCustoSell").val(data[0]['valorcusto'])
            $("#valorvenda").val(data[0]['valorvenda'])
            $("#proCode").val(data[0]['codigo'])

            var srestante = document.querySelector('#srestante').value
            var codigodoproducto = data[0]['codigo']
            let stockrestante = parseInt(data[0]['stockrestante'])

            if(sessionStorage.getItem(codigodoproducto)){
              let provalue = sessionStorage.getItem(codigodoproducto)
              srestante = stockrestante - provalue
            }else{
              srestante = stockrestante - 0
            }

            $("#srestante").val(srestante)

            document.querySelector("#qtddpro").innerHTML = `Total de producto por unidade ${srestante}`

          }
         
          
        }, error: function () {
          alert("Houve um erro desconhecido!")
        }
      })
    }else{
      document.querySelector("#qtddpro").textContent = ""
    }
  });

  
});