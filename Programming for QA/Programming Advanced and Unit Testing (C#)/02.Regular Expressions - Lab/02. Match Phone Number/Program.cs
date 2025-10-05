using System.Text.RegularExpressions;

string text = Console.ReadLine();

string pattern = @"\+359([\ \-])2\1\d{3}\1\d{4}\b";

Regex regex = new Regex(pattern);

MatchCollection matchCollection = regex.Matches(text);

List<string> result = new List<string>();

foreach (Match match in matchCollection)
{
    result.Add(match.Value);
}

Console.WriteLine(string.Join(", ", result));
