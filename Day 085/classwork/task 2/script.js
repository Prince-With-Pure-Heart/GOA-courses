function manualSlice(massive, start, end){
    return massive.splice(start, end);
}

console.log(manualSlice([1,2,3,4,5,6], 2, 4))