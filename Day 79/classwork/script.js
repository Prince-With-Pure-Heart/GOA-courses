//let input1 = Number(prompt());
//let input2 = Number(prompt());
//console.log(input1 + input2);
// console.log(input1 * input2);
// console.log(input1 / input2);
// console.log(input1 - input2);


let userInfo = document.getElementById("info");

function validateForm() {
    const emailValue = info.elements.email.value;
    const passValue = info.elements.password.value;
    const userValue = info.elements.userName.value;
    if(emailValue == "" || passValue == ""){
        alert("Please fill alm of the blanks");
        return;
    }
    console.log('Form submitted successfully');
    console.log("Email: " + emailValue);
    console.log("Password: " + passValue);
    console.log("username: " + userValue)

};
document.getElementById("btn").onclick = validateForm();