int n = int.Parse(Console.ReadLine());

int sum = 0;

for (int i = n; i != 0; i /= 10)
{
    int digit = i % 10;
    sum += digit;
}
Console.WriteLine(sum);