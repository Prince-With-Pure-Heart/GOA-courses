const myForm = document.getElementById("Form");
const BTN = document.getElementById("btn");
 
 

const dataBase = [];

function validateForm() {
    const emailValue = form.elements.email.value;
    const passValue = form.elements.password.value;
    const userName = form.elements.userName.value;

    if(emailValue == '' || passValue == '' ) {
        alert('Please fill in all fields');
        return;
    };

    const acc = {
        email: emailValue,
        password: passValue,
        userName: userName
    };

    dataBase.push(acc);

    console.log(dataBase)

}


BTN.onclick = validateForm;

 