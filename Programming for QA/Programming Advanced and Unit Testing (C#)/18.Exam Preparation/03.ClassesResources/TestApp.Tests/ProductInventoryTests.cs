using NUnit.Framework;
using System;
using TestApp.Product;

namespace TestApp.Tests;

[TestFixture]
public class ProductInventoryTests
{
    private ProductInventory _inventory = null!;
    
    [SetUp]
    public void SetUp()
    {
        this._inventory = new();
    }
    
    [Test]
    public void Test_AddProduct_ProductAddedToInventory()
    {
        //Arrange
        string productName = "apple";
        double productPrice = 10;
        int productQuantity = 5;

        string expected = $"Product Inventory:{Environment.NewLine}" + 
            $"apple - Price: $10.00 - Quantity: 5";
        //Act
        _inventory.AddProduct(productName, productPrice, productQuantity);
        string output = _inventory.DisplayInventory();
        //Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_DisplayInventory_NoProducts_ReturnsEmptyString()
    {
        // Arrange

        string expected = $"Product Inventory:";
        //Act
        string output = _inventory.DisplayInventory();
        //Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_DisplayInventory_WithProducts_ReturnsFormattedInventory()
    {
        // Arrange
        string productName = "apple";
        double productPrice = 10;
        int productQuantity = 5;
        string productName2 = "orange";
        double productPrice2 = 20;
        int productQuantity2 = 2;

        string expected = $"Product Inventory:{Environment.NewLine}" +
            $"apple - Price: $10.00 - Quantity: 5{Environment.NewLine}" + 
            $"orange - Price: $20.00 - Quantity: 2";
        //Act
        _inventory.AddProduct(productName, productPrice, productQuantity);
        _inventory.AddProduct(productName2, productPrice2, productQuantity2);
        string output = _inventory.DisplayInventory();
        //Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_CalculateTotalValue_NoProducts_ReturnsZero()
    {
        // Arrange

        double expected = 0;
        //Act
        double output = _inventory.CalculateTotalValue();
        //Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_CalculateTotalValue_WithProducts_ReturnsTotalValue()
    {
        //Arrange
        string productName = "apple";
        double productPrice = 10;
        int productQuantity = 5;
        string productName2 = "orange";
        double productPrice2 = 20;
        int productQuantity2 = 2;

        double expected = 90;

        //Act
        _inventory.AddProduct(productName, productPrice, productQuantity);
        _inventory.AddProduct(productName2, productPrice2, productQuantity2);
        double output = _inventory.CalculateTotalValue();
        //Assert
        Assert.That(output, Is.EqualTo(expected));
    }
}
