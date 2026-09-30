/**
 * @param {number[]} asteroids
 * @return {number[]}
 */
var asteroidCollision = function(asteroids) {
     const stack = []
     asteroids.forEach(asteroid => {
        if (asteroid > 0) stack.push(asteroid)
        else {
            let isFinished = false
            while (stack.length > 0) {
                const top = stack[stack.length - 1]
                const asteroidSize = Math.abs(asteroid)
                // top이 음수면 같은 방향이므로 끝
                if (top < 0) break
                // 소행성의 값의 크기가 현재 stack에 있는 값보다 작으면 충돌하고 사라짐
                if (asteroidSize < top) {
                    isFinished = true
                    break
                }
                else if (asteroidSize === top) {
                    stack.pop() // 같으면 모두 충돌해서 폭발 후 끝
                    isFinished = true
                    break
                }
                // 소행성의 값 크기 > stack의 top 크기
                else {
                    stack.pop()
                }
            }
            if (!isFinished) stack.push(asteroid)
        }
     })
     return stack
};