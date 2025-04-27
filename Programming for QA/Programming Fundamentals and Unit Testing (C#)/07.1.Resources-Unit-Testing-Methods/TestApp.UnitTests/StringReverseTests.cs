using NUnit.Framework;

namespace TestApp.UnitTests;

public class StringReverseTests
{
    // TODO: finish test
    [Test]
    public void Test_Reverse_WhenGivenEmptyString_ReturnsEmptyString()
    {
        // Arrange
        string emptyString = string.Empty;
        // Act
        string actualResult = StringReverse.Reverse(emptyString);

        // Assert
        Assert.AreEqual(string.Empty, actualResult);
    }

    [Test]
    public void Test_Reverse_WhenGivenSingleCharacterString_ReturnsSameCharacter()
    {
        string letter = "y";
        string actualResult = StringReverse.Reverse(letter);
        Assert.AreEqual(letter, actualResult);
    }

    [Test]
    public void Test_Reverse_WhenGivenNormalString_ReturnsReversedString()
    {
        string text = "yosko";
        string actualResult = StringReverse.Reverse(text);
        string expectedResult = "oksoy";
        Assert.AreEqual(expectedResult, actualResult);
    }
}
