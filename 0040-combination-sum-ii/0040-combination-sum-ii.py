class Solution(object):
    def combinationSum2(self, candidates, target):
        def backtracking(idx, target, path):
            if target < 0:
                return

            if target == 0:
                result.append(path)
                return

            for i in range(idx, len(candidates)):
                # 중복되는 것을 방지하기 위해 인덱스가 dfs진행되는 idx보다 큰 상태인 것과 이전 값이 현재와 같으면 넘어간다.
                # 예를 들어 [1, 2, 2, 2, 5]인 경우
                # 1. i > idx조건이 없으면 idx가 0일 때 0 == -1의 경우를 비교하게 되어 예외처리를 해준다.
                # 이외에도 현재의 비교가 아닌 다음 값을 비교해야한다.
                # 2. 현재와 이전 값이 같은 경우를 확인해서 중복됨을 줄인다.
                # 0에서 2까지 인덱스 [1, 2, 2]일 때 만들어지고, 해당 조건이 없다면 0,1,3 인덱스를 기준으로 [1, 2, 2]가 
                # 또 들어가게 되어서 조건이 필요함.
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                backtracking(i + 1, target - candidates[i], path + [candidates[i]])
        result = []
        # 정렬을 한 상태로 만든다.
        candidates.sort()
        backtracking(0, target, [])
        # result.sort()
        return result
        