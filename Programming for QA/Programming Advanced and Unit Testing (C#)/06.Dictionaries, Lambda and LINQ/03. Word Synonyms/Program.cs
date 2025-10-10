int count = int.Parse(Console.ReadLine());

Dictionary<string, string> wordsWithSynonyms = new Dictionary<string, string>();

for (int i = 0; i < count; i++)
{
    string word = Console.ReadLine();
    string synonym = Console.ReadLine();

    if (wordsWithSynonyms.ContainsKey(word))
    {
        wordsWithSynonyms[word] += ", " + synonym;
    }
    else
    {
        wordsWithSynonyms.Add(word, synonym);
    }
}

foreach(var word in wordsWithSynonyms)
{
    Console.WriteLine($"{word.Key} - {word.Value}");
}