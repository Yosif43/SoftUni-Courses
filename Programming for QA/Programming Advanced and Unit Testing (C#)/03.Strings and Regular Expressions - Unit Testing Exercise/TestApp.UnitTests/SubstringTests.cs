using NUnit.Framework;

namespace TestApp.UnitTests;

public class SubstringTests
{
    // TODO: finish the test
    [Test]
    public void Test_RemoveOccurrences_RemovesSubstringFromMiddle()
    {
        // Arrange
        string toRemove = "fox";
        string input = "The quick brown fox jumps over the lazy dog";

        // Act
        string result = Substring.RemoveOccurrences(toRemove, input);
        // Assert
        string expectedResult = "The quick brown jumps over the lazy dog";
        Assert.AreEqual(expectedResult, result);

    }

    [Test]
    public void Test_RemoveOccurrences_RemovesSubstringFromStart()
    {
        // Arrange
        string toRemove = "The quick";
        string input = "The quick brown fox jumps over the lazy dog";

        // Act
        string result = Substring.RemoveOccurrences(toRemove, input);
        // Assert
        string expectedResult = "brown fox jumps over the lazy dog";
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Test_RemoveOccurrences_RemovesSubstringFromEnd()
    {
        // Arrange
        string toRemove = "lazy dog";
        string input = "The quick brown fox jumps over the lazy dog";

        // Act
        string result = Substring.RemoveOccurrences(toRemove, input);
        // Assert
        string expectedResult = "The quick brown fox jumps over the";
        Assert.AreEqual(expectedResult, result);
    }

    [Test]
    public void Test_RemoveOccurrences_RemovesAllOccurrences()
    {
        // Arrange
        string toRemove = "The";
        string input = "The quick brown fox jumps over the lazy dog";

        // Act
        string result = Substring.RemoveOccurrences(toRemove, input);

        // Assert
        string expectedResult = "quick brown fox jumps over lazy dog";
        Assert.AreEqual(expectedResult, result);
    }
}
