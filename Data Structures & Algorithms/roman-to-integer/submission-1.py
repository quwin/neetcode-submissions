class Solution:
    def romanToInt(self, s: str) -> int:
        keys = {
            "" : 0,
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }
        res = 0
        prior = ""
        for i in range(len(s)):
            if prior + s[i] in keys:
                res -= keys[prior]
                res += keys[prior + s[i]]
            else:
                res += keys[s[i]]
            prior = s[i]

        return res