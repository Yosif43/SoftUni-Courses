int number = int.Parse(Console.ReadLine());

if (number == 0 || number >= 100 && number <= 200);
else Console.WriteLine("invalid");

// or

bool isValid = (number == 0 || number >= 100 && number <= 200);
if (!isValid)
{
    Console.WriteLine("invalid");
}

// or 
if (!(number == 0 || number >= 100) && number <= 200) Console.WriteLine("invalid");