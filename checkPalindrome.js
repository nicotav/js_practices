function solution(inputString) {
    var reversed = inputString.split('').reverse().join('');
    return inputString === reversed;
}