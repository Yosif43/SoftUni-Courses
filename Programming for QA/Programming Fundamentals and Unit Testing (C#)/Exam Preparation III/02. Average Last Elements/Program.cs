int[] numbers = Console.ReadLine()
    .Split(" ", StringSplitOptions.RemoveEmptyEntries)
    .Select(int.Parse)
    .ToArray();

int elements = int.Parse(Console.ReadLine());
int arrLenght = numbers.Length;
int sum = 0;

for (int i = 0; i < elements; i++)
{
    int currentNumber = numbers[arrLenght - 1 - i];
    sum += currentNumber;
}
double lastElementAvg = (double)sum / elements;
Console.WriteLine($"{lastElementAvg:F2}");
