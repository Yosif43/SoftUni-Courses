using System;
namespace ExerciseOopHierarchy
{
	//АРТИКУЛ ОТ МЕНЮТО -> ПРЕДЯСТИЕ
	public class AppetizerMenuItem : MenuItem
	{
		//наследени характеристики: Name, Description, Price

		//конструктор
		public AppetizerMenuItem(string name, string description, decimal price)
			: base (name, description, price)
		{
			
		}

        //ToString -> "Appetizer: {base.ToString()}"
        public override string ToString()
        {
            return "Appetizer: " + base.ToString();
        }
    }
}

