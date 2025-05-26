string product = Console.ReadLine();
string day = Console.ReadLine();

if (day == "Weekday")
{
    if (product == "Banana") {
        double banana = 2.50;
        Console.WriteLine($"{banana:F2}");
    }
    else if (product == "Apple")
    {
        double apple = 1.30;
        Console.WriteLine($"{apple:F2}");
    }
    else if(product == "Kiwi")
    {
        double kiwi = 2.20;
        Console.WriteLine($"{kiwi:F2}");    
    }
    
}
else if (day == "Weekend")
{
    if (product == "Banana")
    {
        double banana = 2.70;
        Console.WriteLine($"{banana:F2}");
    }
    else if (product == "Apple")
    {
        double apple = 1.60;
        Console.WriteLine($"{apple:F2}");
    }
    else if (product == "Kiwi")
    {
        double kiwi = 3.00;
        Console.WriteLine($"{kiwi:F2}");
    }
}
    