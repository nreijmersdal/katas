using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Fibonacci
{
    [TestClass]
    public class FibonacciTest
    {
        private Sequence fib = new Sequence();

        [TestMethod]
        public void Range_Zero()
        {
            Assert.AreEqual("0", fib.Generate(0));
        }

        [TestMethod]
        public void Range_One()
        {
            Assert.AreEqual("0, 1", fib.Generate(1));
        }

        [TestMethod]
        public void Range_Two()
        {
            Assert.AreEqual("0, 1, 1", fib.Generate(2));
        }
        
        [TestMethod]
        public void Range_Three()
        {
            Assert.AreEqual("0, 1, 1, 2", fib.Generate(3));
        }

        [TestMethod]
        public void Range_Four()
        {
            Assert.AreEqual("0, 1, 1, 2, 3", fib.Generate(4));
        }

        [TestMethod]
        public void Range_Long()
        {
            Assert.AreEqual("0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55," + 
             " 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946," +
             " 17711, 28657, 46368, 75025, 121393, 196418, 317811", fib.Generate(28));
        }

    }
}
