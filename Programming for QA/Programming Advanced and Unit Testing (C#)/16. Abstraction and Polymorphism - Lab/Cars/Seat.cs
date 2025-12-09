using Cars;
using System;

internal class Seat : ICar
{
    public Seat(string model, string color)
    {
        Model = model;
        Color = color;
    }

    public string Model { get; set; }
    public string Color { get; set; }
    public string Start()
    {
        return "Engine start";
    }

    public string Stop()
    {
        return "Break!";
    }

    public override string ToString()
    {
        return $"{Color} {GetType().Name} {Model}{Environment.NewLine}" +
            $"{Start()}{Environment.NewLine}" +
            $"{Stop()}";
    }
}