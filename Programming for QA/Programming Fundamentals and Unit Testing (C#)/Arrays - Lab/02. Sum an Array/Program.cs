int[] numbers = Console.ReadLine().Split(" ").Select(int.Parse).ToArray();

int arr = 0;

for  (int i = 0; i < numbers.Length; i++)
{
    arr += numbers[i];
    
}

Console.WriteLine(arr);