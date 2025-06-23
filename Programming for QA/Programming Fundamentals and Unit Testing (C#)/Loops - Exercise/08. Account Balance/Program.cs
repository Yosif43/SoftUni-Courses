double balance = 0;
string input;

while ((input = Console.ReadLine()) != "End")
{
    double transactionAmount = double.Parse(input);

    if (transactionAmount >= 0)
    {
        Console.WriteLine($"Increase: {transactionAmount:F2}");
    }
    else
    {
        Console.WriteLine($"Decrease: {-transactionAmount:F2}");
    }

    balance += transactionAmount;
}

Console.WriteLine($"Balance: {balance:F2}");