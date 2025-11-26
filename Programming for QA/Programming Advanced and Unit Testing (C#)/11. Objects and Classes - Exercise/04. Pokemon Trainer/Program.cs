using System;
using System.Collections.Generic;
using System.Linq;

public class Program
{
    public static void Main()
    {
        Dictionary<string, Trainer> trainers = new Dictionary<string, Trainer>();
        string input;
        while ((input = Console.ReadLine()) != "Tournament")
        {
            string[] parts = input.Split(' ');
            string trainerName = parts[0];
            string pokemonName = parts[1];
            string element = parts[2];
            int health = int.Parse(parts[3]);

            if (!trainers.ContainsKey(trainerName))
            {
                trainers[trainerName] = new Trainer(trainerName);
            }

            trainers[trainerName].AddPokemon(new Pokemon(pokemonName, element, health));
        }

        string command;
        while ((command = Console.ReadLine()) != "End")
        {
            foreach (var trainer in trainers.Values)
            {
                trainer.CheckForElement(command);
            }
        }

        foreach (var trainer in trainers.Values.OrderByDescending(t => t.NumberOfBadges))
        {
            Console.WriteLine($"{trainer.Name} {trainer.NumberOfBadges} {trainer.PokemonCollection.Count}");
        }
    }
}

public class Trainer
{
    public string Name { get; private set; }
    public int NumberOfBadges { get; private set; } = 0;
    public List<Pokemon> PokemonCollection { get; private set; }

    public Trainer(string name)
    {
        Name = name;
        PokemonCollection = new List<Pokemon>();
    }

    public void AddPokemon(Pokemon pokemon)
    {
        PokemonCollection.Add(pokemon);
    }

    public void CheckForElement(string element)
    {
        if (PokemonCollection.Any(p => p.Element == element))
        {
            NumberOfBadges++;
        }
        else
        {
            for (int i = PokemonCollection.Count - 1; i >= 0; i--)
            {
                PokemonCollection[i].Health -= 10;
                if (PokemonCollection[i].Health <= 0)
                {
                    PokemonCollection.RemoveAt(i);
                }
            }
        }
    }
}

public class Pokemon
{
    public string Name { get; private set; }
    public string Element { get; private set; }
    public int Health { get; set; }

    public Pokemon(string name, string element, int health)
    {
        Name = name;
        Element = element;
        Health = health;
    }
}
