using System;
namespace ExerciseOopHierarchy
{
	//АРТИКУЛ ОТ МЕНЮТО -> ДЕСЕРТ
	public class DessertMenuItem : MenuItem
    {
        //наследени характеристики: Name, Description, Price

        //конструктор
        public DessertMenuItem(string name, string description, decimal price)
            : base(name, description, price)
        {

        }

        //ToString -> "Dessert: {base.ToString()}"
        public override string ToString()
        {
            return "Dessert: " + base.ToString();
        }
    }

}

