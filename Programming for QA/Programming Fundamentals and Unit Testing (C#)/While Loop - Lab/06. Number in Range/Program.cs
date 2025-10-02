int n = int.Parse(Console.ReadLine());

while (true)
{
    if (n >= 1 && n <= 100)
    {
        break;
    }
    n = int.Parse(Console.ReadLine());
}
Console.WriteLine(n);