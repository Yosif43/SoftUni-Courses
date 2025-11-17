using NUnit.Framework;

using System;
using System.Text;

namespace TestApp.Tests;

public class MinerTests
{
    [Test]
    public void Test_Mine_WithEmptyInput_ShouldReturnEmptyString()
    {
        // Arrange
        string[] input = new string[0];

        // Act
        string result = Miner.Mine(input);

        // Assert
        Assert.That(result, Is.Empty);
    }

    // TODO: finish test
    [Test]
    public void Test_Mine_WithMixedCaseResources_ShouldBeCaseInsensitive()
    {
        // Arrange
        string[] input = new string[] { "SilVer 10", "silver 20" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("silver -> 30");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Miner.Mine(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Mine_WithDifferentResources_ShouldReturnResourceCounts()
    {
        // Arrange
        string[] input = new string[] { "SilVer 10", "GolD 15", "silver 20", "bronZ 3", "gold 1" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("silver -> 30");
        sb.AppendLine("gold -> 16");
        sb.AppendLine("bronz -> 3");

        string expectedResult = sb.ToString().TrimEnd();

        // Act
        string result = Miner.Mine(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
