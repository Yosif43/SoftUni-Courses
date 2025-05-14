using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class FakeTests
{
    [Test]
    public void Test_RemoveStringNumbers_RemovesDigitsFromCharArray()
    {
        // Arrange
        char[] input = { 'a', '1', 'b', '2', 'c' };
        char[] expected = { 'a', 'b', 'c' };

        // Act
        var result = Fake.RemoveStringNumbers(input);

        // Assert
        Assert.AreEqual(expected, result);
    }

    [Test]
    public void Test_RemoveStringNumbers_NoDigitsInInput_ReturnsSameArray()
    {
        // Arrange
        char[] input = { 'a', 'b', 'c' };
        char[] expected = { 'a', 'b', 'c' };

        // Act
        var result = Fake.RemoveStringNumbers(input);

        // Assert
        Assert.AreEqual(expected, result);
    }

    [Test]
    public void Test_RemoveStringNumbers_EmptyArray_ReturnsEmptyArray()
    {
        // Arrange
        char[] input = { };
        char[] expected = { };

        // Act
        var result = Fake.RemoveStringNumbers(input);

        // Assert
        Assert.AreEqual(expected, result);
    }
}
