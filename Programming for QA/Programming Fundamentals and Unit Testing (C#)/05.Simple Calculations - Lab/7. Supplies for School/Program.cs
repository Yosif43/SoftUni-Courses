int penPackages = int.Parse(Console.ReadLine());
int marketPackages = int.Parse(Console.ReadLine());
int boardCleaner = int.Parse(Console.ReadLine());
int discount = int.Parse(Console.ReadLine());

double packagePens = penPackages * 5.80;
double packageMarker = marketPackages * 7.20;
double cleanerBoards = boardCleaner * 1.20;
double totalSum = packagePens + packageMarker + cleanerBoards;
double percent = totalSum * discount / 100;
double total = totalSum - percent;

Console.WriteLine(total);