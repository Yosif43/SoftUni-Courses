float deposit = float.Parse(Console.ReadLine());
int months = int.Parse(Console.ReadLine());
float annual = float.Parse(Console.ReadLine());
double persent = annual / 100;
double amount = deposit * persent;
double interest = amount / 12;
double total = deposit + months * interest;
Console.WriteLine($"{total:F2}");

