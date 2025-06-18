List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

string command;
while ((command = Console.ReadLine()) != "end")
{
    string[] tokens = command.Split(' ');
    switch (tokens[0])
    {
        case "Delete":
            int elementToDelete = int.Parse(tokens[1]);
            numbers.RemoveAll(x => x == elementToDelete);
            break;
        case "Insert":
            int elementToInsert = int.Parse(tokens[1]);
            int position = int.Parse(tokens[2]);
            if (position >= 0 && position <= numbers.Count) // Check if position is valid
            {
                numbers.Insert(position, elementToInsert);
            }
            break;
    }
}

Console.WriteLine(string.Join(" ", numbers));