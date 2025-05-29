string text = Console.ReadLine();

int upperCaseCount = 0;
int lowerCaseCount = 0;
int spaceCount = 0;

foreach (char c in text)
{
    if (char.IsUpper(c))
    {
        upperCaseCount++;
    }
    else if (char.IsLower(c))
    {
        lowerCaseCount++;
    }
    else if (c == ' ')
    {
        spaceCount++;
    }
}

Console.WriteLine(upperCaseCount);
Console.WriteLine(lowerCaseCount);
Console.WriteLine(spaceCount);