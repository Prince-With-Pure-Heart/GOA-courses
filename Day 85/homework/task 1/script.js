function manualFilter(arr, childFunc){
    let nums = [];
    for(let i = 0; i < arr.length; i ++ ){
        if(childFunc(arr[i]) === true){
            nums.push(i)

        }
    }
    return nums
}

console.log(manualFilter([1,2,3,4,5,56,7,8,10], function(value) {
    return value % 2 == 0;
}))