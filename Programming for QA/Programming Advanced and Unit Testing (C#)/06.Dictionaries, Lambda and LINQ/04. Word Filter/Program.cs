var words = Console.ReadLine().Split().ToList();

List<string> filtered = new List<string>();

foreach(string word in words)
{
    if (word.Length % 2 == 0)
    {
        filtered.Add(word);
    }
}

foreach(string word in filtered)
{
    Console.WriteLine(word);
}