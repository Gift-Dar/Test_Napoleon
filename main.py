dict_values = {
    'M': 1000, 'D': 500,
    'C': 100, 'L': 50,
    'X': 10, 'V': 5,
    'I': 1
}

class Solution:
    def __init__(self):
        self.arab_Int = 0

    @staticmethod
    def checkLength(s):
        str_length = len(s)
        if str_length == 0 or str_length > 15:
            print('Введите римское число, содержащее от 1 до 15 символов.')
            return False
        return True

    @staticmethod
    def checkCharsStr(s):
        for char in s:
            if char not in dict_values.keys():
                print(f'Нельзя использвать символ "{char}" при написании римского числа!')
                return False
        return True

    def romanToInt(self, s: str) -> int:
        s = s.upper()
        s = s.replace('\"', '')
        if self.checkLength(s) and self.checkCharsStr(s):
            self.countInt(s)
            print(self.arab_Int)
            return self.arab_Int

    def countInt(self, s):
        max_value = (max(s, key=lambda x: dict_values[x]))
        index_max_value = s.find(max_value)
        self.arab_Int += dict_values[max_value]
        str_minus = s[0: index_max_value]
        str_plus = s[(index_max_value + 1):]

        if len(str_minus) == 1:
            self.arab_Int -= dict_values[str_minus]
        if len(str_plus) == 1:
            self.arab_Int += dict_values[str_plus]
        if len(str_minus) > 1:
            self.countInt(str_minus)
        if len(str_plus) > 1:
            self.countInt(str_plus)

s = input('s = ')
exm_1 = Solution()
exm_1.romanToInt(s)
