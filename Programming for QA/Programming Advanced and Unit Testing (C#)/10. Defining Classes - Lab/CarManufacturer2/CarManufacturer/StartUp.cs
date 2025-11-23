namespace CarManufacturer
{
    public class StartUp
    {
        static void Main()
        {
            Car car = new Car();
            {
                car.Make = "VW";
                car.Model = "MK3";
                car.Year = 1992;
                car.FuelQuantity = 200;
                car.FuelConsumption = 8;
                car.Drive(20);
                Console.WriteLine(car.WhoAmI());
            }
        }
    }
}
