int points = int.Parse(Console.ReadLine());

if  (points >= 0 && points <= 3)
{
    double result = points + 5;
    Console.WriteLine(result);
}
else if (points >= 4 && points <= 6)
{
    double result = points + 15;
    Console.WriteLine(result);
}
else if (points >= 7 && points <= 9) 
{
    double result = points + 20;
    Console.WriteLine(result);
}