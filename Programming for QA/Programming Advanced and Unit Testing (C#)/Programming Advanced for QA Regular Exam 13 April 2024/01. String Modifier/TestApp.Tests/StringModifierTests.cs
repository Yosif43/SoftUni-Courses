using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class StringModifierTests
{
    [Test]
    public void Test_Modify_EmptyString_ReturnsEmptyString()
    {
        // Arrange
        string input = "";
        string expected = "";

        // Act
        string result = StringModifier.Modify(input);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_Modify_SingleWordWithEvenLength_ReturnsUppperCaseWord()
    {
        // Arrange
        string input = "even";
        string expected = "EVEN";

        // Act
        string result = StringModifier.Modify(input);

        // Assert
        Assert.That(result, Is.EqualTo(expected));

    }

    [Test]
    public void Test_Modify_SingleWordWithOddLength_ReturnsToLowerCaseWord()
    {
        // Arrange
        string input = "oDd";
        string expected = "odd";

        // Act
        string result = StringModifier.Modify(input);

        // Assert
        Assert.That(result, Is.EqualTo(expected));

    }

    [Test]
    public void Test_Modify_MultipleWords_ReturnsModifiedString()
    {
        // Arrange
        string input = "This is a Test";
        string expected = "THIS IS a TEST";

        // Act
        string result = StringModifier.Modify(input);

        // Assert
        Assert.That(result, Is.EqualTo(expected));

    }
}

