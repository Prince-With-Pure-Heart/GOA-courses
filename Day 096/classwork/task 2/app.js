arr = [1,2,34,10,56];

// const reduced_arr =  arr.reduce((cur, value) =>{
//     return cur + value
// });

// console.log(reduced_arr);

const manualReduce = (arr, func, curValue = 0) =>{
    let acc = curValue;

    for(const i of arr){
        acc = func(acc, value);

        
    }
    return acc;
}
console.log(manualReduce ((acc, cur) => acc + cur), 10)


