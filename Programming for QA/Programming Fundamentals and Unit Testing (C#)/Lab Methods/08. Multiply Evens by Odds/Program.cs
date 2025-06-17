int n = Math.Abs(int.Parse(Console.ReadLine()));

Console.WriteLine(GetMultipleOfEvenAndOdds(n));

static int GetSumOfEvenDigits(int number)
{
    int evenSum = 0;

    while (number > 0)
    {
        int digit = number % 10;
        number /= 10;
        if (digit % 2 == 0)
        {
            evenSum += digit;
        }
    }
    return evenSum;
}

static int GetSumOfOddDigits(int number)
{
    int oddSum = 0;

    while (number > 0)
    {
        int digit = number % 10;
        number /= 10;
        if (digit % 2 != 0)
        {
            oddSum += digit;
        }
    }
    return oddSum;
}

static int GetMultipleOfEvenAndOdds(int number)
{
    return GetSumOfEvenDigits(number) * GetSumOfOddDigits(number);
}