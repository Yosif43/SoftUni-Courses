using System.Text.RegularExpressions;
string text = Console.ReadLine();

string pattern = @"\b[A-Z][a-z]+ [A-Z][a-z]+\b";

Regex regex = new Regex(pattern);
MatchCollection matches = regex.Matches(text);
List<string> result = new List<string>();

foreach (Match match in matches)
{
    result.Add(match.Value);
}

Console.WriteLine(string.Join(" ", result));
