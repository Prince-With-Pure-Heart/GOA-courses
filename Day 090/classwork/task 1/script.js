const box = document.getElementById('bbox');

let position = 0;
let direction = 1;

 
setInterval(() => {
    position += direction;

    if(position >= 300 - 50){
        direction = -1;
    } else if(position <= 0){
        direction = 1;
    } 
    
    box.style.left = position + 'px';
     
},  20);