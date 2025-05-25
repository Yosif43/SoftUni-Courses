List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
List<int> topIntegers = new List<int>();

for (int i = 0; i < numbers.Count; i++)
{
    bool isTopInteger = true;
    int currentNumber = numbers[i];
    for (int j = i + 1; j < numbers.Count; j++)
    {
        if (currentNumber <= numbers[j])
        {
            isTopInteger = false;
            break;
        }
    }

    if (isTopInteger)
    {
        topIntegers.Add(currentNumber);
    }
}

Console.WriteLine(string.Join(" ", topIntegers));