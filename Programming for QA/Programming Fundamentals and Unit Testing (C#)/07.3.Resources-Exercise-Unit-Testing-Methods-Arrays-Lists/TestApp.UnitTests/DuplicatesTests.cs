using NUnit.Framework;

using System;
using System.Linq;

namespace TestApp.UnitTests;

public class DuplicatesTests
{
    // TODO: finish test
    [Test]
    public void Test_RemoveDuplicates_EmptyArray_ReturnsEmptyArray()
    {
        // Arrange
        int[] numbers = Array.Empty<int>();

        // Act
        var result = Duplicates.RemoveDuplicates(numbers);

        // Assert
        Assert.IsEmpty(result);
    }

    // TODO: finish test
    [Test]
    public void Test_RemoveDuplicates_NoDuplicates_ReturnsOriginalArray()
    {
        // Arrange
        int[] numbers = { 1, 2, 3, 4, 5 };

        // Act
        var result = Duplicates.RemoveDuplicates(numbers);

        // Assert
        Assert.That(result.OrderBy(n => n), Is.EqualTo(numbers.OrderBy(n => n)));

    }

    [Test]
    public void Test_RemoveDuplicates_SomeDuplicates_ReturnsUniqueArray()
    {
        // Arrange
        int[] numbers = { 1, 2, 2, 3, 4, 4, 5 };

        // Act
        var result = Duplicates.RemoveDuplicates(numbers);

        // Assert
        int[] expected = { 1, 2, 3, 4, 5 };
        Assert.That(result.OrderBy(n => n), Is.EqualTo(expected));
    }

    [Test]
    public void Test_RemoveDuplicates_AllDuplicates_ReturnsSingleElementArray()
    {
        // Arrange
        int[] numbers = { 1, 1, 1, 1 };

        // Act
        var result = Duplicates.RemoveDuplicates(numbers);

        // Assert
        int[] expected = { 1 };
        Assert.That(result, Is.EqualTo(expected));
    }
}
