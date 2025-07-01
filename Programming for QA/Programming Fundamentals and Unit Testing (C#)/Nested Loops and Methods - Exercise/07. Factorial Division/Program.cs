using System;

class FactorialDivision
{
    static void Main(string[] args)
    {
        int firstNumber = int.Parse(Console.ReadLine());
        int secondNumber = int.Parse(Console.ReadLine());

        double firstNumberFactorial = CalculateFactorial(firstNumber);
        double secondNumberFactorial = CalculateFactorial(secondNumber);

        double divisionResult = firstNumberFactorial / secondNumberFactorial;

        Console.WriteLine($"{Math.Floor(divisionResult)}");
    }

    static double CalculateFactorial(int number)
    {
        if (number == 0)
            return 1;

        double factorial = 1;
        for (int i = 1; i <= number; i++)
        {
            factorial *= i;
        }

        return factorial;
    }
}
