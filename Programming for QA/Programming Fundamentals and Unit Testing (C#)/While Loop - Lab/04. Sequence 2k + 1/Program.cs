int number = int.Parse(Console.ReadLine());
int n = 1;

while (true)
{
    if (n > number)
    {
        break;
    }
    Console.WriteLine(n);
    n = 2 * n + 1;
}