int numberN = int.Parse(Console.ReadLine());
int numberP = int.Parse(Console.ReadLine());

int sum = 1;
for  (int i = 0; i < numberP; i++)
{
    sum *= numberN;
}
Console.WriteLine(sum);
