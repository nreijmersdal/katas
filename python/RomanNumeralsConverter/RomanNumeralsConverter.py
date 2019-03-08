class RomanNumeralsConverter:

    mapping = [
        ['M',1000],
        ['CM',900],
        ['D',500],
        ['CD',400],
        ['C',100],
        ['XC',90],
        ['L',50],
        ['XL',40],
        ['X',10],
        ['IX',9],
        ['V',5],
        ['IV',4],
        ['I',1]
    ]

    def convert(self, input):
        if type(input) == int:
            return self.convert_to_numeral(input)
        elif type(input) == str:      
            return self.convert_to_arabic(input)
    
    def convert_to_arabic(self, numeral):
        result = 0

        for i in reversed(range(len(self.mapping))):
            while numeral.endswith(self.mapping[i][0]):
                numeral = numeral[:len(numeral)-len(self.mapping[i][0])]
                result += self.mapping[i][1]

        return result

    def convert_to_numeral(self, number):
        result = ''

        for i in range(len(self.mapping)):
            while number >= self.mapping[i][1]:
                result += self.mapping[i][0]
                number -= self.mapping[i][1]

        return result