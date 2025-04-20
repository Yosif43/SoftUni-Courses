int pages = int.Parse(Console.ReadLine());
int pageperHour = int.Parse(Console.ReadLine());
int days = int.Parse(Console.ReadLine());

int hoursNeed = pages / pageperHour;
int daysNeedet = hoursNeed / days;

Console.WriteLine(daysNeedet);