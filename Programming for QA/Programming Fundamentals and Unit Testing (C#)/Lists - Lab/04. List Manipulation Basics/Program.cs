List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

string command;
while ((command = Console.ReadLine()) != "end")
{
    string[] tokens = command.Split(' ');
    int number, index;

    switch (tokens[0])
    {
        case "Add":
            number = int.Parse(tokens[1]);
            numbers.Add(number);
            break;
        case "Remove":
            number = int.Parse(tokens[1]);
            numbers.Remove(number);
            break;
        case "RemoveAt":
            index = int.Parse(tokens[1]);
            numbers.RemoveAt(index);
            break;
        case "Insert":
            number = int.Parse(tokens[1]);
            index = int.Parse(tokens[2]);
            numbers.Insert(index, number);
            break;
    }
}

Console.WriteLine(string.Join(" ", numbers));