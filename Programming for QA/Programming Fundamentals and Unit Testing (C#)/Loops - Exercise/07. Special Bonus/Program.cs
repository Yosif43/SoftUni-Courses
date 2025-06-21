int stopNumber = int.Parse(Console.ReadLine());
int number = 0;
int previousNumber = 0;

while (true)
{
    number = int.Parse(Console.ReadLine());

    if (number == stopNumber)
    {

        double increasedValue = previousNumber * 1.2;
        Console.WriteLine($"{increasedValue}");
        break;
    }
    previousNumber = number;
}
