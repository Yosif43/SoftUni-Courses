using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class TextFilterTests
{
    // TODO: finish the test
    [Test]
    public void Test_Filter_WhenNoBannedWords_ShouldReturnOriginalText()
    {
        // Arrange
        string[] bannedWords = new string[] { };
        string text = "Lorem ipsum etc.";
        string expectedResult = "Lorem ipsum etc.";

        // Act
        string actualResult = TextFilter.Filter(bannedWords, text);
        // Assert
        Assert.That(actualResult, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Filter_WhenBannedWordExists_ShouldReplaceBannedWordWithAsterisks()
    {
        // Arrange
        string[] bannedWords = new string[] { "Lorem" };
        string text = "Lorem ipsum etc.";
        string expectedResult = "***** ipsum etc.";
        // Act
        string actualResult = TextFilter.Filter(bannedWords, text);
        // Assert
        Assert.That(actualResult, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Filter_WhenBannedWordsAreEmpty_ShouldReturnOriginalText()
    {
        // Arrange
        string[] bannedWords = new string[] { };
        string text = "Lorem ipsum etc.";
        string expectedResult = "Lorem ipsum etc.";
        // Act
        string actualResult = TextFilter.Filter(bannedWords, text);
        // Assert
        Assert.That(actualResult, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_Filter_WhenBannedWordsContainWhitespace_ShouldReplaceBannedWord()
    {
        // Arrange
        string[] bannedWords = new string[] { "Lorem ipsum" };
        string text = "Lorem ipsum etc.";
        string expectedResult = "*********** etc.";
        // Act
        string actualResult = TextFilter.Filter(bannedWords, text);
        // Assert
        Assert.That(actualResult, Is.EqualTo(expectedResult));
    }
}
