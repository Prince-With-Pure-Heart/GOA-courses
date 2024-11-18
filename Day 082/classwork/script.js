// function evenSum(border){
//     let result = 0
//     for(let i = 0; i == border; i += 2 ){
//         if(i % 2 === 0){
//            result = result + i;



//         };
//     document.write(result);

//     };

// };
// console.log(evenSum(4));


// let numsArray = [];
// for(let i = 0; i == 10; i ++ ){
//     const numsObject = {
//         value: i,
//         type: ""
        
//     }
//     if(i % 2 == 0){
//         numsObject.type = "Even"
//     }else{
//         numsObject.type = "Odd"
//     }
//     numsArray.push(numsObject)
// };
// console.log(numsArray)


let tries = 3
let password = prompt()
let guess = prompt()
while(true){
    tries --
    if(guess === password){
        alert("You have succesfully logged in")
    }
    if(tries === 0){
        alert("Failed to log in")
    }if(guess != password){

        alert("Try again!")
        guess = prompt()

    }
    

}