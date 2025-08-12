int temperature = int.Parse(Console.ReadLine());
string timeOfDay = Console.ReadLine();

if (timeOfDay == "Morning")
{
    if (temperature >= 10 && temperature <= 18)
    {
        Console.WriteLine($"It's {temperature} degrees, get your Sweatshirt and Sneakers.");
    }
    else if (temperature > 18 &&  temperature <= 24)
    {
        Console.WriteLine($"It's {temperature} degrees, get your Shirt and Moccasins.");
    }
    else
    {
        Console.WriteLine($"It's {temperature} degrees, get your T-Shirt and Sandals.");
    }
}
else if (timeOfDay == "Afternoon")
{
    if (temperature >= 10 && temperature <= 18)
    {
        Console.WriteLine($"It's {temperature} degrees, get your Shirt and Moccasins.");
    }
    else if (temperature > 18 && temperature <= 24)
    {
        Console.WriteLine($"It's {temperature} degrees, get your T-Shirt and Sandals.");
    }
    else
    {
        Console.WriteLine($"It's {temperature} degrees, get your Swim Suit and Barefoot.");
    }
}
else if (timeOfDay == "Evening")
{
    if (temperature >= 10 && temperature <= 18)
    {
        Console.WriteLine($"It's {temperature} degrees, get your Shirt and Moccasins.");
    }
    else if (temperature > 18 && temperature <= 24)
    {
        Console.WriteLine($"It's {temperature} degrees, get your Shirt and Moccasins.");
    }
    else
    {
        Console.WriteLine($"It's {temperature} degrees, get your Shirt and Moccasins.");
    }
}