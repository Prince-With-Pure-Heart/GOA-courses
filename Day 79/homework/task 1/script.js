const btn = document.getElementById("btn");
const form = document.getElementById("Form");

function validForm(){
   const emailVal = form.elements.email.value;
   const passWordVal = form.elements.password.value;
   const userNameVal = form.elements.userName.value;

   if(emailVal === "" || passWordVal === "" || userNameVal === ""){
    alert("All of teh field are required");
    return;

   }
   else{
    console.log("Signed up succesfuly");
   };
};

btn.onclick = validForm;