﻿int n = int.Parse(Console.ReadLine());

for  (int i = 2;  i <= n; i += 2)
{
    for (int j = 1; j <= n; j += 2)
    {
        int product = i * j;
        Console.Write($"{i}{j}{product} ");
    }
}