var words = Console.ReadLine()
    .Split()
    .Where(s => s.Length % 2 == 0)
    .Select(s => {Console.WriteLine(s); return s;})
    .ToList();

