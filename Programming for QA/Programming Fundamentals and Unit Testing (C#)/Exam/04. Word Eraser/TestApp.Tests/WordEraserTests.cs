using System;
using System.Collections.Generic;
using NUnit.Framework;

namespace TestApp.Tests;

public class WordEraserTests
{
    [Test]
    public void Test_Erase_EmptyWordsList_ShouldReturnEmptyString()
    {
        // Arrange
        var wordEraser = new WordEraser();
        var words = new List<string>();

        // Act
        var result = wordEraser.Erase(words, "test");

        // Assert
        Assert.IsEmpty(result);
    }

    [Test]
    public void Test_Erase_NullWordsList_ShouldReturnEmptyString()
    {
        // Arrange
        var wordEraser = new WordEraser();
        List<string>? words = null;

        // Act
        var result = wordEraser.Erase(words, "test");

        // Assert
        Assert.IsEmpty(result);
    }

    [Test]
    public void Test_Erase_NullOrEmptyWordToErase_ShouldReturnStringOfGivenWordsList()
    {
        // Arrange
        var wordEraser = new WordEraser();
        var words = new List<string> { "hello", "world" };

        // Act
        var resultWithNull = wordEraser.Erase(words, null);
        var resultWithEmpty = wordEraser.Erase(words, string.Empty);

        // Assert
        Assert.AreEqual("hello world", resultWithNull);
        Assert.AreEqual("hello world", resultWithEmpty);
    }

    [Test]
    public void Test_Erase_ValidInput_ShouldReturnEmptyString_WhenAllWordsMatchedTheWordToErase()
    {
        // Arrange
        var wordEraser = new WordEraser();
        var words = new List<string> { "test", "test", "test" };

        // Act
        var result = wordEraser.Erase(words, "test");

        // Assert
        Assert.IsEmpty(result);
    }

    [Test]
    public void Test_Erase_ValidInput_ShouldReturnStringWithoutErasedWords_WhenFewOfWordsMatchedWordToArese()
    {
        // Arrange
        var wordEraser = new WordEraser();
        var words = new List<string> { "hello", "test", "world", "test" };

        // Act
        var result = wordEraser.Erase(words, "test");

        // Assert
        Assert.AreEqual("hello world", result);
    }
}

