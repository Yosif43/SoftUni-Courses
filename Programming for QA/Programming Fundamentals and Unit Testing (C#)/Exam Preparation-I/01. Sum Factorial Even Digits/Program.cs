int number = int.Parse(Console.ReadLine());

int sum = 0;

while (number > 0)
{
    int digit = number % 10;
    number /= 10;

    if (digit % 2 == 0)
    {
        int factorial = 1;

        for (int i = 1;  i <= digit; i++)
        {
            factorial *= i;
        }
        sum += factorial;
    }
}


Console.WriteLine(sum);