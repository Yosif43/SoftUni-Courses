using NUnit.Framework;

using System.Collections.Generic;

namespace TestApp.UnitTests;

public class MaxNumberTests
{

    [Test]
    public void Test_FindMax_InputHasOneElement_ShouldReturnTheElement()
    {
        // Arrange
        var numbers = new List<int> { 42 };
        var expectedMax = 42;

        // Act
        var actualMax = MaxNumber.FindMax(numbers);

        // Assert
        Assert.AreEqual(expectedMax, actualMax);
    }

    [Test]
    public void Test_FindMax_InputHasPositiveIntegers_ShouldReturnMaximum()
    {
        // Arrange
        var numbers = new List<int> { 1, 2, 3, 4, 5 };
        var expectedMax = 5;

        // Act
        var actualMax = MaxNumber.FindMax(numbers);

        // Assert
        Assert.AreEqual(expectedMax, actualMax);
    }

    [Test]
    public void Test_FindMax_InputHasNegativeIntegers_ShouldReturnMaximum()
    {
        // Arrange
        var numbers = new List<int> { -5, -4, -3, -2, -1 };
        var expectedMax = -1;

        // Act
        var actualMax = MaxNumber.FindMax(numbers);

        // Assert
        Assert.AreEqual(expectedMax, actualMax);
    }

    [Test]
    public void Test_FindMax_InputHasMixedIntegers_ShouldReturnMaximum()
    {
        // Arrange
        var numbers = new List<int> { -10, 0, 5, 3, -2, 20, -1 };
        var expectedMax = 20;

        // Act
        var actualMax = MaxNumber.FindMax(numbers);

        // Assert
        Assert.AreEqual(expectedMax, actualMax);
    }

    [Test]
    public void Test_FindMax_InputHasDuplicateMaxValue_ShouldReturnMaximum()
    {
        // Arrange
        var numbers = new List<int> { 1, 2, 3, 3, 2, 1 };
        var expectedMax = 3;

        // Act
        var actualMax = MaxNumber.FindMax(numbers);

        // Assert
        Assert.AreEqual(expectedMax, actualMax);
    }
}
