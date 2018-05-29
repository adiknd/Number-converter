class NumberConverter:

    @staticmethod
    def convert_rom_to_arab(num):
        #Method converting roman number to arabic
        numbers_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
                        'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        result = 0
        i = 0
        while i < len(num)+1:
            if i == len(num)-1:
                result += numbers_dict[num[i]]
                return result
            else:
                if numbers_dict[num[i]] < numbers_dict[num[i+1]]:
                    result += numbers_dict[num[i] + num[i + 1]]
                    if i+1 == len(num)-1:
                        return result
                    i +=1
                else:
                    result += numbers_dict[num[i]]
                    if i == len(num) - 1:
                        return result
            i +=1

    @staticmethod
    def convert_arab_to_rom(num):
        #Method converting arabic number to roman
        rom_numbers = ('I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M')
        arab_numbers = (1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000)
        result = ''
        while num > 0:
            for i in range(1, 14):
                for j in range(num // arab_numbers[-i]):
                    if num / arab_numbers[-i]:
                        result += rom_numbers[-i]
                        num -= arab_numbers[-i]
        return result


#print(NumberConverter.convert_rom_to_arab('XXVII'))
#print(NumberConverter.convert_arab_to_rom(278))
