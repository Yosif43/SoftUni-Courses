using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class CamelCaseConverterTests
{
    [Test]
    public void Test_ConvertToCamelCase_EmptyString_ReturnsEmptyString()
    {
        // Arange
        string input = string.Empty;
        // Act
        string output = CamelCaseConverter.ConvertToCamelCase(input);
        // Assert
        Assert.That(output, Is.EqualTo(string.Empty));
    }

    [Test]
    public void Test_ConvertToCamelCase_SingleWord_ReturnsLowercaseWord()
    {
        // Arange
        string input = "SoftUni";
        string expected = "softuni";
        // Act
        string output = CamelCaseConverter.ConvertToCamelCase(input);
        // Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_ConvertToCamelCase_MultipleWords_ReturnsCamelCase()
    {
        // Arange
        string input = "first second third";
        string expected = "firstSecondThird";
        // Act
        string output = CamelCaseConverter.ConvertToCamelCase(input);
        // Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_ConvertToCamelCase_MultipleWordsWithMixedCase_ReturnsCamelCase()
    {
        // Arange
        string input = "fiRSt sECond tHIRd";
        string expected = "firstSecondThird";
        // Act
        string output = CamelCaseConverter.ConvertToCamelCase(input);
        // Assert
        Assert.That(output, Is.EqualTo(expected));
    }
}
