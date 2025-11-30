from .roman import RomanConverter
from .mayan import MayanConverter
from .babylonian import BabylonianConverter
from .chinese import ChineseConverter

class ConverterEngine:
    def __init__(self):
        self.roman = RomanConverter()
        self.mayan = MayanConverter()
        self.babylonian = BabylonianConverter()
        self.chinese = ChineseConverter()

    def convert(self, number, target_system):
        try:
            num = int(number)
        except ValueError:
            return {"error": "Input must be a valid integer."}

        if target_system == 'roman':
            return self.roman.to_roman(num)
        elif target_system == 'mayan':
            return self.mayan.to_mayan(num)
        elif target_system == 'babylonian':
            return self.babylonian.to_babylonian(num)
        elif target_system == 'chinese':
            return self.chinese.to_chinese(num)
        else:
            return {"error": f"Unknown target system: {target_system}"}
