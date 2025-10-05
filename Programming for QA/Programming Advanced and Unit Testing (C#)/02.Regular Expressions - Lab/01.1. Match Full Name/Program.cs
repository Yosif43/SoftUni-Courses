using System.Text.RegularExpressions;
string text = Console.ReadLine();

string pattern = @"\b[A-Z][a-z]+ [A-Z][a-z]+\b";

Regex regex = new Regex(pattern);
MatchCollection matches = regex.Matches(text);

foreach (Match match in matches)
{
    Console.Write(match.Value + " ");
}

