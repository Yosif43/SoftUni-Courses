int start = int.Parse(Console.ReadLine());
int end = int.Parse(Console.ReadLine());

for  (int number = start; number <= end; number++)
{
    bool isPrime = true;
    for (int i = 2; i < number; i++)
    {
        if (number % i == 0)
        {
            isPrime = false;
            break;
        }
    }
    if (isPrime)
    {
        Console.Write(number + " ");
    }
}