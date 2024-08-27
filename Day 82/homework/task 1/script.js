function numRange(start, end){
    let arr = []
    for(let i; start < end; i ++ ){
        arr.push(i)
        
    }
    return arr
    
}

let val = calculateAverage(numRange(1, 11))


function calculateAverage(arr){
    let result = 0
    for(let i; i < arr.length; i ++){
        result += i
        
    }
    return result / arr.length
}

