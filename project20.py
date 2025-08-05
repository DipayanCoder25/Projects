class RomanValueChanger:
    def __init__(self):
        self.roman_numerals = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def int_to_roman(self, number):
        if not (0 < number < 4000):
            raise ValueError("Number must be between 1 and 3999")
        
        result = ''
        for value, symbol in self.roman_numerals:
            while number >= value:
                result += symbol
                number -= value
        return result



converter = RomanValueChanger()
a = int(input("Enter a value you want to change to roman: "))
print(converter.int_to_roman(a))  
b  = int(input("Enter a value you want to change to roman: "))
print(converter.int_to_roman(b))  
