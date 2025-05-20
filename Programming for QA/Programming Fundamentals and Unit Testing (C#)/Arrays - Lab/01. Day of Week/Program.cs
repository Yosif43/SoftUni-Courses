string[] days = new string[7];
days[0] = "Monday";
days[1] = "Tuesday";
days[2] = "Wednesday";
days[3] = "Thursday";
days[4] = "Friday";
days[5] = "Saturday";
days[6] = "Sunday";

string[] moreDays =
{
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"

};

int currentDay = int.Parse(Console.ReadLine());

if  (currentDay >= 1 && currentDay <= 7)
{
    
    Console.WriteLine(days[currentDay - 1]);
}
else
{
    Console.WriteLine("Invalid day!");
}