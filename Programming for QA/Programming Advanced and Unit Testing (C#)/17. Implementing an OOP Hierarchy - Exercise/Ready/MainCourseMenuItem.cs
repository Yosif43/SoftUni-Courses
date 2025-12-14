using System;
namespace ExerciseOopHierarchy
{
	//АРТИКУЛ ОТ МЕНЮТО -> ОСНОВНО ЯСТИЕ
	public class MainCourseMenuItem : MenuItem
    {
        //наследени характеристики: Name, Description, Price

        //конструктор
        public MainCourseMenuItem(string name, string description, decimal price)
            : base(name, description, price)
        {

        }

        //ToString -> "Main Course: {base.ToString()}"
        public override string ToString()
        {
            return "Main Course: " + base.ToString();
        }
    }
}

