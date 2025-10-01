namespace ConsoleAppSummator
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }

        public static int Sum(int[] nums)
        {
            int result = 0;

            foreach (int num in nums) {
            result += num;
            }
            return result;
        }
    }
}