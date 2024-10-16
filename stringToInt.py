class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        base = 0
        i = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for sign
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = 1 - 2 * (s[i] == '-')
            i += 1

        # Step 3: Convert number and check for overflow
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')  # Convert char to int
            # Check for overflow
            if base > INT_MAX // 10 or (base == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            base = 10 * base + digit
            i += 1

        return base * sign