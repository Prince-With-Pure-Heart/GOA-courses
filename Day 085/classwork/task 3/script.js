function manualFilter(childFunc, arr ){
    let nums = [];
    for(let num = 0; num < arr.length; num ++ ){
        if(childFunc(arr[num]) === true){
            nums.push(arr[num])

        }
        
    }
    return nums
}

function isEven(num){
    return num % 2 == 0;
}
console.log(manualFilter(isEven, [1,2,3,4,5,6,77,8]))

