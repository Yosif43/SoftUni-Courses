string typeOfMovie = Console.ReadLine();
int Rows = int.Parse(Console.ReadLine());
int Seats = int.Parse(Console.ReadLine());

if (typeOfMovie == "Premiere")
{
    int totalSeats = Rows * Seats;
    double totalPrice = totalSeats * 12.00;
    Console.WriteLine($"{totalPrice:F2}");
}
else if (typeOfMovie == "Normal")
{
    int totalSeats = Rows * Seats;
    double totalPrice = totalSeats * 7.50;
    Console.WriteLine($"{totalPrice:F2}");
}
else if (typeOfMovie == "Discount")
{
    int totalSeats = Rows * Seats;
    double totalPrice = totalSeats * 5.00;
    Console.WriteLine($"{totalPrice:F2}");
}