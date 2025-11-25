using System;
using System.Collections.Generic;
using System.Linq;

class Team
{
    public string Name { get; set; }
    public string CreatorName { get; set; }
    public List<string> Members { get; set; }

    public Team(string name, string creatorName)
    {
        Name = name;
        CreatorName = creatorName;
        Members = new List<string>();
    }
}

class Program
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        List<Team> teams = new List<Team>();

        for (int i = 0; i < n; i++)
        {
            string[] creationInput = Console.ReadLine().Split('-');
            string creator = creationInput[0];
            string teamName = creationInput[1];

            if (teams.Any(t => t.Name == teamName))
            {
                Console.WriteLine($"Team {teamName} was already created!");
            }
            else if (teams.Any(t => t.CreatorName == creator))
            {
                Console.WriteLine($"{creator} cannot create another team!");
            }
            else
            {
                Team team = new Team(teamName, creator);
                teams.Add(team);
                Console.WriteLine($"Team {teamName} has been created by {creator}!");
            }
        }

        string command;
        while ((command = Console.ReadLine()) != "end of assignment")
        {
            string[] joinInput = command.Split("->");
            string user = joinInput[0];
            string teamName = joinInput[1];

            Team team = teams.FirstOrDefault(t => t.Name == teamName);

            if (team == null)
            {
                Console.WriteLine($"Team {teamName} does not exist!");
            }
            else if (teams.Any(t => t.Members.Contains(user) || t.CreatorName == user))
            {
                Console.WriteLine($"Member {user} cannot join team {teamName}!");
            }
            else
            {
                team.Members.Add(user);
            }
        }

        var teamsWithMembers = teams
            .Where(t => t.Members.Count > 0)
            .OrderByDescending(t => t.Members.Count)
            .ThenBy(t => t.Name);

        foreach (var team in teamsWithMembers)
        {
            Console.WriteLine(team.Name);
            Console.WriteLine($"- {team.CreatorName}");
            foreach (var member in team.Members.OrderBy(m => m))
            {
                Console.WriteLine($"-- {member}");
            }
        }

        var teamsToDisband = teams.Where(t => t.Members.Count == 0).OrderBy(t => t.Name);
        Console.WriteLine("Teams to disband:");
        foreach (var team in teamsToDisband)
        {
            Console.WriteLine(team.Name);
        }
    }
}
