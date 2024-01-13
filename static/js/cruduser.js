$(document).ready(function(){
    var table = $('#tabela').DataTable({
        'processing': true,
        'serverSide': true,
        'serverMethod': 'post',
        'ajax': {
            'url':'../src/selectUser.php'
        },
        'columns': [
          { data: 'nome' },
          { data: 'user' },
          { data: 'senha' },
          { data: 'nivel' },
          { data: 'editar'},
          { data: 'deletar'}
        ], 
        "oLanguage": {
          "sProcessing":   "Processando...",
          "sLengthMenu":   "Mostrar _MENU_ registros",
          "sZeroRecords":  "Não foram encontrados resultados",
          "sInfo":         "Mostrando de _START_ até _END_ de _TOTAL_ registros",
          "sInfoEmpty":    "Mostrando de 0 até 0 de 0 registros",
          "sInfoFiltered": "",
          "sInfoPostFix":  "",
          "sSearch":       "Pesquisar:",
          "sUrl":          "",
          "oPaginate": {
              "sFirst":    "Primeiro",
              "sPrevious": "Anterior",
              "sNext":     "Seguinte",
              "sLast":     "Último"
          }
      }
    });

    (function disablebuttons(){
      var nomeuser = $("#nomeuser").val();
      var username = $("#username").val();
      var password = $("#password").val();
      var passlength = $("#password").val().length;
      var level = $("#nivelusuario").val();
      if(nomeuser == "" || username == "" || password == "" || level == ""){
          $('#submeter').attr('disabled', 'disabled');
      }else{
        // pass condition
        if(passlength < 6){
          $("#password").css("border", "2px solid red");
          document.getElementById('passerror').innerHTML = "A senha deve ter no mínimo 6 caracteres!";
        }else{
          $("#password").css("border", "none");
          document.getElementById("passerror").innerHTML = "";
          if(level == 0 || level == 1){
            $('#submeter').removeAttr('disabled');
          }else{
            $('#submeter').attr('disabled', 'disabled');
          }
        }
        // level condition
        if (level == 0 || level == 1){
          $("#nivelusuario").css("border", "none");
          document.getElementById("nivelerror").innerHTML = "";
          if (passlength >= 6){
            $('#submeter').removeAttr('disabled');  
          }else{
          $('#submeter').attr('disabled', 'disabled');
          }
        }else{
          $("#nivelusuario").css("border", "2px solid red");
          document.getElementById("nivelerror").innerHTML = "O níver deve ser 0 ou 1";
        }
      }
      setTimeout(disablebuttons, 750);
    })()

    $("#adduser").click(()=>{
      var bgModal = document.querySelector(".bg-modal");
      bgModal.classList.remove("hideModal");
        $("#bg-modal").css("top", "0");
        document.getElementById("modaltitle").innerHTML = "Adicionar usuário ";
        $("#userform")[0].reset();
        $('#action').val("addUser");
        $('#submeter').val('Salvar');
    })

    $("#fecharModal").click(()=>{$("#bg-modal").css("top", "-100%");})
    $("#tabela").on("click", ".editarButton", function(){
        var userid = $(this).attr("id");
        var action = 'getUser';
        $.ajax({
          url:'userAction.php',
          method:"POST",
          data:{userid:userid, action:action},
          dataType:"json",
          success:function(data){
            $("#bg-modal").css("top", "0");
            document.getElementById("modaltitle").innerHTML = "Editar usuário";
            $('#nomeuser').val(data.nome);
            $('#username').val(data.usuario);
            $('#password').val(data.senha);
            $('#nivelusuario').val(data.nivel);				
            $('#action').val('updateUser');
            $('#userid').val(data.id);
            $('#submeter').val('Actualizar');
  
          },
          error: function(){
            alert("erro")
          }
        })
    })

    $("#tabela").on('click', ".deleteButton", function(){
        swal({
          title: "Tem certeza?",
          text: "Essa acção não pode ser revertida!",
          icon: "warning",
          buttons: true,
          dangerMode: true,
          })
          .then((willDelete) => {
          if (willDelete) {
            var userid = $(this).attr("id");
            var action = 'delUser';
            $.ajax({
              url: "userAction.php",
              method: "POST",
              data:{userid:userid, action:action},
              success:function(){
                table.ajax.reload();
              }
            })
          }
          });
     });

     $('#bg-modal').on('submit', '#userform', function(event){
        event.preventDefault();
        $('#submeter').attr('disabled', 'disabled');
        var formData = $(this).serialize();
        $.ajax({
            url: "userAction.php",
            method: "POST",
            data: formData,
            success: function(data){
                $('#userform')[0].reset();
                $("#bg-modal").css("top", "-100%");
                $('#submeter').attr('disabled', false);
                table.ajax.reload();
            }
        })
      });
    

});