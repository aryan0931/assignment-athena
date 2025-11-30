class RomanConverter:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

    def to_roman(self, num):
        if not isinstance(num, int) or num <= 0 or num > 3999:
            return "Invalid input: Number must be an integer between 1 and 3999."
        
        roman_num = ''
        i = 0
        explanation = []
        
        temp_num = num
        while  num > 0:
            for _ in range(num // self.val[i]):
                roman_num += self.syb[i]
                num -= self.val[i]
                explanation.append(f"Add {self.syb[i]} ({self.val[i]})")
            i += 1
        
        return {
            "original": temp_num,
            "converted": roman_num,
            "explanation": explanation
        }

    def from_roman(self, s):
        s = s.upper()
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        explanation = []
        
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
                explanation.append(f"Subtract {s[i]} ({roman[s[i]]}) from next")
            else:
                result += roman[s[i]]
                explanation.append(f"Add {s[i]} ({roman[s[i]]})")
                
        return {
            "original": s,
            "converted": result,
            "explanation": explanation
        }
