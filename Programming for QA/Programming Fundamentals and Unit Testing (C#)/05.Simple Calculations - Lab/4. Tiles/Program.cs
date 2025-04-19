float W = float.Parse(Console.ReadLine());
float H = float.Parse(Console.ReadLine());
float Wt = float.Parse(Console.ReadLine());
float Ht = float.Parse(Console.ReadLine());
double bathroom = (W * H) * 1.10;
double area = Wt * Ht;
double total = Math.Round(bathroom / area);
Console.WriteLine(total);