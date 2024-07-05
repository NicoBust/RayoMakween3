var usuario=document.getElementById("usuario");
var contrasena=document.getElementById("contrasena");
var error=document.getElementById("error");
error.style.color="red";

function enviarFormulario(){
    console.log("formulario enviado");
    var mensajeError =[];
    if(usuario.value === null || usuario.value === ""){
        mensajeError.push("ingresa tu nombre");
    }
    if(contrasena.value === null || contrasena.value === ""){
        mensajeError.push("ingresa tu Contraseña");
    }
    error.innerHTML = mensajeError.join(", ");
    return false;
}