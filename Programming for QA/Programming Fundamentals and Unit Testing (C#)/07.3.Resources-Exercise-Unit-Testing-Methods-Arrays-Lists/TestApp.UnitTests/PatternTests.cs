using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class PatternTests
{
    [Test]
    public void Test_SortInPattern_SortsIntArrayInPattern_SortsCorrectly()
    {
        // Arrange
        int[] inputArray = new int[] { 5, 3, 2, 8, 5, 2 };
        int[] expectedOutput = new int[] { 2, 8, 3, 5 };

        // Act
        var result = Pattern.SortInPattern(inputArray);

        // Assert
        Assert.AreEqual(expectedOutput, result);
    }

    [Test]
    public void Test_SortInPattern_EmptyArray_ReturnsEmptyArray()
    {
        // Arrange
        int[] inputArray = new int[] { };
        int[] expectedOutput = new int[] { };

        // Act
        var result = Pattern.SortInPattern(inputArray);

        // Assert
        Assert.AreEqual(expectedOutput, result);
    }

    [Test]
    public void Test_SortInPattern_SingleElementArray_ReturnsSameArray()
    {
        // Arrange
        int[] inputArray = new int[] { 4 };
        int[] expectedOutput = new int[] { 4 };

        // Act
        var result = Pattern.SortInPattern(inputArray);

        // Assert
        Assert.AreEqual(expectedOutput, result);
    }
}
