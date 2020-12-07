class Solution:
    def reverse(self, x: int) -> int:
        rev_x = int(("-" if "-"==str(x)[0] else "")+str(x).replace("-","")[::-1])
        return 0 if rev_x<pow(-2,31) or rev_x>pow(2,31)-1 else rev_x