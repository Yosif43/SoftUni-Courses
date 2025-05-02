using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class EvenOddSubtractionTests
{
    [Test]
    public void Test_FindDifference_InputIsEmpty_ShouldReturnZero()
    {
        // Arrange
        int[] emptyArray = Array.Empty<int>();

        // Act
        int result = EvenOddSubtraction.FindDifference(emptyArray);

        // Assert
        Assert.That(result, Is.EqualTo(0));
    }

    // TODO: finish the test
    [Test]
    public void Test_FindDifference_InputHasOnlyEvenNumbers_ShouldReturnEvenSum()
    {
        // Arrange
        int[] evenArray = new int[] { 2, 4, 6, 8 };

        // Act
        int result = EvenOddSubtraction.FindDifference(evenArray);

        // Assert
        Assert.That(result, Is.EqualTo(20)); // The sum of 2 + 4 + 6 + 8 = 20
    }

    [Test]
    public void Test_FindDifference_InputHasOnlyOddNumbers_ShouldReturnNegativeOddSum()
    {
        // Arrange
        int[] oddArray = new int[] { 1, 3, 5, 7 };

        // Act
        int result = EvenOddSubtraction.FindDifference(oddArray);

        // Assert
        Assert.That(result, Is.EqualTo(-16)); // The negative sum of 1 + 3 + 5 + 7 = -16
    }

    [Test]
    public void Test_FindDifference_InputHasMixedNumbers_ShouldReturnDifference()
    {
        // Arrange
        int[] mixedArray = new int[] { 1, 2, 3, 4, 5 };

        // Act
        int result = EvenOddSubtraction.FindDifference(mixedArray);

        // Assert
        Assert.That(result, Is.EqualTo(-3));
    }
}
