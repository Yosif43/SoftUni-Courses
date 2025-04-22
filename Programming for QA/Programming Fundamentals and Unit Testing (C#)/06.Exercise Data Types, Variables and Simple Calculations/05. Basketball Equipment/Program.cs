int basketball = int.Parse(Console.ReadLine());

double sneakers = basketball - (basketball * 0.40);
double team = sneakers - (sneakers * 0.20);
double basketballPrice = team / 4;
double accessories = basketballPrice / 5;
double totalPrice = basketball + sneakers + team + basketballPrice + accessories;
Console.WriteLine(totalPrice);
