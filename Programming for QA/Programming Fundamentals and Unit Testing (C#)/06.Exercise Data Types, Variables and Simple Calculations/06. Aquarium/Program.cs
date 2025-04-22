int lenght = int.Parse(Console.ReadLine());
int width = int.Parse(Console.ReadLine());
int height = int.Parse(Console.ReadLine());
double percentage = double.Parse(Console.ReadLine());

double aquariumVolume = lenght * width * height;
double volumeinLiters = aquariumVolume * 0.001;
double percentCalc = percentage / 100;
double requiredLiters = volumeinLiters * (1 - percentCalc);

Console.WriteLine($"{requiredLiters:F2}");
