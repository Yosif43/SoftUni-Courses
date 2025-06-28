string word = Console.ReadLine();

int vowelsCount = CountVowelsInText(word);

Console.WriteLine(vowelsCount);

static int CountVowelsInText(string text)
{
    int vowelsCount = 0;
    for (int i = 0; i < text.Length; i++)
    {
        char ch = char.ToLower(text[i]);
        if (ch == 'a' || ch == 'e' || ch == 'o' || ch == 'u' || ch == 'i')
        {
            vowelsCount++;
        }
    }
    return vowelsCount;
}