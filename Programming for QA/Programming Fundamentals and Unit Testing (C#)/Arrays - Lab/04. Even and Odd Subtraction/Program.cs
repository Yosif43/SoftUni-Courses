int[] numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

int sumEven = numbers.Where(x => x % 2 == 0).Sum();

int sumOdd = numbers.Where(x => x % 2 != 0).Sum();

int difference = sumEven - sumOdd;

Console.WriteLine(difference);