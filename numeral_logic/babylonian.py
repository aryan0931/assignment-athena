class BabylonianConverter:
    def __init__(self):
        pass

    def to_babylonian(self, num):
        if not isinstance(num, int) or num < 0:
            return "Invalid input: Number must be a non-negative integer."
        
        if num == 0:
            return {
                "original": 0,
                "converted": ["no_value"], # Often a space or specific placeholder in later periods
                "explanation": ["Babylonians didn't have a true zero initially, but used a space or placeholder."]
            }

        # Base 60
        powers = []
        temp_num = num
        while temp_num > 0:
            powers.append(temp_num % 60)
            temp_num //= 60
        
        powers.reverse()
        
        explanation = []
        converted_representation = []
        
        for i, val in enumerate(powers):
            power_of_60 = len(powers) - 1 - i
            place_value = 60 ** power_of_60
            
            # 1-59 constructed from 10s (corner wedge) and 1s (vertical wedge)
            tens = val // 10
            ones = val % 10
            
            converted_representation.append({
                "value": val,
                "tens": tens,
                "ones": ones,
                "place_value": place_value
            })
            
            explanation.append(f"Position {power_of_60} (x{place_value}): {val} -> {tens} tens, {ones} ones")

        return {
            "original": num,
            "converted": converted_representation,
            "explanation": explanation
        }
