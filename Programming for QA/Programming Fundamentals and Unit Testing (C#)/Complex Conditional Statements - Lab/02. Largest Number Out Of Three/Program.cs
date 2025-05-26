int number1 = int.Parse(Console.ReadLine());
int number2 = int.Parse(Console.ReadLine());
int number3 = int.Parse(Console.ReadLine());

if (number1 > number2)
{
    if (number1 > number3) Console.WriteLine(number1);
    else Console.WriteLine(number3);
}
else 
    if (number2 > number3) Console.WriteLine(number2);
    else Console.WriteLine(number3);
