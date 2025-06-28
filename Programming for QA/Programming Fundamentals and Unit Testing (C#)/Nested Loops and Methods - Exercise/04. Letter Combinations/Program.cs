using System;

class LetterCombinations
{
    static void Main()
    {
        // Read input letters
        char startLetter = Console.ReadLine()[0];
        char endLetter = Console.ReadLine()[0];
        char excludedLetter = Console.ReadLine()[0];

        int combinationsCount = 0;
        string combinations = "";

        // Generate combinations
        for (char i = startLetter; i <= endLetter; i++)
        {
            for (char j = startLetter; j <= endLetter; j++)
            {
                for (char k = startLetter; k <= endLetter; k++)
                {
                    if (i != excludedLetter && j != excludedLetter && k != excludedLetter)
                    {
                        combinations += $"{i}{j}{k} ";
                        combinationsCount++;
                    }
                }
            }
        }

        // Print combinations and count
        Console.WriteLine(combinations.Trim());
        Console.WriteLine(combinationsCount);
    }
}
