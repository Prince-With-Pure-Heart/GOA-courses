// const numbers = [1,2,3,4,5];

// const sum = numbers.reduce((acc, cur) => {
//     return acc + cur
// }, 10);




// const manualReduce = (arr, func, startingValue = 0) => {
//     let acc = startingValue;

//     for(const value of arr){
//         acc = func(acc, value);
//     }

//     return acc;
// }

// console.log(manualReduce(numbers, (acc, cur) => acc + cur, 10));



const numbers = [1,2,3,4,5,6,7,8,9,10];


const numbersMap = numbers.map((number,index) =>{
    if(index % 2 === 0){
        return number * 2
    }else if(index % 2 !== 0){
        return number
    }
})

console.log(numbersMap)

// map - ის კლონი
const manualMap = (arr)=>{
    let result = []
    // გადავუვლით arr სიის ინდექსებს (ეს სია არის 24 ხაზზე შექმნილი ცვლადი)
    // შემდეგ კი შევამოწმებთ რომელ ინდექსზე დგას და ახალ სიაში ჩავამატებთ ჩვენი პირობის მიხედვით
    for(let index of arr){
        if(index % 2 === 0){
            result.push(arr[index] * 2)
            
        }else{
            result.push(arr[index])
        }
    }return result
    
}

console.log(manualMap(numbers));

