// Double the Numbers (map)Create an array of numbers. Use map() to return a new array where each number is doubled.
const nums = [1,2,3,4,5]
const double = nums.map((a) => a * 2);

//Filter Even Numbers (filter) Given an array of numbers, use filter() to return a new array containing only the even numbers.
const numbers = [1,3,4,56,7,19];
const evenOrOdd = numbers.filter((x) =>{
    return x % 2 === 0 ? 'Even':'Odd'
})

//Square of Numbers (map) Create an array of numbers. Use map() to return a new array where each number is squared.
const num = [1,4,56,7]
const square = num.map((number) =>{
    return number ** 2
})

// Extract Long Names (filter)Extract Long Names (filter)Create an array of names. Use filter() to return a new array of names longer than 5 characters.
const names = ['alex', 'nikolozi', 'luka', 'ana', 'zurabi']

const filterNames  = names.filter((value) =>{
    let arr =[]
    if(value.length > 5){
        arr.push(value)
    }
    return arr

})

// Capitalize First Letter (map) reate an array of strings. Use map() to return a new array where the first letter of each string is capitalized.
const letters = ['ab', 'aa', 'cc']

const capitalize = letters.map((val) =>{
    let arr = []
    for(let i in letters){
       
        arr.push( i.toUpperCase());
    
    }    
    
     
});

// Sum All Numbers (forEach) Sum All Numbers (forEach) Given an array of numbers, use forEach() to iterate through the array and find the sum of all numbers.
const Nums = [1,10,5,6]

 
 

