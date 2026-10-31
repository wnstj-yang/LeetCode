/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    const criteria = [1, 2, 3, 4, 5, 6]
    const sum = rolls.reduce((acc, cur) => acc + cur, 0)
    const needValue = (mean * (n + rolls.length)) - sum
    // 
    if (needValue < n || needValue < 0) return []


    let ans = []
    criteria.some(num => {
        if (n * num >= needValue) {
            ans = Array(n).fill(num)
            return true
        }
    })
    let ansSum = ans.reduce((acc, cur) => acc + cur, 0)

    if (ansSum === needValue) return ans
    else {
        let leftValue = ansSum - needValue
        let index = 0
        while (leftValue > 0) {
            if (ans[index] > 1) {
                ans[index]--
                leftValue--
            }
            else index++
        }
        return ans
    }
};