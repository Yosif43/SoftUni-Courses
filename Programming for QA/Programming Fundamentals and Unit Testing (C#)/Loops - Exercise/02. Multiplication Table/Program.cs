int number = int.Parse(Console.ReadLine());

for (int i = 1;  i <= 10; i++)
{
    int sum = number * i;
    Console.WriteLine($"{number} x {i} = {sum}");
}