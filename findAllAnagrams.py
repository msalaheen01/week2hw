from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []

        char_count = defaultdict(int)

        s_length = len(s)

        p_length = len(p)

        # edge case for p > s
        if p_length > s_length:
            return res

        for char in p:
            char_count[char] += 1

        for i in range(p_length - 1):
            if s[i] in char_count:
                char_count[s[i]] -= 1

        for i in range(-1, s_length - p_length + 1):
            if i > -1 and s[i] in char_count:
                char_count[s[i]] += 1

            if (i + p_length) < s_length and s[i + p_length] in char_count:
                char_count[s[i + p_length]] -= 1

                if all(thing == 0 for thing in char_count.values()):
                    res.append(i + 1)

        return res
