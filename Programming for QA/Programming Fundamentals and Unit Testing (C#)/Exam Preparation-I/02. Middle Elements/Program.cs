int[] numbers = Console.ReadLine().Split().Select(int.Parse).ToArray();

int middle = numbers.Length / 2;

int firstNumber = numbers[middle - 1];
int secondNumber = numbers[middle];
double sum = (firstNumber + secondNumber) / 2.0;
Console.WriteLine($"{sum:F2}");