from numeral_logic import ConverterEngine
import json

def test_conversions():
    engine = ConverterEngine()
    
    tests = [
        (2024, 'roman', 'MMXXIV'),
        (10, 'roman', 'X'),
        (5, 'mayan', None), # Check structure
        (61, 'babylonian', None), # Check structure
        (123, 'chinese', '一百二十三')
    ]
    
    print("Running Tests...")
    
    for num, system, expected in tests:
        result = engine.convert(num, system)
        print(f"\nTesting {num} -> {system}")
        
        if system == 'roman' or system == 'chinese':
            if result['converted'] == expected:
                print(f"PASS: {result['converted']}")
            else:
                print(f"FAIL: Expected {expected}, got {result['converted']}")
        else:
            # For complex types, just print the result to verify structure
            print(f"Result structure: {json.dumps(result['converted'], indent=2)}")

if __name__ == "__main__":
    test_conversions()
