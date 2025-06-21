int n = int.Parse(Console.ReadLine());

int numsDividedBy2Mod0Count = 0;
int numsDividedBy3Mod0Count = 0;
int numsDividedBy4Mod0Count = 0;
for (int i = 0; i < n; i++)
{
    int currentNumber = int.Parse(Console.ReadLine());

    if (currentNumber % 2 == 0)
    {
        numsDividedBy2Mod0Count++;
    }

    if (currentNumber % 3 == 0)
    {
        numsDividedBy3Mod0Count++;
    }

    if (currentNumber % 4 == 0)
    {
        numsDividedBy4Mod0Count++;
    }
}

double numsDividedBy2Mod0Percentage = (double)numsDividedBy2Mod0Count / n * 100;
double numsDividedBy3Mod0Percentage = (double)numsDividedBy3Mod0Count / n * 100;
double numsDividedBy4Mod0Percentage = (double)numsDividedBy4Mod0Count / n * 100;

Console.WriteLine($"{numsDividedBy2Mod0Percentage:F2}%");
Console.WriteLine($"{numsDividedBy3Mod0Percentage:F2}%");
Console.WriteLine($"{numsDividedBy4Mod0Percentage:F2}%");