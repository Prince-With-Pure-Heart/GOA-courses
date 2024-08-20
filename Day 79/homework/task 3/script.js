let signUp = document.getElementById("form");
let userName = document.getElementById("username");
let userEmail = document.getElementById("email");
let userPassword = document.getElementById("password");
const btn = document.getElementById("submit")
const cleanUp = document.getElementById("clear");
function Clear(){
    if(userName != "" || userEmail != "" || userPassword != ""){
        userName.textContent = ""
        userEmail.textContent = ""
        userPassword.textContent = ""
    }



}


cleanUp.onclick = Clear;