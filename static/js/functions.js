

function mesano(value, position="t"){
    var date = new Date()
    var mes = date.getMonth() + 1
    var ano = date.getFullYear()
    var meses = ["Janeiro", "Fevereiro","Marco", "Abril", "Maio","Junho", "Julho","Agosto", "Setembro","Outubro", "Novembro","Dezembro"]

    var returnMonth = ""
    position == "l" ? returnMonth = meses[mes -2] : position == 'n' ? returnMonth = meses[mes] : returnMonth = meses[mes -1]

    return (value === 'mes') ? returnMonth : (value === "ambos") ? `${returnMonth} ${ano}` : ano.toString()
}

function thisOrLastYear(){
    var thismonthandyear = mesano("ambos").split(" ")
    var thismonth = thismonthandyear[0]
    return thismonth === "Janeiro" ? `${"Dezembro"} ${thismonthandyear[1] - 1}` : thismonthandyear;
}


const returnDate = (retorno='f')=>{
    var now = new Date()
    var dia = ("0" + now.getDate()).slice(-2);
    var monthcurrent = now.getMonth() + 1
    var mes = ("0" + monthcurrent).slice(-2);
    var anocompleto = now.getFullYear();
    var fulldate = `${dia}.${mes}.${anocompleto}`

    return retorno == 'day' ? dia : retorno == 'month' ? mes : fulldate
}

const returnTime = (retorno='minfull')=>{
    var now = new Date()
    var hora = ("0" + now.getHours()).slice(-2)
    var minutos = ("0" + now.getMinutes()).slice(-2)
    var segundos = ("0" + now.getSeconds()).slice(-2)
    var hourmin = `${hora}:${minutos}`
    var fullTime = `${hora}:${minutos}:${segundos}`

    return retorno == 'hour' ? hora : retorno == 'minutes' ? minutos : retorno == 'full' ? fullTime : hourmin
}


const randomNum = (numLen=6) =>{
    var randomedValues = Array.from({length: numLen}, ()=> Math.floor(Math.random() * 9) + 1)
    var randomedNum = ""
    randomedValues.map((val) => {
        randomedNum += val
    })

    return randomedNum
}