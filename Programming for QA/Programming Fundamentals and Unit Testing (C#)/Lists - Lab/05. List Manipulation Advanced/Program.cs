using System;
using System.Collections.Generic;
using System.Linq;

class ListManipulationAdvanced
{
    static void Main()
    {
        List<int> numbers = Console.ReadLine().Split(' ').Select(int.Parse).ToList();

        while (true)
        {
            string input = Console.ReadLine();
            if (input == "end") break;

            string[] tokens = input.Split(' ');
            string command = tokens[0];

            if (command == "Contains")
            {
                int numberToCheck = int.Parse(tokens[1]);
                Console.WriteLine(numbers.Contains(numberToCheck) ? "Yes" : "No such number");
            }
            else if (command == "PrintEven")
            {
                Console.WriteLine(string.Join(" ", numbers.Where(n => n % 2 == 0)));
            }
            else if (command == "PrintOdd")
            {
                Console.WriteLine(string.Join(" ", numbers.Where(n => n % 2 != 0)));
            }
            else if (command == "GetSum")
            {
                Console.WriteLine(numbers.Sum());
            }
            else if (command == "Filter")
            {
                string condition = tokens[1];
                int number = int.Parse(tokens[2]);
                List<int> filteredNumbers = new List<int>();

                if (condition == "<")
                {
                    filteredNumbers = numbers.Where(n => n < number).ToList();
                }
                else if (condition == ">")
                {
                    filteredNumbers = numbers.Where(n => n > number).ToList();
                }
                else if (condition == ">=")
                {
                    filteredNumbers = numbers.Where(n => n >= number).ToList();
                }
                else if (condition == "<=")
                {
                    filteredNumbers = numbers.Where(n => n <= number).ToList();
                }

                numbers = filteredNumbers;
            }
        }

        Console.WriteLine(string.Join(" ", numbers));
    }
}