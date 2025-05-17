using NUnit.Framework;

using System.Collections.Generic;

namespace TestApp.UnitTests;

public class PalindromeTests
{
    // TODO: finish test
    [Test]
    public void Test_IsPalindrome_ValidPalindrome_ReturnsTrue()
    {
        // Arrange
        List<string> words = new List<string> { "level", "radar", "civic" };

        // Act
        bool result = Palindrome.IsPalindrome(words);

        // Assert
        Assert.AreEqual(true, result);
    }

    // TODO: finish test
    [Test]
    public void Test_IsPalindrome_EmptyList_ReturnsTrue()
    {
        // Arrange
        List<string> words = new List<string>();

        // Act
        bool result = Palindrome.IsPalindrome(words);

        // Assert
        Assert.AreEqual(true, result);
    }

    [Test]
    public void Test_IsPalindrome_SingleWord_ReturnsTrue()
    {
        // Arrange
        List<string> words = new List<string> { "noon" };

        // Act
        bool result = Palindrome.IsPalindrome(words);

        // Assert
        Assert.AreEqual(true, result);
    }

    [Test]
    public void Test_IsPalindrome_NonPalindrome_ReturnsFalse()
    {
        // Arrange
        List<string> words = new List<string> { "apple", "banana", "carrot" };

        // Act
        bool result = Palindrome.IsPalindrome(words);

        // Assert
        Assert.AreEqual(false, result);
    }

    [Test]
    public void Test_IsPalindrome_MixedCasePalindrome_ReturnsTrue()
    {
        // Arrange
        List<string> words = new List<string> { "Racecar", "Level", "Civic" };

        // Act
        bool result = Palindrome.IsPalindrome(words);

        // Assert
        Assert.AreEqual(true, result);
    }
}
