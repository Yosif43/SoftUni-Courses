using System.Diagnostics;
using System.Text;

string input = Console.ReadLine();

Stopwatch stopwatch = new Stopwatch();
stopwatch.Start();

StringBuilder digits = new StringBuilder();
StringBuilder letters = new StringBuilder();
StringBuilder others = new StringBuilder();

foreach (char ch in input)
{
    if (char.IsDigit(ch))
    {
        digits.Append(ch);
    }
    else if (char.IsLetter(ch))
    {
        letters.Append(ch);
    }
    else { others.Append(ch); }
}
stopwatch.Stop();
Console.WriteLine(digits);
Console.WriteLine(letters);
Console.WriteLine(others);
