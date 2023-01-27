function solution(statues) {
    let result = 0
    let sorted = statues.sort()
    let first = sorted[0]
    let last = sorted[sorted.length - 1]

    for (let i = first; i < last; i++) {
        if (!sorted.includes(i)) {
            result++
        }
    }

    return result

}



solution([6, 2, 3, 8]) // [2, 3, 6, 8]
console.log('hi')