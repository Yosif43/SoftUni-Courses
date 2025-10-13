var companiesWithEmployees = new Dictionary<string, List<string>>();

string input = Console.ReadLine();

while (input != "End")
{
    string[] inputParams = input.Split(" -> ");
    string company = inputParams[0];
    string employeeID = inputParams[1];

    if (companiesWithEmployees.ContainsKey(company))
    {
        if (!companiesWithEmployees[company].Contains(employeeID))
        {
            companiesWithEmployees[company].Add(employeeID);
        }
    }
    else
    {
        companiesWithEmployees.Add(company, new List<string>() { employeeID });
    }


    input = Console.ReadLine();
}

foreach(var pair in companiesWithEmployees)
{
    Console.WriteLine(pair.Key);
    foreach(var employee in pair.Value)
    {
        Console.WriteLine($"-- {employee}");
    }
}