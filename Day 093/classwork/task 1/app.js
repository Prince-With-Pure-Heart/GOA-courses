// var-ის განმასხვავებელი ნიშნებია: 1.Hoisting, ანუ ცვლადი ინიციალიზირდება კოდის გაშვებისთანავე, 2.შესაძლებელია ცვლადის რეინიზილერება, 3.ცვლადი ხელმისაწვდომია ყველა კოდის ბლოკში ანუ ყველა scope-ში

let name = "aleksandre"
console.log(name)

function changeName(){
    let name ="Nikolozi";
    console.log(name)
}

changeName();

// ფუნქციის კოდის ბლოკის გარეთ name ცვლადის მნიშვნელობაა ალექსანდრე ხოლო ფუნქციის შიგნით ნიკოლოზი
let students = [68, 70, 90, 23, 15]

for(const score of students){
    if(score >= 70){
       console.log(`student has passed`)
        
    }else{
        console.log( `student has failed`)
    }
}

// write an arrow function that takes one parameter and returns it's cube
const cube = (num) =>{
    return num ** 3
}
// write an arrow function that returns sum of two numbers
const twoSum = (num1, num2) =>{
    return num1 + num2
}
console.log(twoSum(4, 10))

// write an arrow function that returns `Learnin javscript!`
const js = () => `Learning javascript`
console.log(js)

// write an arrow functions with one parameter and returns "Even " if number is even and "odd" if number is odd

const numberType = (number) =>{
      return number % 2 == 0 ? `Even`:`Odd`
}

// Create an arrow function that takes tow numbers as argumnets and returns their multiply if second number isn't provided it should return 1

const multiply = (num1, num2) =>{
    if(num2 === undefined){
        return 1
    };
    return num1 * num2
}

console.log(multiply(1,9))

// wrtie an arrow function that takes two paramters and creates object containing this values

const createObject = (name,age) =>{
    const Object = {
        name: name,
        age: age
    }
    return Object
}
console.log(createObject("Aleksandre", 15)
)

// write an arrow function that takes to numbers , and within that write arrow function to return the product of both  numbers

const main = (num1, num2) =>{
    const product = () =>{
        return num1 * num2
    }
}
console.log(main(1,2))

// sum of arrays using for loop

const sumOfArray = (arr1, arr2) =>{
    const result = 0;
    for(let i of arr1){
        result += i

        
    }
    for(let num of arr2 ){
        result += num
    }
    return result

    
}
console.log(sumOfArray([1,2], [2,3]))