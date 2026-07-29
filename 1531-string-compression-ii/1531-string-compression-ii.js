/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLengthOfOptimalCompression = function(s, k) {
    const memo = new Map();

    const dp = (index, remain, lastChar, continuedChar) => {
        // k개보다 더 많이 삭제한 경우
        if (remain < 0) {
            return Infinity;
        }

        // 모든 문자를 처리한 경우
        if (index === s.length) {
            return 0;
        }

        // 현재 상태를 key로 저장
        const key = `${index}-${remain}-${lastChar}-${continuedChar}`;

        if (memo.has(key)) {
            return memo.get(key);
        }

        const ch = s[index];

        // 선택 1: 현재 문자 삭제
        // 삭제했으므로 remain만 1 감소
        // lastChar와 continuedChar는 그대로
        const deleteCost = dp(
            index + 1,
            remain - 1,
            lastChar,
            continuedChar
        );

        // 선택 2: 현재 문자 유지
        let keepCost;

        if (ch !== lastChar) {
            // 이전 문자와 다르면 새로운 그룹 시작
            //
            // aaa + b
            // a3    → a3b
            //          +1
            keepCost =
                1 + dp(
                    index + 1,
                    remain,
                    ch,
                    1
                );

        } else {
            // 이전 문자와 같으면 기존 그룹에 추가
            //
            // 압축 길이가 실제로 증가하는 순간:
            // a   → a2    (1 → 2)
            // a9  → a10   (9 → 10)
            // a99 → a100  (99 → 100)

            const extra =
                continuedChar === 1 ||
                continuedChar === 9 ||
                continuedChar === 99
                    ? 1
                    : 0;

            keepCost =
                extra + dp(
                    index + 1,
                    remain,
                    lastChar,
                    continuedChar + 1
                );
        }

        // 삭제 vs 유지 중 더 짧은 압축 길이 선택
        const result = Math.min(deleteCost, keepCost);

        memo.set(key, result);

        return result;
    };

    return dp(0, k, '', 0);
};



    //                 s[index]
    //                    │
    //           ┌────────┴────────┐
    //           │                 │
    //          삭제               유지
    //           │                 │
    //    remain - 1        ┌──────┴──────┐
    //                      │             │
    //                 이전과 같음     이전과 다름
    //                      │             │
    //                기존 그룹 증가   새 그룹 생성
    //                      │             │
    //                필요할 때 +1       +1
    //                      └──────┬──────┘
    //                             │
    //                    Math.min(삭제, 유지)