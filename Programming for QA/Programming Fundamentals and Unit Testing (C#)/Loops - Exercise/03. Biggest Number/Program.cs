int num = int.Parse(Console.ReadLine());

int maximumNumber = 0;
for (int i = 0; i < num; i++)
{
    int currentNumber = int.Parse(Console.ReadLine());
    if (currentNumber > maximumNumber)
    {
        maximumNumber = currentNumber;
    }
}

Console.WriteLine(maximumNumber);