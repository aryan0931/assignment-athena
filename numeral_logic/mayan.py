class MayanConverter:
    def __init__(self):
        pass

    def to_mayan(self, num):
        if not isinstance(num, int) or num < 0:
            return "Invalid input: Number must be a non-negative integer."
        
        if num == 0:
            return {
                "original": 0,
                "converted": ["shell"], # 0 is represented by a shell
                "explanation": ["Zero is represented by a shell symbol."]
            }

        # Mayan is Base-20
        # Positions are powers of 20: 1, 20, 400, 8000...
        # Written vertically, highest power at top.
        
        powers = []
        temp_num = num
        while temp_num > 0:
            powers.append(temp_num % 20)
            temp_num //= 20
        
        # Reverse to have highest power first (top to bottom)
        powers.reverse()
        
        explanation = []
        converted_representation = []
        
        for i, val in enumerate(powers):
            power_of_20 = len(powers) - 1 - i
            place_value = 20 ** power_of_20
            
            # Construct dot/bar representation for this digit (0-19)
            bars = val // 5
            dots = val % 5
            symbol_desc = f"{dots} dots and {bars} bars"
            if val == 0:
                symbol_desc = "Shell (0)"
            
            converted_representation.append({
                "value": val,
                "dots": dots,
                "bars": bars,
                "is_zero": val == 0,
                "place_value": place_value
            })
            
            explanation.append(f"Position {power_of_20} (x{place_value}): {val} -> {symbol_desc}")

        return {
            "original": num,
            "converted": converted_representation,
            "explanation": explanation
        }
