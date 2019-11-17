using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace FizzBuzz
{
    [TestClass]
    public class FizzBuzzTester {
        FizzBuzzer fb = new FizzBuzzer();

        [TestMethod]
        public void Normal_Numbers_Return_Number() {
            Assert.AreEqual("1", fb.forNumber(1));
            Assert.AreEqual("2", fb.forNumber(2));
        }

        [TestMethod]
        public void Dividable_By_Three_Returns_Fizz() {
            Assert.AreEqual("Fizz", fb.forNumber(3));
            Assert.AreEqual("Fizz", fb.forNumber(6));
        }

        [TestMethod]
        public void Dividable_By_Five_Returns_Buzz() {
            Assert.AreEqual("Buzz", fb.forNumber(5));
            Assert.AreEqual("Buzz", fb.forNumber(10));
        }
        
        [TestMethod]
        public void Dividable_By_Three_And_Five_Returns_FizzBuzz() {
            Assert.AreEqual("FizzBuzz", fb.forNumber(15));
        }

        [TestMethod]
        public void Run_Returns_FizzBuzzer_String() {
            Assert.AreEqual("1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz", fb.Run(1,10));
            Assert.AreEqual("FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz", fb.Run(90,11));
        }
    }
}
