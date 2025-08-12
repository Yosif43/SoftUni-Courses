int temperature = int.Parse(Console.ReadLine());
string timeOfDay = Console.ReadLine();
string outfit = "";
string shoes = "";

if (temperature >= 10 &&  temperature <= 18)
{
    if (timeOfDay == "Morning")
    {
        outfit = "Sweetshirt";
        shoes = "Sneakers";
    }
    else if (timeOfDay == "Afternoon" || timeOfDay == "Evening")
    {
        outfit = "Shirt";
        shoes = "Moccasins";
    }
}

Console.WriteLine($"It's {temperature} degrees, get your {outfit} and {shoes}.");