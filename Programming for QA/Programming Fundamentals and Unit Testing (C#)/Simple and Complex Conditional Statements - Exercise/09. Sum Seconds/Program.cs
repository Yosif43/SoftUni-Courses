int athlete1 = int.Parse(Console.ReadLine());
int athlete2 = int.Parse(Console.ReadLine());
int athlete3 = int.Parse(Console.ReadLine());

//int totalTime = athlete1 + athlete2 + athlete3;

//int minutes = totalTime / 60;
//int seconds = totalTime % 60;
//string formattedSeconds = seconds.ToString().PadLeft(2, '0');
//Console.WriteLine($"{minutes}:{formattedSeconds}");

// or 

int totalTime = athlete1 + athlete2 + athlete3;

int minutes = totalTime / 60;
int seconds = totalTime % 60;
Console.WriteLine($"{minutes}:{seconds:D2}");
