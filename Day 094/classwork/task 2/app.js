 

const names = ["Luka", "Lile", "Nia", "wfsdf"];

const newNames = names.filter((curValue) => {
    return curValue.length >= 4
})

console.log(newNames)

const manualFilter = (arr, func) => {
    const result = [];
    
    for(let i = 0; i < arr.length; i++){
        const bool = func(arr[i], i, arr);
        
        if(bool) {
            result.push(arr[i])
        }
    }
    
    return result;
}

console.log(manualFilter(names, (curValue) => {
    return curValue[0] != "L"
}))



