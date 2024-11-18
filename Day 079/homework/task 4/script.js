let counter = 0;
let count = document.getElementById("count");
let input = document.getElementById("username");
input.addEventListener("input", increaseCounter );


function increaseCounter(){
    let max = 200;
    let amount = input.value.length;

    if(amount > max){
        count.style.color = "red";
        count.textContent = "No more characters are allowed";
    }else{
        count.textContent = amount + "/" + max + " characters";
        count.style.color = "green";
    }


    
};
