using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class StringRotatorTests
{
    [Test]
    public void Test_RotateRight_EmptyString_ReturnsEmptyString()
    {
        // Arrange
        string input = string.Empty;
        int position = 3;
        // Act
        string result = StringRotator.RotateRight(input, position);
        // Assert
        //Assert.AreEqual(input, result);
        Assert.That(result, Is.Empty);


    }

    [Test]
    public void Test_RotateRight_RotateByZeroPositions_ReturnsOriginalString()
    {
        // Arrange
        string input = "abcdef";
        int position = 0;
        string expected = input;
        // Act
        string result = StringRotator.RotateRight(input, position);
        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_RotateRight_RotateByPositivePositions_ReturnsRotatedString()
    {
        // Arrange
        string input = "abcdef";
        int position = 3;
        string expected = "defabc";
        // Act
        string result = StringRotator.RotateRight(input, position);
        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_RotateRight_RotateByNegativePositions_ReturnsRotatedString()
    {
        // Arrange
        string input = "abcdef";
        int position = -2;
        string expected = "efabcd";
        // Act
        string result = StringRotator.RotateRight(input, position);
        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_RotateRight_RotateByMorePositionsThanStringLength_ReturnsRotatedString()
    {
        // Arrange
        string input = "abcdef";
        int position = 8;
        string expected = "efabcd";
        // Act
        string result = StringRotator.RotateRight(input, position);
        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }
}
