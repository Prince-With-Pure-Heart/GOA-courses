// let time = 10;
// setInterval(function(){
//     time --;
//     console.log(time)
//     if(time === 0){
//         clearInterval();
//         console.log("Time's up");
//     }
// }, 1000)

let time = Date.getSeconds();
const func = setInterval(function(){
    console.log(time)
    if(time === 35){
        clearInterval();
    }
    
}, time)
 
console.log(func)