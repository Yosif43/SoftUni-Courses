using System;
using System.Collections.Generic;

namespace ExerciseOopHierarchy
{
	public class Restaurant
	{
		//характеристики: меню (списък с артикули) + клиентела (списък с клиенти)
		private List<MenuItem> _menu = new();
		private List<Customer> _customers = new();

		//дейности

		public void AddCustomer(Customer customer)
		{
			this._customers.Add(customer);
		}

        public MenuItem GetMenuItem(int index)
		{
			//1. невалиден индекс -> по-малък от първия или по-голям от последния
			if (index < 0 || index > _menu.Count -1)
			{
				//невалиден индекс
				throw new IndexOutOfRangeException();
			}
			//2. валиден индекс
			return _menu[index];
		}
		
		public void AddMenuItem(MenuItem item)
		{
			this._menu.Add(item);
		}

		public void PlaceOrder(Customer customer, Order order)
		{
			customer.AddOrder(order);
		}

		public void DisplayMenu()
		{
			Console.WriteLine("Menu Items:");
			foreach (MenuItem item in _menu)
			{
				Console.WriteLine(item.ToString());
			}
		}

		public void DisplayOrderHistory(Customer customer)
		{
			//customer = {name: "Ivan", email: "ivan@abv.bg", orderHistory: {..., ..., ...}}
			Console.WriteLine($"{customer.Name}'s Order History:");
			foreach(Order order in customer.OrderHistory)
			{
				Console.WriteLine($"Order Total: ${order.GetTotal()}");
				foreach(MenuItem item in order.Items)
				{
					Console.WriteLine($"  {item}");
				}
			}
		}

    }
}

