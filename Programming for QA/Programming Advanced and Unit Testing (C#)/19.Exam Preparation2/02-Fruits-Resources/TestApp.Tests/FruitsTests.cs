using System.Collections.Generic;

using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class FruitsTests
{
    [Test]
    public void Test_GetFruitQuantity_FruitExists_ReturnsQuantity()
    {
        // Arange
        Dictionary<string, int> fruitsDictionary = new()
        {
            { "apple", 5 },
            { "banana", 15 },
            { "orange", 25 },
        };
        string askedFruit = "banana";
        int expected = 15;
        //Act
        int result = Fruits.GetFruitQuantity(fruitsDictionary, askedFruit);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_GetFruitQuantity_FruitDoesNotExist_ReturnsZero()
    {
        // Arange
        Dictionary<string, int> fruitsDictionary = new()
        {
            { "apple", 5 },
            { "banana", 15 },
            { "orange", 25 },
        };
        string askedFruit = "kiwi";
        int expected = 0;
        //Act
        int result = Fruits.GetFruitQuantity(fruitsDictionary, askedFruit);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_GetFruitQuantity_EmptyDictionary_ReturnsZero()
    {
        // Arange
        Dictionary<string, int> fruitsDictionary = new();
        string askedFruit = "banana";
        int expected = 0;
        //Act
        int result = Fruits.GetFruitQuantity(fruitsDictionary, askedFruit);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_GetFruitQuantity_NullDictionary_ReturnsZero()
    {
        // Arange
        Dictionary<string, int> fruitsDictionary = null;
        string askedFruit = "banana";
        int expected = 0;
        //Act
        int result = Fruits.GetFruitQuantity(fruitsDictionary, askedFruit);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_GetFruitQuantity_NullFruitName_ReturnsZero()
    {
        // Arange
        Dictionary<string, int> fruitsDictionary = new()
        {
            { "apple", 5 },
            { "banana", 15 },
            { "orange", 25 },
        };
        string askedFruit = null;
        int expected = 0;
        //Act
        int result = Fruits.GetFruitQuantity(fruitsDictionary, askedFruit);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }
}
