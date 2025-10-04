string input = Console.ReadLine();

string digits = "";
string letters = "";
string others = "";

foreach (char ch in input)
{
    if (char.IsDigit(ch)){
        digits += ch;
    }else if (char.IsLetter(ch))
    {
        letters += ch;
    }else { others += ch; }
}
Console.WriteLine(digits);
Console.WriteLine(letters);
Console.WriteLine(others);