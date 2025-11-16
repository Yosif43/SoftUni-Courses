using NUnit.Framework;

using System;
using System.Collections.Generic;
using System.Text;

namespace TestApp.Tests;

public class CountCharactersTests
{
    [Test]
    public void Test_Count_WithEmptyList_ShouldReturnEmptyString()
    {
        // Arrange
        List<string> input = new();

        // Act
        string result = CountCharacters.Count(input);

        // Assert
        Assert.That(result, Is.Empty);
    }

    [Test]
    public void Test_Count_WithNoCharacters_ShouldReturnEmptyString()
    {
        // Arrange
        List<string> input = new List<string>() { "" };

        // Act
        string result = CountCharacters.Count(input);

        // Assert
        Assert.That(result, Is.Empty);
    }

    [Test]
    public void Test_Count_WithSingleCharacter_ShouldReturnCountString()
    {
        // Arrange
        List<string> input = new List<string>() { "a" };
        string expectedValue = "a -> 1";

        // Act
        string result = CountCharacters.Count(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedValue));
    }

    [Test]
    public void Test_Count_WithMultipleCharacters_ShouldReturnCountString()
    {
        // Arrange
        List<string> input = new List<string>() { "stoyan", "shopov" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("s -> 2");
        sb.AppendLine("t -> 1");
        sb.AppendLine("o -> 3");
        sb.AppendLine("y -> 1");
        sb.AppendLine("a -> 1");
        sb.AppendLine("n -> 1");
        sb.AppendLine("h -> 1");
        sb.AppendLine("p -> 1");
        sb.AppendLine("v -> 1");
        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = CountCharacters.Count(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Count_WithSpecialCharacters_ShouldReturnCountString()
    {
        // Arrange
        List<string> input = new List<string>() { "a", "bc", "bca", "", "\"" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("a -> 2");
        sb.AppendLine("b -> 2");
        sb.AppendLine("c -> 2");
        sb.AppendLine("\" -> 1");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = CountCharacters.Count(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
