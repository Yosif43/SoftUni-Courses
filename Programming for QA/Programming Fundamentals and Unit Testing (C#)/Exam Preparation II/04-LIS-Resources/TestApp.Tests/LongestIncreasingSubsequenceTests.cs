using NUnit.Framework;
using System;

namespace TestApp.Tests;

public class LongestIncreasingSubsequenceTests
{
    [Test]
    public void Test_GetLis_NullArray_ThrowsArgumentNullException()
    {
        // Arrange
        int[]? arr = null;

        // Act & Assert
        Assert.Throws<ArgumentNullException>(() => LongestIncreasingSubsequence.GetLis(arr));

    }

    [Test]
    public void Test_GetLis_EmptyArray_ReturnsEmptyString()
    {
        // Arrange
        int[] arr = new int[0];

        // Act
        var result = LongestIncreasingSubsequence.GetLis(arr);

        // Assert
        Assert.AreEqual(string.Empty, result);
    }

    [Test]
    public void Test_GetLis_SingleElementArray_ReturnsElement()
    {
        // Arrange
        int[] arr = { 5 };

        // Act
        var result = LongestIncreasingSubsequence.GetLis(arr);

        // Assert
        Assert.AreEqual("5", result);
    }

    [Test]
    public void Test_GetLis_UnsortedArray_ReturnsLongestIncreasingSubsequence()
    {
        // Arrange
        int[] arr = { 10, 22, 9, 33, 21, 50, 41, 60, 80 };

        // Act
        var result = LongestIncreasingSubsequence.GetLis(arr);

        // Assert
        // The LIS for the given array is 10, 22, 33, 50, 60, 80
        Assert.AreEqual("10 22 33 50 60 80", result);
    }

    [Test]
    public void Test_GetLis_SortedArray_ReturnsItself()
    {
        // Arrange
        int[] arr = { 1, 2, 3, 4, 5, 6 };

        // Act
        var result = LongestIncreasingSubsequence.GetLis(arr);

        // Assert
        Assert.AreEqual("1 2 3 4 5 6", result);
    }
}
