int hourofDay = int.Parse(Console.ReadLine());
string dayofWeek = Console.ReadLine();

if (dayofWeek == "Monday" || dayofWeek == "Tuesday" || dayofWeek == "Wednesday" || dayofWeek == "Thursday" || dayofWeek == "Friday" || dayofWeek == "Saturday")
{
    if (hourofDay >= 10 && hourofDay <= 18) Console.WriteLine("open");
    else Console.WriteLine("closed");
}
else Console.WriteLine("closed");
