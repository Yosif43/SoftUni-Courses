using System.Text.RegularExpressions;
using System.Text.RegularExpressions.MatchCollection;

string text = "Today is 2015-05-11, but tomorrow will be 2015-05-12";

string pattern = @"\d{4}-\d{2}-\d{2}";

Regex regex = new Regex(pattern);

bool containsValidDate = regex.IsMatch(text);
Match match = regex.Match(text);
MatchCollection matches = regex.Matches(text);

Console.WriteLine(containsValidDate);
Console.WriteLine(match);
Console.WriteLine(matches);