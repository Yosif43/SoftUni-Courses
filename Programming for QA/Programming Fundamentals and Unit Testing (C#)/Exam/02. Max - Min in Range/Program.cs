int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

int startIndex = int.Parse(Console.ReadLine());
int endIndex = int.Parse(Console.ReadLine());

if (startIndex < 0 || endIndex >= numbers.Length || startIndex > endIndex)
{
    Console.WriteLine("Invalid range.");
    return;
}

int maxNumber = numbers[startIndex];
int minNumber = numbers[startIndex];
for (int i = startIndex; i <= endIndex; i++)
{
    if (numbers[i] > maxNumber) maxNumber = numbers[i];
    if (numbers[i] < minNumber) minNumber = numbers[i];
}

int sum = maxNumber + minNumber;

Console.WriteLine(sum);