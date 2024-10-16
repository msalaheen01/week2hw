class Solution:
    def reverseWords(self, s: str) -> str:
        

        words = s.split()

        reverse = words[::-1]

        reverse = ' '.join(reverse)

        return reverse