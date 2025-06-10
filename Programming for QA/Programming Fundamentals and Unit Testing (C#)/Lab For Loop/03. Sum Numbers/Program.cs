double num1 = double.Parse(Console.ReadLine());

double sum = 0;

for  (double i = 1; i <= num1; i++)
{
    double number = double.Parse(Console.ReadLine());
    sum += number;
}

Console.WriteLine(sum);