string product = Console.ReadLine();
int quantity = int.Parse(Console.ReadLine());

Console.WriteLine($"{GetFinalPrice(product, quantity):F2}");
static double GetFinalPrice(string p, int q)
{
    double singlePrice = 0;
    if (p == "coffee")
    {
        singlePrice = 1.50;
    }
    else if (p == "water")
    {
        singlePrice = 1.00;
    }
    else if (p == "coke")
    {
        singlePrice = 1.40;
    }
    else if (p == "snacks")
    {
        singlePrice = 2.00;
    }

    return singlePrice * q;
}