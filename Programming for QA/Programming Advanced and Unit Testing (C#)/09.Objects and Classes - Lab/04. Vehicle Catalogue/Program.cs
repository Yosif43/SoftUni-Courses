using System.Reflection;

namespace _04._Vehicle_Catalogue
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Catalogue catalogue = new Catalogue()
            {
                cars = new List<Car>(),
                trucks = new List<Truck>()
            };
            
            string input = Console.ReadLine();

            while (input != "end") 
            {
                string[] inputParams = input.Split("/");
                string type = inputParams[0];
                string brand = inputParams[1];
                string model = inputParams[2];

                if (type == "Car")
                {
                   string horsePower = inputParams[3];
                   Car car = new Car()
                   {   
                       Brand = brand,
                       Model = model,
                       HorsePower = horsePower
                   };
                    catalogue.cars.Add(car);
                }
                else if (type == "Truck")
                {
                    string weight = inputParams[3];
                    Truck truck = new Truck()
                    {
                        Brand = brand,
                        Model = model,
                        Weight = weight
                    };
                    catalogue.trucks.Add(truck);
                }
                

                input = Console.ReadLine();
            }

            catalogue.cars = catalogue.cars.OrderBy(car => car.Brand).ToList();
            catalogue.trucks = catalogue.trucks.OrderBy(truck => truck.Brand).ToList();
            if (catalogue.cars.Count > 0)
            {
                Console.WriteLine("Cars:");
                foreach (var car in catalogue.cars)
                {
                    Console.WriteLine($"{car.Brand}: {car.Model} - {car.HorsePower}hp");
                }
            }
            if (catalogue.trucks.Count > 0)
            {
                Console.WriteLine("Trucks:");
                foreach (var truck in catalogue.trucks)
                {
                    Console.WriteLine($"{truck.Brand}: {truck.Model} - {truck.Weight}kg");
                }
            }
        }

        public class Truck
        {
            public string Brand { get; set; }
            public string Model { get; set; }
            public string Weight { get; set; }
        }

        public class Car
        {
            public string Brand { get; set; }
            public string Model { get; set; }
            public string HorsePower { get; set; }
        }
        public class Catalogue
        {
            public List<Truck> trucks { get; set; }
            public List<Car> cars { get; set; }
        }
    }
}
