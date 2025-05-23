List<int> firstSequence = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
List<int> secondSequence = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

List<int> mergedList = new List<int>();

int longerCount = Math.Max(firstSequence.Count, secondSequence.Count);

for (int i = 0; i < longerCount; i++)
{
    if (i < firstSequence.Count)
    {
        mergedList.Add(firstSequence[i]);
    }
    if (i < secondSequence.Count)
    {
        mergedList.Add(secondSequence[i]);
    }
}

Console.WriteLine(string.Join(" ", mergedList));