using System;
using System.Text;
using NUnit.Framework;

namespace TestApp.Tests;

public class OrdersTests
{
    [Test]
    public void Test_Order_WithEmptyInput_ShouldReturnEmptyString()
    {
        // Arrange
        string[] input = new string[0];

        // Act
        string result = Orders.Order(input);

        // Assert
        Assert.That(result, Is.Empty);
    }

    // TODO: finish test
    [Test]
    public void Test_Order_WithMultipleOrders_ShouldReturnTotalPrice()
    {
        // Arrange
        string[] input = new string[] { "Beer 2.00 1.0", "Beer 3.00 2.0", "Water 10.00 1.0" };
        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Beer -> 9.00");
        sb.AppendLine("Water -> 10.00");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Orders.Order(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Order_WithRoundedPrices_ShouldReturnTotalPrice()
    {
        // Arrange
        string[] input = new string[] { "Juice 2.00 2.0", "Juice 3.00 2.0", "Apple 1.00 1.0", "Apple 2.50 1.0" };
        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Juice -> 12.00");
        sb.AppendLine("Apple -> 5.00");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Orders.Order(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Order_WithDecimalQuantities_ShouldReturnTotalPrice()
    {
        // Arrange
        string[] input = new string[] { "Water 2.00 2.0", "Water 3.00 2.0", "Water 12.53 1.0", "Phone 1.0 1.15" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Water -> 62.65");
        sb.AppendLine("Phone -> 1.15");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Orders.Order(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
