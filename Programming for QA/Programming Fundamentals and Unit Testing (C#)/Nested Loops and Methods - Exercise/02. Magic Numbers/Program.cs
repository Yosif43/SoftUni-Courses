int n = int.Parse(Console.ReadLine());

for  (int hundreds = 1; hundreds <= 9; hundreds++)
{
    for (int tens = 0; tens <= 9; tens++)
    {
        for (int singles = 0; singles <= 9; singles++)
        {
            int digitsProduct = hundreds * tens * singles;
            if (digitsProduct == n)
            {
                Console.Write($"{hundreds}{tens}{singles} ");
            }
        }
    }
}