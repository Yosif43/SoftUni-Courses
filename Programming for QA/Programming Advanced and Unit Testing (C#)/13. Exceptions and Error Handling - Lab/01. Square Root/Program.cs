namespace _01._Square_Root
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string input = Console.ReadLine();

            try
            {
                double number = ParsePositiveNumber(input);
                double result = Math.Sqrt(number);
                Console.WriteLine(result);
             
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                Console.WriteLine("Goodbye.");
            }

        }

        static double ParsePositiveNumber(string input)
        {

            bool isParsed = double.TryParse(input, out double num);

            if (!isParsed)
            {
                throw new FormatException("Invalid input.");
            }

            if (num < 0)
            {
                throw new ArgumentException("Invalid number.");
            }


            return num;
        }
    }
}
