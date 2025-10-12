var word = Console.ReadLine();

Dictionary<char, int> characters = new Dictionary<char, int>();

foreach (char ch in word)
{
    if (ch != ' ')
    {
        if (characters.ContainsKey(ch))
        {
            characters[ch]++;
        }
        else
        {
            characters.Add(ch, 1);
        }
    }
}

foreach(var pair in characters)
{
    Console.WriteLine($"{pair.Key} -> {pair.Value}");
}