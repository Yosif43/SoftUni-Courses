string figure = Console.ReadLine();

if (figure == "square") {
    double num = double.Parse(Console.ReadLine());
    double square = num * num;
    Console.WriteLine($"{square:F2}");
     }
else if (figure == "rectangle") {
    double num1 = double.Parse(Console.ReadLine());
    double num2 = double.Parse(Console.ReadLine());
    double rectangle = num1 * num2;
    Console.WriteLine($"{rectangle:F2}");
    }
else if (figure == "circle") {
    double number = double.Parse(Console.ReadLine());
    double circle = Math.PI * number * number;
    Console.WriteLine($"{circle:F2}");
    }