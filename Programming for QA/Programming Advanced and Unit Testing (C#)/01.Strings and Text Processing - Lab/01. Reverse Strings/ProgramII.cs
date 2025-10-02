string input = Console.ReadLine();

while (input != "end")
{
    char[] output = input.ToCharArray().Reverse().ToArray();
    string reversed = string.Join("", output);
    Console.WriteLine(input + " = " + reversed);

    input = Console.ReadLine();
}