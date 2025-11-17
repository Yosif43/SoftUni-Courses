using NUnit.Framework;

using System;

namespace TestApp.Tests;

public class OddOccurrencesTests
{
    [Test]
    public void Test_FindOdd_WithEmptyArray_ShouldReturnEmptyString()
    {
        //Arrange
        string[] input = new string[0];

        //Act
        string result = OddOccurrences.FindOdd(input);

        //Assert
        Assert.That(result, Is.Empty);
    }

    // TODO: finish test
    [Test]
    public void Test_FindOdd_WithNoOddOccurrences_ShouldReturnEmptyString()
    {
        //Arrange
        string[] input = new string[] { "sto", "sto", "shop", "shop", "shop", "shop" };

        //Act
        string result = OddOccurrences.FindOdd(input);

        //Assert
        Assert.That(result, Is.Empty);
    }

    [Test]
    public void Test_FindOdd_WithSingleOddOccurrence_ShouldReturnTheOddWord()
    {
        //Arrange
        string[] input = new string[] { "sofia", "plovdiv", "sofia" };
        string expectedResult = "plovdiv";

        //Act
        string result = OddOccurrences.FindOdd(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_FindOdd_WithMultipleOddOccurrences_ShouldReturnAllOddWords()
    {
        //Arrange
        string[] input = new string[] { "varna", "sofia", "plovdiv", "varna", "sofia", "sofia" };
        string expectedResult = "sofia plovdiv";

        //Act
        string result = OddOccurrences.FindOdd(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_FindOdd_WithMixedCaseWords_ShouldBeCaseInsensitive()
    {
        //Arrange
        string[] input = new string[] { "varnA", "Sofia", "PloVdiv", "VarnA", "SOFia", "sofiA" };
        string expectedResult = "sofia plovdiv";

        //Act
        string result = OddOccurrences.FindOdd(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
