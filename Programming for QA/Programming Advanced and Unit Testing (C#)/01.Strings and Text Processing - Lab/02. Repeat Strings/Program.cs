string[] words = Console.ReadLine().Split().ToArray();

string output = "";

foreach (string word in words)
{
    for (int i = 0; i < word.Length; i++)
    {
        output += word;
    }
}

Console.WriteLine(output);