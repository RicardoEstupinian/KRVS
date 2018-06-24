function habilitar(){
    var c1=document.getElementById("1");
    var c2=document.getElementById("2");
    var c3=document.getElementById("3");
    var c4=document.getElementById("4");
    var c5=document.getElementById("5");
    var c6=document.getElementById("6");
    var c7=document.getElementById("7");
    var c8=document.getElementById("8");

    var btn=document.getElementById("btnsimular");
    var btng=document.getElementById("btnguardar");

    if(c1.value!= "" && c2.value!= "" && c3.value!="" && c4.value!="" && c5.value!="" && c6.value!="" && c7.value!="" && c8.value!=""){
        btn.disabled=false;
    }else{
        btn.disabled=true;
    }

    if(btn.disabled==false){
        btng.disabled=false;
    }else{
        btng.disabled=true;
    }
}
function h(){
    var a=document.getElementById("btnsimular");
    a.disabled=false;
}



function mensaje(){
    alert('Se guardo Exitosamente');
}
