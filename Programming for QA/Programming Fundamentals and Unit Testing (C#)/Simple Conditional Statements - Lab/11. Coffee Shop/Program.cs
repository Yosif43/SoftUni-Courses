string drink = Console.ReadLine();
string extra = Console.ReadLine();

double price = 0.0;
const double CoffeePrice = 1.00;
const double TeaPrice = 0.60;
const double SugarPrice = 0.40;

if (drink == "coffee")
{
    price += CoffeePrice;
}
else if (drink == "tea")
{
    price += TeaPrice;
}
else
{
    Console.WriteLine("Invalid drink name.");
    return;
}

if (extra == "sugar")
{
    price += SugarPrice;
}
else if (extra != "no")
{
    Console.WriteLine("Invalid option for extra.");
    return;
}

Console.WriteLine($"Final price: ${price:0.00}");