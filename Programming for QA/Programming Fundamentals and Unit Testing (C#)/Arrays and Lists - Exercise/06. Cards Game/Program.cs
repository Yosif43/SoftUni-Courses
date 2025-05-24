List<int> firstPlayerCards = Console.ReadLine().Split(' ').Select(int.Parse).ToList();
List<int> secondPlayerCards = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

while (firstPlayerCards.Count > 0 && secondPlayerCards.Count > 0)
{
    int firstPlayerCard = firstPlayerCards[0];
    int secondPlayerCard = secondPlayerCards[0];

    if (firstPlayerCard > secondPlayerCard)
    {
        firstPlayerCards.Add(firstPlayerCard);
        firstPlayerCards.Add(secondPlayerCard);
    }
    else if (secondPlayerCard > firstPlayerCard)
    {
        secondPlayerCards.Add(secondPlayerCard);
        secondPlayerCards.Add(firstPlayerCard);
    }

    firstPlayerCards.RemoveAt(0);
    secondPlayerCards.RemoveAt(0);

}

if (firstPlayerCards.Count > 0)
{
    int sum = firstPlayerCards.Sum();
    Console.WriteLine($"First player wins! Sum: {sum}");
}
else
{
    int sum = secondPlayerCards.Sum();
    Console.WriteLine($"Second player wins! Sum: {sum}");
}