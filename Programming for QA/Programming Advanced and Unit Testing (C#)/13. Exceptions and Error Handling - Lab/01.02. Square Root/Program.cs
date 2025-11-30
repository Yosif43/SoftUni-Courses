namespace _01._02._Square_Root
{
    internal class Program
    {
        static void Main(string[] args)
        {
            double number = double.Parse(Console.ReadLine());
            try
            {
                number = NotNegativeNumber(number);
                double result = Math.Sqrt(number);
                Console.WriteLine(result);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally { Console.WriteLine("Goodbye."); }
        }

        static double NotNegativeNumber(double input)
        {
            if (input < 0)
            {
                throw new ArgumentException("Invalid number.");
            }

            return input;
        }
    }
}
