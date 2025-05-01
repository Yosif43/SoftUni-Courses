using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class AverageTests
{
    // TODO: finish the test
    [Test]
    public void Test_CalculateAverage_InputHasOneElement_ShouldReturnSameElement()
    {
        // Arrange
        int[] array = { 42 };
        double expected = 42;

        // Act
        double result = Average.CalculateAverage(array);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_CalculateAverage_InputHasPositiveIntegers_ShouldReturnCorrectAverage()
    {
        // Arrange
        int[] array = { 10, 20, 30, 40 };
        double expected = 25;

        // Act
        double result = Average.CalculateAverage(array);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_CalculateAverage_InputHasNegativeIntegers_ShouldReturnCorrectAverage()
    {
        // Arrange
        int[] array = { -10, -20, -30, -40 };
        double expected = -25;

        // Act
        double result = Average.CalculateAverage(array);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_CalculateAverage_InputHasMixedIntegers_ShouldReturnCorrectAverage()
    {
        // Arrange
        int[] array = { -10, 20, -30, 40 };
        double expected = 5;

        // Act
        double result = Average.CalculateAverage(array);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }
}
