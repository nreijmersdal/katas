class StringCalculator:

    def __init__(self):
        self.string = ''
        self.list_of_numbers = []
        self.delimiter = ','

    def add(self, string_of_numbers):
        self.validate_input(string_of_numbers)
        self.process_delimiter()
        self.generate_list_of_numbers()
        return sum(self.list_of_numbers)

    def generate_list_of_numbers(self):
        negatives = []
        for str_number in self.string.split(self.delimiter):
            number = int(str_number)
            if number < 0: negatives.append(str_number)
            if number > 1000: number = 0
            self.list_of_numbers.append(number)
        if negatives: raise NegativeException("Negatives not allowed: " + ",".join(negatives))
    
    def process_delimiter(self):
        if self.string.startswith('//'):
            has_bracket_delimiter = self.string.find('[')
            if has_bracket_delimiter == -1:
                self.delimiter = self.string[2]
            else:
                delimiters = self.string[3:self.string.find('\n')-1]
                delimiters = delimiters.replace('[', self.delimiter)
                delimiters = delimiters.replace(']','')
                for item in delimiters.split(self.delimiter):
                    self.string = self.string.replace(item, self.delimiter)
            self.string = self.string[self.string.find('\n')+1:]
        self.string = self.string.replace('\n', self.delimiter)

    def validate_input(self, string_of_numbers):
        self.string = string_of_numbers
        if self.string == "": self.string = "0"

class NegativeException(Exception):
    pass