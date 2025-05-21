int[] array1 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

int[] array2 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

bool areIdentical = true;
for (int i = 0; i < array1.Length; i++)
{
    if (array1[i] != array2[i])
    {
        areIdentical = false;
        break;
    }
}

if (areIdentical)
{
    Console.WriteLine("Arrays are identical.");
}
else
{
    Console.WriteLine("Arrays are not identical.");
}