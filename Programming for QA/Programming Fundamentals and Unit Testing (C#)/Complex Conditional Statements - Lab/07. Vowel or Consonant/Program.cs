string vowel = Console.ReadLine();
if (vowel == "A" || vowel == "a" || vowel == "E" || vowel == "e" || vowel == "I" || vowel == "i" || vowel == "O" || vowel == "o" || vowel == "U" || vowel == "u") Console.WriteLine("Vowel");
else Console.WriteLine("Consonant");

// or 

switch (vowel)
{
    case "a":
    case "A":
    case "e":
    case "E":
    case "I":
    case "i":
    case "O":
    case "o":
    case "U":
    case "u":
        Console.WriteLine("Vowel");
        break;
    default: Console.WriteLine("Consonant");
        break;

}