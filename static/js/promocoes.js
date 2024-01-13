$(document).ready(function () {


  function selectAllRecs(){
    var action = "selectallrecordsPromocoes"
    $.ajax({
        url: "barAction.php",
        method: "post",
        data: {action:action},
        dataType: "json",
        async:false,
        success: function(data){
          if($('#userLogged').val() == 1){
            data.forEach(i=>{
              document.querySelector('.tableContainer').innerHTML += "<div class='proprodiv' id=''><div class='stockprodivtitle'><h3>"+i.produto+"</h3><h3 style='margin-left:auto;'>"+i.pesoliquido+"</h3> </div><div class='proprodivMlables'><div><p>Número de garafas</p><p><strong>"+i.nprodutos+"</strong></p></div><div><p>Valor promocional</p><p><strong>"+i.vpromo+"</strong></p></div></div><div class='stockbuttonsdiv'><button  class='delPromo' id="+i.id+">Deletar</button></div></div>"
            })
          }else{
            data.forEach(i=>{
                document.querySelector('.tableContainer').innerHTML += "<div class='proprodiv' id=''><div class='stockprodivtitle'><h3>"+i.produto+"</h3><h3 style='margin-left:auto;'>"+i.pesoliquido+"</h3> </div><div class='proprodivMlables'><div><p>Número de garafas</p><p><strong>"+i.nprodutos+"</strong></p></div><div><p>Valor promocional</p><p><strong>"+i.vpromo+"</strong></p></div></div></div>"
            })
          }
        }
    })

  }

  selectAllRecs()

  var action = "selectallrecordsP"; $.ajax({ url: "barAction.php", method: "POST", data: { action: action }, dataType: "json", success: function (data) {
     for (var i = 0; i < data.length; i++) {
      var barcode = data[i]["barcode"];
      var proC = data[i]["codigo"];
      var proN = data[i]["producto"]; 
      var proP = data[i]["pesoliquido"]; 
      var proF = `${proN} - ${proP}`; 
      var selectData = `${proC} - ${proN} - ${proP} - ${barcode}`; 

      $("#sellProComboBox").append(`<option value="${selectData}">${selectData}</option>`)
      $("#sellProComboBox").select2(); 
    } 
  }, error: function () { alert('Erro') } }); 
  


  (function disableB(){var elemArry = ['sellProComboBox', 'nGarrafas', 'valorPromo'];elemArry.forEach(e=>{if($(`#${e}`).val() == ""){$('#submeter').attr('disabled', 'disabled');}else{$('#submeter').attr('disabled', false)}});setTimeout(disableB, 800)})();
  

  function toggleCB(){
    clearSearch = document.querySelector('#clearSearcCard')
    var list = clearSearch.classList
    list.toggle('showClearButton')
  }

  const searchValueInput = document.querySelector('#searchStock')
  searchValueInput.addEventListener('keyup', function(){
    var searchValue = $('#searchStock').val()
    if(searchValue != ""){
      var action = 'filterPromo';
      $.ajax({
        url: 'barAction.php',
        method: "POST",
        data: { searchValue: searchValue, action: action },
        dataType: "json",
        success:function(data){
          document.querySelector('.tableContainer').innerHTML = ""
          data.forEach(i=>{
            document.querySelector('.tableContainer').innerHTML += "<div class='proprodiv' id=''><div class='stockprodivtitle'><h3>"+i.produto+"</h3><h3 style='margin-left:auto;'>"+i.pesoliquido+"</h3> </div><div class='proprodivMlables'><div><p>Número de garafas</p><p><strong>"+i.nprodutos+"</strong></p></div><div><p>Valor promocional</p><p><strong>"+i.vpromo+"</strong></p></div></div><div class='stockbuttonsdiv'><button  class='delPromo' id="+i.id+">Deletar</button></div></div>"
            // console.log(i)
          })
        }, error: function(){
          alert('Houve um erro desconhecido')
        }
      })
      var clearSearch = document.querySelector('#clearSearcCard')
      clearSearch.classList.add('showClearButton')
    //   toggleCB()
    }else{
      document.querySelector('.tableContainer').innerHTML = "";
        selectAllRecs();
        toggleCB()
    } 
  })

  $('#clearSearcCard').click(()=>{
    document.querySelector('.tableContainer').innerHTML = "";
    $('#searchStock').val("");
    selectAllRecs()
    toggleCB()
  })

    $("#addProductB").click(() => {
      var bgModal = document.querySelector(".bg-modal");
      bgModal.classList.remove("hideModal");
      $("#bg-modal").css("top", "0");
      document.getElementById("modaltitle").innerHTML = "Aplicar Promoção";
      $('#clientform')[0].reset();
      $('#action').val("addpromo");
      $('#submeter').val('Submeter');
  
    });
  
    $("#fecharClientModal").click(() => { 
      $("#bg-modal").css("top", "-100%") 
      $('#clientform')[0].reset()
    });

    function returnSelectClasses(){
      var itemSelecionado = sellProComboBox.val()
      var itemOption = document.querySelector("#sellProComboBox");
      const options = Array.from(itemOption.options);
      const selectedOption = options.find(item => item.text === itemSelecionado)
      var classes = selectedOption.getAttribute("class");
      return classes;
    }


    var sellProComboBox = $("#sellProComboBox");
    sellProComboBox.change(()=>{
      var comboValue = $('#sellProComboBox').val();
      // var sCInput = returnSelectClasses()
      $('#proName').val(comboValue.split("-")[1]);
      $('#proCode').val(comboValue.split("-")[0]);
      $('#plPro').val(comboValue.split("-")[2]);
      $('#barcodeinput').val(comboValue.split("-")[3]);
      // var s = $("#barcodeinput").val()
      // console.log(s)
    })
  
    // var delPromoB = document.querySelectorAll(".delPromo");
    // delPromoB.forEach(e=>{
    //   e.addEventListener("click", ()=>{
    //     swal({
    //     title: "Tem certeza que deseja apagar a promoção?",
    //     text: "Essa acção não pode ser revertida!",
    //     icon: "warning",
    //     buttons: true,
    //     dangerMode: true,
    //     })
    //     .then((willDelete) => {
    //     if(willDelete) {
    //       var action = 'delPromo';
    //       var promoCode = e.getAttribute('id');
    //       $.ajax({
    //         url: "barAction.php",
    //         method: "POST",
    //         data:{promoCode:promoCode, action:action},
    //         success:function(){
    //           window.location = "promo.php"
    //         }
    //       });
    //     }
    //     });
    //   })
    // })

    $('.tableContainer').on('click', '.delPromo', function(){
      // alert('ops')
      swal({
        title: "Tem certeza que deseja apagar o stock?",
        text: "Essa acção não pode ser revertida!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
        })
        .then((willDelete) => {
        if (willDelete) {
          var action = 'delPromo';
          var promoCode = $(this).attr('id');
          // alert(promoCode)
          $.ajax({
            url: "barAction.php",
            method: "POST",
            data:{promoCode:promoCode, action:action},
            success:function(){
              window.location = "promo"
            }
          });
        }
      });
    
    })

    //
    $('#bg-modal').on('submit', '#clientform', function (event) {
      event.preventDefault();
      $('#submeter').attr('disabled', 'disabled');
      var formData = $(this).serialize();
      // console.log(formData)
      $.ajax({
        url: "barAction.php",
        method: "POST",
        data: formData,
        success: function (data) {
          $('#clientform')[0].reset();
          $("#bg-modal").css("top", "-100%");
          $('#submeter').attr('disabled', false);

          window.location = "promo"
          // console.table(data)
        },error: function(){
          alert("Houve um erro desconhecido")
        }
      })
    });
  
  
  });