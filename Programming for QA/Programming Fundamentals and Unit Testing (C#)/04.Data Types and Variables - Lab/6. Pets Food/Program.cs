int dogfood = int.Parse(Console.ReadLine());
int catfood = int.Parse(Console.ReadLine());
double dogpack = dogfood * 2.50;
double catpack = catfood * 4.00;
double sum = dogpack + catpack;
Console.WriteLine($"{sum:F2} lv.");