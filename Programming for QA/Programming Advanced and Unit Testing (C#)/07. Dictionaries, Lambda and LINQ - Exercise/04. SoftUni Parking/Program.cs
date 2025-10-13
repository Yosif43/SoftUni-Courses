var numberOfCommands = int.Parse(Console.ReadLine());

var usersWirhPlates = new Dictionary<string, string>();

for  (int i = 0; i < numberOfCommands; i++)
{
    string[] commandParams = Console.ReadLine().Split();
    string command = commandParams[0];
    string user = commandParams[1];
    

    if (command == "register")
    {
        string plate = commandParams[2];

        if (!usersWirhPlates.ContainsKey(user))
        {
            usersWirhPlates.Add(user, plate);
            Console.WriteLine($"{user} registered {plate} successfully");
        }
        else
        {
            Console.WriteLine($"ERROR: already registered with plate number {usersWirhPlates[user]}");
        }
    }
    else if (command == "unregister")
    {
        if (usersWirhPlates.ContainsKey(user))
        {
            usersWirhPlates.Remove(user);
            Console.WriteLine($"{user} unregistered successfully");
        }
        else
        {
            Console.WriteLine($"ERROR: user {user} not found");
        }
    }

}

foreach (var pair in usersWirhPlates)
{
    Console.WriteLine($"{pair.Key} => {pair.Value}");
}