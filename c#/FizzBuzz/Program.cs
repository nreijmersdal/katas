using System;

namespace FizzBuzz
{
    class Program
    {
        static void Main(string[] args)
        {
            var output = new FizzBuzzer().Run();
            Console.WriteLine(output);
        }
    }
}