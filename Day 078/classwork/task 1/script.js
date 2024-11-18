console.log(10)

const user = {
    userNAme: "aleksandre",
    userPlace: "georgia",
    userAcademy: "goa",
    userSurname: "ghomidze"

}
let text = document.getElementById("p1");
let hooper = document.getElementById("p2");
text.textContent = "Nope";
hooper.textContent= "ASA";


function sumOfTWo(a, b) {
    return a + b

}
console.log(sumOfTWo("Aleks", 10))

function textContentChanger() {
   document.getElementById("p3".textContent = "hellow")
}


function changeColorRed() {
    document.getElementById("color-red").style.color = "red";
    
}
function changeColorYellow() {
    document.getElementById("color-yellow").style.color = "yellow";

}
function changeColorBlue() {
     
    document.getElementById("color-blue").style.color = "blue";
}