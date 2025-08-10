class Solution(object):
    def groupAnagrams(self, strs):
        result = {}
        # 정렬한 string이 키가 되고 result에 없을 시 값도 된다.
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in result:
                result[sorted_string] = [string]
            else:
                result[sorted_string].append(string)
        # 구분된 값들을 따로 추출해서 반환해준다.
        return result.values()