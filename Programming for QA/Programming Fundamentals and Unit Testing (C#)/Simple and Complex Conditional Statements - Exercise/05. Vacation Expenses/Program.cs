string season = Console.ReadLine();
string accommodation = Console.ReadLine();
int countofDays = int.Parse(Console.ReadLine());

if  (accommodation == "Hotel")
{
    if (season == "Spring")
    {
        double result = (countofDays * 30) * 0.80;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Summer")
    {
        double result = countofDays * 50;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Autumn")
    {
        double result = (countofDays * 20) * 0.70;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Winter")
    {
        double result = (countofDays * 40) * 0.90;
        Console.WriteLine($"{result:F2}");
    }
}
else if (accommodation == "Camping")
{
    if (season == "Spring")
    {
        double result = (countofDays * 10) * 0.80;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Summer")
    {
        double result = countofDays * 30;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Autumn")
    {
        double result = (countofDays * 15) * 0.70;
        Console.WriteLine($"{result:F2}");
    }
    else if (season == "Winter")
    {
        double result = (countofDays * 10) * 0.90;
        Console.WriteLine($"{result:F2}");
    }
}