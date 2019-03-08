class FizzBuzzer:
    
    def run(self):
        return " ".join([str(self.integer_to_fizzbuzz(num)) for num in range(1,101)])

    def integer_to_fizzbuzz(self, input):
        result = ''

        if input % 3 == 0:
            result += 'Fizz'
        if input % 5 == 0:
            result += 'Buzz'

        if result:
            return result
        else:
            return input