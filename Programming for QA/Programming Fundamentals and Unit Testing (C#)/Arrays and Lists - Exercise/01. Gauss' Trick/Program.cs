List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

int i = 0;
int j = numbers.Count - 1;

while (i <= j)
{
    if (i == j)
    {
        Console.Write($"{numbers[i]} ");
    }
    else
    {
        Console.Write($"{numbers[i] + numbers[j]} ");
    }
    i++;
    j--;
}