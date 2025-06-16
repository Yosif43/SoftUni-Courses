string text = Console.ReadLine();
int n = int.Parse(Console.ReadLine());

Console.WriteLine(RepeatString(text, n));
static string RepeatString(string input, int count)
{
    string output = "";
    for (int i = 1; i <= count; i++)
    {
        output += input;
    }



    return output;
}