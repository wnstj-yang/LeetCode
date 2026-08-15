/**
 * @param {number[]} arr
 * @return {number[]}
 */
var threeEqualParts = function(arr) {
    let ans = [-1, -1]
    const sum = arr.reduce((arr, cur) => arr + cur, 0)
    if (sum === 0) return [0, 2]
    // 1. 합이 3의 배수가 아니면 세 등분으로 나눠도 값이 똑같지 않음
    if (sum % 3 !== 0) return [-1, -1]
    let count = 0
    let first = 0
    let second = 0
    let third = 0
    const target = sum / 3
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 1) {
            count++;
            if (count === 1) first = i
            if (count === target + 1) second = i
            if (count === target * 2 + 1) third = i
        }
    }
    console.log(first, second, third)
    while (third < arr.length) {
        if ((arr[first] !== arr[second] || arr[second] !== arr[third])) return [-1, -1]
        first++
        second++
        third++
    }


    return [first - 1, second]
};