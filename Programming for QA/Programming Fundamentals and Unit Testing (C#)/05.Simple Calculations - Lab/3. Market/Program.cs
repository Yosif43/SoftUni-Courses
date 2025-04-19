float tprice = float.Parse(Console.ReadLine());
float tquantity = float.Parse(Console.ReadLine());
float cprice = float.Parse(Console.ReadLine());
float cquantity  = float.Parse(Console.ReadLine());
double tomatoes = tprice * tquantity;
double cucumbers = cprice * cquantity;
double total = tomatoes + cucumbers;
Console.WriteLine($"{total:F2}");