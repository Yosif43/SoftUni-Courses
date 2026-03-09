using System;
using System.Collections.Generic;
using System.Linq;

namespace ExerciseOopHierarchy
{
	public class Order
	{
		//ХАРАКТЕРИСТИКИ

		//поле -> описваме / модифицираме артикулите
		private List<MenuItem> _items = new();
		//имаме място, където да съхраним нашите артикули


		//ИСКАМЕ САМО ДОСТЪП ЗА ЧЕТЕНЕ
		//поле -> за външния свят
		public IReadOnlyCollection<MenuItem> Items => this._items.AsReadOnly();

		//ПОВЕДЕНИЕ / ДЕЙНОСТИ

		//1. добавяне на артикул в поръчката
		public void AddItem (MenuItem menuItem)
		{
			this._items.Add(menuItem);
		}

		//2. изчислим общата сума на поръчката
		//_items = {12.90, 8.90, 5.60}
		public decimal GetTotal()
		{
			return this._items.Select(item => item.Price).Sum();
		}

	}
}

