int centuries = int.Parse(Console.ReadLine());
double years = centuries * 100;
double days = Math.Round(years * 365.242);
double hours = days * 24;
double minutes = hours * 60;
Console.WriteLine($"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes");