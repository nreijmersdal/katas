using System.Collections.Generic;
using System.Linq;

namespace FizzBuzz
{
    public class FizzBuzzer {

        public string Run(int start = 1, int count = 100) {
            var result = new List<string>();
            foreach (var index in Enumerable.Range(start, count)) {
                result.Add(forNumber(index));
            }
            return string.Join(" ", result.ToArray());
        }

        public string forNumber(int number) {
            var result = "";

            if (number%3==0) result += "Fizz";
            if (number%5==0) result += "Buzz";
            if (result=="") result += number.ToString();
            
            return result;
        }
    }
}