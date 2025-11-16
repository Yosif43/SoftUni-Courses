using NUnit.Framework;

using System;
using System.Collections.Generic;
using System.Text;

namespace TestApp.Tests;

public class GroupingTests
{
    // TODO: finish test
    [Test]
    public void Test_GroupNumbers_WithEmptyList_ShouldReturnEmptyString()
    {
        // Arrange
        List<int> input = new List<int>();

        // Act
        string result = Grouping.GroupNumbers(input);

        // Assert
        Assert.That(result, Is.Empty);
    }

    [Test]
    public void Test_GroupNumbers_WithEvenAndOddNumbers_ShouldReturnGroupedString()
    {
        // Arrange
        List<int> input = new List<int>() { 1, 2, 3, 4, 5, 6 };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Odd numbers: 1, 3, 5");
        sb.AppendLine("Even numbers: 2, 4, 6");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Grouping.GroupNumbers(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));

    }

    [Test]
    public void Test_GroupNumbers_WithOnlyEvenNumbers_ShouldReturnGroupedString()
    {
        // Arrange
        List<int> input = new List<int>() { 10, 0, 4 };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Even numbers: 10, 0, 4");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Grouping.GroupNumbers(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));

    }

    [Test]
    public void Test_GroupNumbers_WithOnlyOddNumbers_ShouldReturnGroupedString()
    {
        // Arrange
        List<int> input = new List<int>() { 1, 13, 27 };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Odd numbers: 1, 13, 27");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Grouping.GroupNumbers(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));

    }

    [Test]
    public void Test_GroupNumbers_WithNegativeNumbers_ShouldReturnGroupedString()
    {
        // Arrange
        List<int> input = new List<int>() { -2, -4, -5, -3 };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Even numbers: -2, -4");
        sb.AppendLine("Odd numbers: -5, -3");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Grouping.GroupNumbers(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
