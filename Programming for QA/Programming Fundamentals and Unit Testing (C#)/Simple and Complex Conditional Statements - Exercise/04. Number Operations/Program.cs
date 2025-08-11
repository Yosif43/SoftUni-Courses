double number1 = double.Parse(Console.ReadLine());
double number2  = double.Parse(Console.ReadLine());
string evOperator = Console.ReadLine();

if (evOperator == "+")
{
    double result = number1 + number2;
    Console.WriteLine($"{number1} {evOperator} {number2} = {result:F2}");
}
else if (evOperator == "-")
{
    double result = (number1 - number2);
    Console.WriteLine($"{number1} {evOperator} {number2} = {result:F2}");
}
else if (evOperator == "*")
{
    double result = number1 * number2;
    Console.WriteLine($"{number1} {evOperator} {number2} = {result:F2}");
}
else if (evOperator == "/")
{
    double result = number1 / number2;
    Console.WriteLine($"{number1} {evOperator} {number2} = {result:F2}");
}