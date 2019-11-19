using System.Collections.Generic;
using System.Linq;

namespace Fibonacci
{
    internal class Sequence
    {
        private List<int> _sequence = new List<int>();

        public string Generate(int length) {
            _sequence.Add(0);
            if (length >= 1) _sequence.Add(1);
            if (length >= 2) {
                foreach (var i in Enumerable.Range(2, length-1)) {
                    _sequence.Add((_sequence[i-2] + _sequence[i-1]));
                }
            }

            return string.Join(", ", _sequence.ToArray());
        }
    }
}