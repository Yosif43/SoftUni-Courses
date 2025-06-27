int floors = int.Parse(Console.ReadLine());
int states = int.Parse(Console.ReadLine());

for (int f = floors; f >= 1; f--)
{
    string type = "";
    if (f == floors)
    {
        type = "L";
    }
    else if (f % 2 == 0)
    {
        type = "O";
    }
    else
        { type = "A"; }

    for (int e = 0; e < states; e++)
    {
        Console.Write($"{type}{f}{e} ");
    }
    Console.WriteLine();
}