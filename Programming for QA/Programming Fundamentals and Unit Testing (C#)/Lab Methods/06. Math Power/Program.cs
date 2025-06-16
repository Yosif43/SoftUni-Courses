int baseNumber = int.Parse(Console.ReadLine());
int power = int.Parse(Console.ReadLine());

Console.WriteLine(MathPow(baseNumber, power));

static int MathPow(int baseNum, int powers)
{
    int output = baseNum;
    for (int i = 2; i <= powers; i++)
    {
        output *= baseNum;
    }
    return output;
}