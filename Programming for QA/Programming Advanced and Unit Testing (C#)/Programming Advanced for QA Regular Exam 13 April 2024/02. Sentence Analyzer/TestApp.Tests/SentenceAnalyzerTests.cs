using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class SentenceAnalyzerTests
{
    [Test]
    public void Test_Analyze_EmptyString_ReturnsEmptyDictionary()
    {
        // Arrange


        // Act
        var result = SentenceAnalyzer.Analyze(string.Empty);

        // Assert
        Assert.That(result, Is.Empty);
    }

    [Test]
    public void Test_Analyze_SingleLetter_ReturnsDictionaryWithSingleLetterEntry()
    {
        // Arrange
        string testInput = "a";

        // Act
        var result = SentenceAnalyzer.Analyze(testInput);

        // Assert
        Assert.That(result.ContainsKey("letters"), Is.True);
        Assert.That(result["letters"], Is.EqualTo(1));
    }

    [Test]
    public void Test_Analyze_SingleDigit_ReturnsDictionaryWithSingleDigitEntry()
    {
        // Arrange
        string testInput = "5";

        // Act
        var result = SentenceAnalyzer.Analyze(testInput);

        // Assert
        Assert.That(result.ContainsKey("digits"), Is.True);
        Assert.That(result["digits"], Is.EqualTo(1));
    }

    [Test]
    public void Test_Analyze_WholeSentence_ReturnsDictionaryWithAllSymbolTypesCount()
    {
        // Arrange
        string testInput = "Hello, world! 123";

        // Act
        var result = SentenceAnalyzer.Analyze(testInput);

        // Assert
        Assert.Multiple(() =>
        {
            Assert.That(result.ContainsKey("letters"), Is.True);
            Assert.That(result["letters"], Is.EqualTo(10));

            Assert.That(result.ContainsKey("digits"), Is.True);
            Assert.That(result["digits"], Is.EqualTo(3));

            Assert.That(result.ContainsKey("special characters"), Is.True);
            Assert.That(result["special characters"], Is.EqualTo(2));

        });
    }
}

