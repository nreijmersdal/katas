import unittest
from RomanNumeralsConverter import RomanNumeralsConverter

class RomanNumeralsConverterTests(unittest.TestCase):

    test_cases = [
        [1,'I'],
        [2,'II'],
        [3,'III'],
        [4,'IV'],
        [5,'V'],
        [6,'VI'],
        [7,'VII'],
        [8,'VIII'],
        [9,'IX'],
        [10,'X'],
        [12,'XII'],        
        [14,'XIV'],        
        [19,'XIX'],        
        [29,'XXIX'],        
        [49,'XLIX'],        
        [50,'L'],
        [73,'LXXIII'],
        [99,'XCIX'],
        [100,'C'],
        [349,'CCCXLIX'],
        [443,'CDXLIII'],
        [500,'D'],
        [900,'CM'],
        [1000,'M'],
        [1903,'MCMIII'],
        [1999,'MCMXCIX'],
        [2019,'MMXIX'],               
    ]

    def test_all_cases_arabic_to_numeral(self):
        for item in self.test_cases:
            self.assertEqual(item[1], RomanNumeralsConverter().convert(item[0]))

    def test_all_cases_numeral_to_arabic(self):
        for item in self.test_cases:
            self.assertEqual(item[0], RomanNumeralsConverter().convert(item[1]))

if __name__ == '__main__':
    unittest.main()