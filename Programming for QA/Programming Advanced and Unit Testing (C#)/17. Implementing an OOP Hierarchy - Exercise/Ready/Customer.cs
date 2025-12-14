using System;
using System.Collections.Generic;

namespace ExerciseOopHierarchy
{
	public class Customer
	{
		//характеристики: списък с поръчки, име, имейл
		private List<Order> _orderHistory = new();
		public IReadOnlyCollection<Order> OrderHistory => this._orderHistory.AsReadOnly();
		public string Name { get; set; }
		public string Email { get; set; }

		//конструктор
		public Customer (string name, string email)
		{
            //нов празен обект
            //_orderHistor = {}
            Name = name;
			Email = email;

		}

		//действия
		public void AddOrder (Order order)
		{
			_orderHistory.Add(order);

        }

	}
}

