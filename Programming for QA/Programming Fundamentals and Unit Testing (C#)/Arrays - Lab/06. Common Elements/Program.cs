int[] array1 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

int[] array2 = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();

int[] commonElements = array1.Intersect(array2).ToArray();

Console.WriteLine(string.Join(" ", commonElements));