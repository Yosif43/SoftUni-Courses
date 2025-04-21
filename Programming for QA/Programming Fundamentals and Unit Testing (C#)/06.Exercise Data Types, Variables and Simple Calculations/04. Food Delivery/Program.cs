double chickenMenu = double.Parse(Console.ReadLine());
double fishMenu = double.Parse(Console.ReadLine());
double vegetarianMenu = double.Parse(Console.ReadLine());

double chickenPrice = chickenMenu * 10.35;
double fishPrice = fishMenu * 12.40;
double vegetarianPrice = vegetarianMenu * 8.15;
double totalCost = chickenPrice + fishPrice + vegetarianPrice;
double priceDessert = totalCost * 0.20;
double totalSum = totalCost + priceDessert + 2.50;

Console.WriteLine($"{totalSum}");