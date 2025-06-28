class HappyNumbers
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());

        for (int i = 1000; i <= 9999; i++)
        {
            int d1 = i / 1000;
            int d2 = (i / 100) % 10;
            int d3 = (i / 10) % 10;
            int d4 = i % 10;

            if (d1 + d2 == N && d3 + d4 == N)
            {
                Console.Write(i + " ");
            }
        }
    }
}
