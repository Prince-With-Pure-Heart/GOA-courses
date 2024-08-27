let p1 = document.getElementById("p1");
let counter = 0;
let resetBtn = document.getElementById("reset");
let btn1 = document.getElementById("plusButton");
let btn2 = document.getElementById("minusbutton");
function increaseText(){
    p1.innerHTML = counter ++;


};
function decreaseText(){
    if(counter >= 0){
        p1.innerHTML = counter --;
    }
}
function restart(){
    p1.innerHTML = 0;
}

resetBtn.onclick = restart;
btn1.onclick = increaseText;
btn2.onclick = decreaseText;