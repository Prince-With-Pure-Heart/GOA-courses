// ჯავასკრიტპში ფუნქციები არის კოდის რაღაც კრებული, რომელიც გამოიყენება რომ შევასრულოთ ნებისმიერი თასქი
let counter = 0;
let button = document.getElementById("clicker");
 
function increaseCounter(){
       let p1 = document.getElementById("p1");
       p1.textContent = counter ++ 
        

};
button.addEventListener("click", increaseCounter);