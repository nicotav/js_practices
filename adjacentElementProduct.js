// psudo code
// 1. map through the array
// 2. multiply the current value with the next value.
// 3. store the result in a variable



function solution(inputArray) {
    let result = inputArray[0] * inputArray[1];
    let reverse_array = inputArray.reverse();

    inputArray.map((item, index) => {
        let product = item * inputArray[index + 1];
        if (product > result) {
            result = product;
        }
    },)

    reverse_array.map((item, index) => {
        let product = item * reverse_array[index + 1];
        if (product > result) {
            result = product;
        }
    })

    return result;
}

solution([-23, 4, -3, 8, -12])