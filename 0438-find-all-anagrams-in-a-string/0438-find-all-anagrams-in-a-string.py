class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        p_len = len(p)
        s_len = len(s)
        p_alpha_list = [0] * 26
        s_alpha_list = [0] * 26
        for num in p:
            p_alpha_list[ord(num) - ord('a')] += 1

        # 순회하면서 알파벳 위치의 개수를 카운트
        # index가 p의 크기보다 같거나 크면 p의 크기만큼 뺀 인덱스의 알파벳 개수를 줄인다.
        # 각 알파벳 개수가 동일하면 애나그램이므로 index위치를 저장
        for i in range(s_len):
            s_alpha_list[ord(s[i]) - ord('a')] += 1
            if i >= p_len:
                target = s[i - p_len]
                s_alpha_list[ord(target) - ord('a')] -= 1
            if p_alpha_list == s_alpha_list:
                result.append(i - p_len + 1)
        return result
        