var count = int.Parse(Console.ReadLine());

var wordsWithSynonyms = new Dictionary<string, List<string>>();

for (var i = 0; i < count; i++)
{
    var word = Console.ReadLine();
    var synonym = Console.ReadLine();

    if (wordsWithSynonyms.ContainsKey(word))
    {
        wordsWithSynonyms[word].Add(synonym);
    }
    else
    {
        wordsWithSynonyms.Add(word, new() { synonym });
    }
}

foreach (var word in wordsWithSynonyms)
{
    string synonym = string.Join(", ", word.Value);
    Console.WriteLine($"{word.Key} - {synonym}");
}