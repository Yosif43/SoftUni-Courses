Dictionary<string, int> resources = new Dictionary<string, int>();

var resource = Console.ReadLine();

while ( resource != "stop")
{
     var quantity = int.Parse(Console.ReadLine());

    if (resources.ContainsKey(resource))
    {
        resources[resource] += quantity;
    }
    else
    {
        resources.Add(resource, quantity);
    }

     resource = Console.ReadLine();
}

foreach( var kvp in resources)
{
    Console.WriteLine($"{kvp.Key} -> {kvp.Value}");
}