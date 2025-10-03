string word = Console.ReadLine();
string text = Console.ReadLine();

while (text.Contains(word))
{
    int wordIndex = text.IndexOf(word);
    string before = text.Substring(0, wordIndex);
    string after = text.Substring(wordIndex + word.Length);

    text = before + after;
}

Console.WriteLine(text);