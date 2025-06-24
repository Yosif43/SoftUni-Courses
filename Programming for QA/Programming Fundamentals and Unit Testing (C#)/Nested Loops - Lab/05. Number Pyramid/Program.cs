int n = int.Parse(Console.ReadLine());
int currentNumber = 1;

for (int row = 1; currentNumber <= n; row++)
{
    for (int col = 1; col <= row; col++)
    {
        Console.Write(currentNumber + " ");
        currentNumber++;
        if (currentNumber > n)
        {
            break;
        }
    }
    Console.WriteLine();
    if (currentNumber > n)
    {
        break;
    }
}