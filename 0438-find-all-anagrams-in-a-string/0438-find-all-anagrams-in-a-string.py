class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_len = len(p)
        s_len = len(s)
        p_alpha_list = [0] * 26
        s_alpha_list = [0] * 26
        for num in p:
            p_alpha_list[ord(num) - ord('a')] += 1
        j = 0
        for i in range(s_len):
            s_alpha_list[ord(s[i]) - ord('a')] += 1
            if i >= p_len:
                target = s[i - p_len]
                s_alpha_list[ord(target) - ord('a')] -= 1
            if p_alpha_list == s_alpha_list:
                result.append(i - p_len + 1)
            # print(p_alpha_list)
            # print(s_alpha_list)
            # print()
        return result
        