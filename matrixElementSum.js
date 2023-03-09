function solution(matrix) {
    let columns = matrix[0].length;
    let rows = matrix.length;
    let current = null;
    let prev = null;
    let sum = 0;

    console.log(`
        rows=${rows}
        columns=${columns}
    `)

    //check if there is only one row and one column. ex. [[#]]
    if (columns === 1 & rows === 1) {
        return matrix[0][0];
    }

    //sum all the values that does not have 0 below.
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns - 1; j++) {
            current = matrix[i][j];
            console.log(`outer=${current}`)

            // if the first value of a column is zero, stop the loop and continue to the next iteration.
            if (current === 0 && prev === null) {
                prev = current;
                continue;
            }



            // console.log(`i=${i}`)
            // console.log(`matrix[i]=${matrix[i]}`)


            // console.log(`inner=${current}`)
        }

        //     // if the current value is zero and prev is not null, stop the inner loop. All numbers this wont be added.
        //     if (current === 0 && prev >= 0) {
        //         return;
        //     }
        //     prev = current;
        //     sum = sum + current;
        // }
    }
    // console.log(sum)
    // return sum;
}

// solution([[1, 1, 1],
// [2, 2, 2],
// [3, 3, 3]]);
solution(
    [[0, 1, 1, 2],
    [0, 5, 0, 0],
    [2, 0, 3, 3]]);

// solution([[1, 1, 1, 0],
// [0, 5, 0, 1],
// [2, 1, 3, 10]]);


