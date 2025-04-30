using NUnit.Framework;

using System.Collections.Generic;

namespace TestApp.UnitTests;

public class AdjacentEqualTests
{
    // TODO: finish test
    [Test]
    public void Test_Sum_InputIsEmptyList_ShouldReturnEmptyString()
    {
        // Arrange
        List<int> emptyList = new List<int>();

        // Act
        var result = AdjacentEqual.Sum(emptyList);

        // Assert
        Assert.That(result, Is.EqualTo(""));
    }

    // TODO: finish test
    [Test]
    public void Test_Sum_NoAdjacentEqualNumbers_ShouldReturnOriginalList()
    {
        // Arrange
        List<int> numbers = new List<int> { 1, 2, 3, 4, 5 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("1 2 3 4 5"));
    }

    [Test]
    public void Test_Sum_AdjacentEqualNumbersExist_ShouldReturnSummedList()
    {
        // Arrange
        List<int> numbers = new List<int> { 1, 2, 2, 3, 4 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("1 4 3 4"));
    }

    [Test]
    public void Test_Sum_AllNumbersAreAdjacentEqual_ShouldReturnSingleSummedNumber()
    {
        // Arrange
        List<int> numbers = new List<int> { 2, 2, 2, 2, 2 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("10"));
    }

    [Test]
    public void Test_Sum_AdjacentEqualNumbersAtBeginning_ShouldReturnSummedList()
    {
        // Arrange
        List<int> numbers = new List<int> { 3, 3, 2, 1, 1 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("6 2 2"));
    }

    [Test]
    public void Test_Sum_AdjacentEqualNumbersAtEnd_ShouldReturnSummedList()
    {
        // Arrange
        List<int> numbers = new List<int> { 1, 2, 2, 3, 3 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("1 4 6"));
    }

    [Test]
    public void Test_Sum_AdjacentEqualNumbersInMiddle_ShouldReturnSummedList()
    {
        // Arrange
        List<int> numbers = new List<int> { 1, 2, 2, 2, 3 };

        // Act
        var result = AdjacentEqual.Sum(numbers);

        // Assert
        Assert.That(result, Is.EqualTo("1 6 3"));
    }
}
