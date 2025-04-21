int nylon = int.Parse(Console.ReadLine());
int paint = int.Parse(Console.ReadLine());
int quantityThinner = int.Parse(Console.ReadLine());
int needetHours = int.Parse(Console.ReadLine());

double paintafterPercent = paint + (paint * 0.10);
double amountNylon = (nylon + 2) * 1.50;
double amountPaint = paintafterPercent * 14.50;
double amountThinner = quantityThinner * 5.00;
double totalAmount = amountPaint + amountNylon + amountThinner + 0.40;
double amountCraftsman = (totalAmount * 0.30) * needetHours;
double totalSum = totalAmount + amountCraftsman;


Console.WriteLine($"{totalSum}");