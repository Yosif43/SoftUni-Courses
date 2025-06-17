string type = Console.ReadLine();


if (type == "int")
{
    int n1 = int.Parse(Console.ReadLine());
    int n2 = int.Parse(Console.ReadLine());

    Console.WriteLine(GetGreatestInt(n1, n2));
}
else if (type == "char")
{
    char ch1 = char.Parse(Console.ReadLine());
    char ch2 = char.Parse(Console.ReadLine());

    Console.WriteLine(GetGreatestChar(ch1, ch2));
}
else if (type == "string")
{
    string str1 = Console.ReadLine();
    string str2 = Console.ReadLine();

    Console.WriteLine(GetGreatestString(str1, str2));
}


static int GetGreatestInt(int number1, int number2)
{
    if (number1 > number2)
    {
        return number1;
    }
    else
    {
        return number2;
    }
}

static char GetGreatestChar(char char1, char char2)
{
    if (char1 > char2)
    {
        return char1;
    }
    else
    {
        return char2;
    }
}

static string GetGreatestString(string string1, string string2)
{
    if (string1.CompareTo(string2) > 0)
    {
        return string1;
    }
    else
    {
        return string2;
    }
}