List<string> words = Console.ReadLine().ToLower().Split().ToList();

Dictionary<string, int> wordCounter = new Dictionary<string, int>();


foreach (string word in words)
{
    if (wordCounter.ContainsKey(word))
    {
        wordCounter[word]++;
    }
    else
    {
        wordCounter.Add(word, 1);
    }
}

foreach (var pair in wordCounter)
{
    if (pair.Value % 2 != 0)
    {
        Console.Write(pair.Key + " ");
    }
}