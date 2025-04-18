string arch = Console.ReadLine();
int projects = int.Parse(Console.ReadLine());
double hours = projects * 3;
Console.WriteLine($"The architect {arch} will need {hours} hours to complete {projects} project/s.");