class ChineseConverter:
    def __init__(self):
        self.digits = {
            0: '零', 1: '一', 2: '二', 3: '三', 4: '四',
            5: '五', 6: '六', 7: '七', 8: '八', 9: '九'
        }
        self.units = {
            10: '十',
            100: '百',
            1000: '千',
            10000: '万',
            100000000: '亿'
        }

    def to_chinese(self, num):
        if not isinstance(num, int) or num < 0:
            return "Invalid input: Number must be a non-negative integer."
        
        if num == 0:
            return {
                "original": 0,
                "converted": self.digits[0],
                "explanation": ["Zero is 零"]
            }

        result = ""
        explanation = []
        
        # Simplified logic for 0-99999 for this demo
        # A full implementation handles complex zero rules and larger numbers
        
        s_num = str(num)
        length = len(s_num)
        
        has_zero = False
        
        for i, digit in enumerate(s_num):
            d = int(digit)
            power = length - 1 - i
            unit_val = 10 ** power
            
            if d == 0:
                if not has_zero and i != length - 1: # Avoid trailing zeros and double zeros
                    has_zero = True
                    result += self.digits[0]
            else:
                if has_zero:
                    has_zero = False # Reset flag after using it
                
                result += self.digits[d]
                explanation.append(f"{d} -> {self.digits[d]}")
                
                if unit_val >= 10:
                    unit_char = self.units.get(unit_val)
                    if not unit_char:
                         # Fallback for simple powers not in map (like 100000) - simplified for now
                         # In real Chinese, 100000 is 10 Wan.
                         # Let's stick to < 100000 for robust demo or handle Wan logic
                         if unit_val == 10000:
                             unit_char = '万'
                    
                    if unit_char:
                        result += unit_char
                        explanation.append(f"x{unit_val} -> {unit_char}")

        # Cleanup: 10-19 often written as 十X instead of 一十X (One Ten X)
        # But One Ten is also correct in some contexts. Let's keep it simple or fix it.
        # Standard: 10 -> 十, 11 -> 十一. 
        if 10 <= num < 20:
            if result.startswith("一十"):
                result = result[1:] # Remove initial 'One'

        return {
            "original": num,
            "converted": result,
            "explanation": explanation
        }
