class Solution:
    def myAtoi(self, str: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', str.strip())), 2**31 - 1), -2**31)