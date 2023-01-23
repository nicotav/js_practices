function solution(year) {
    let century = Math.floor(year / 100) + 1;

    if (year < 100) {
        return 1;
    }

    if (year % 100 === 0) {
        century--
    }

    return century
}
const century = solution(1905)

console.log(century)