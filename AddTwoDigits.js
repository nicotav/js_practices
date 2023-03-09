// You are given a two-digit integer n. Return the sum of its digits.

// Example

// For n = 29, the output should be
// solution(n) = 11.

function solution(n) {
    var sum = 0;
    var n = n.toString();
    for (var i = 0; i < n.length; i++) {
        sum += parseInt(n[i]);
    }
    return sum;
}
