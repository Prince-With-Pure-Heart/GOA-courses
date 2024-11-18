const images = [
    
        "http://www.sololearn.com/uploads/slider/1.jpg", 
        "http://www.sololearn.com/uploads/slider/2.jpg", 
        "http://www.sololearn.com/uploads/slider/3.jpg"
     
];

let num = 0;
function next(){
    const slider = document.getElementById("slider");
    num ++;
    if(num >= images.length){
        num = 0
    }
    slider.src = images[num]
}
function prev(){
    const slider = document.getElementById("slider");
    num --;
    if(num < 0){
        num = images.length - 1;
        
    }
    slider.src = images[num]
}