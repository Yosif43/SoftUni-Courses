var words = Console.ReadLine().Split().Where(s => s.Length % 2 == 0).ToList();


foreach (string word in words)
{
    Console.WriteLine(word);
}