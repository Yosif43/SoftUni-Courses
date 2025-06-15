int n = int.Parse(Console.ReadLine());

PrintTriangle(n);


static void PrintLine(int start, int end)
{
    for (int i = start; i <= end; i++)
    {
        Console.Write($"{i} ");
    }
    Console.WriteLine();
}

static void PrintTriangle(int size)
{
    for (int i = 1; i < size; i++)
    {
        PrintLine(1,i);
    }
    for (int i = size; i >= 1; i--)
    {
        PrintLine(1, i);
    }
}