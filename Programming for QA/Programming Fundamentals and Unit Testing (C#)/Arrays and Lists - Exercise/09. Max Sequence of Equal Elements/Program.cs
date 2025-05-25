List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

int bestStart = 0;
int bestLength = 1;
int currentStart = 0;
int currentLength = 1;

for (int i = 1; i < numbers.Count; i++)
{
    if (numbers[i] == numbers[i - 1])
    {
        currentLength++;
        if (currentLength > bestLength)
        {
            bestLength = currentLength;
            bestStart = currentStart;
        }
    }
    else
    {
        currentLength = 1;
        currentStart = i;
    }
}

for (int i = 0; i < bestLength; i++)
{
    Console.Write(numbers[bestStart] + " ");
}