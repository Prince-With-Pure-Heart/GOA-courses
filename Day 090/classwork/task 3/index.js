const form = document.getElementById("form");
 
const dataBase = [];

form.addEventListener("submit", function(e){
    e.preventDefault();
    const password = form.password.value;
    for(let i = 0; i < password.length; i ++){
        if(password.charCodeAt(i) >= 33 && password.charCodeAt(i) <= 47){
            console.log("password contains a special character")
        }
    }

    
})
const age = 14
const num = 25
console.log(`My Age is ${age} + ${num} `)