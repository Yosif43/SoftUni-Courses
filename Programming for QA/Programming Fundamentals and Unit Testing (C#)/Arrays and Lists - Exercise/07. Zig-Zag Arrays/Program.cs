int N = int.Parse(Console.ReadLine());

int[] array1 = new int[N];
int[] array2 = new int[N];

for (int i = 0; i < N; i++)
{
    string[] input = Console.ReadLine().Split(' ');
    int firstNumber = int.Parse(input[0]);
    int secondNumber = int.Parse(input[1]);

    if (i % 2 == 0)
    {
        array1[i] = firstNumber;
        array2[i] = secondNumber;
    }
    else
    {
        array1[i] = secondNumber;
        array2[i] = firstNumber;
    }
}

Console.WriteLine(string.Join(" ", array1));
Console.WriteLine(string.Join(" ", array2));