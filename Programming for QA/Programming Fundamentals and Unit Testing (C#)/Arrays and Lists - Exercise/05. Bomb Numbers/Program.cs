List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

int[] bombInfo = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
int bombNumber = bombInfo[0];
int power = bombInfo[1];

for (int i = 0; i < numbers.Count; i++)
{
    if (numbers[i] == bombNumber)
    {
        int leftIndex = Math.Max(i - power, 0);
        int rightIndex = Math.Min(i + power, numbers.Count - 1);

        numbers.RemoveRange(leftIndex, rightIndex - leftIndex + 1);

        i = leftIndex - 1;
    }
}

int sum = numbers.Sum();
Console.WriteLine(sum);