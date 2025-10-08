using NUnit.Framework;

namespace TestApp.UnitTests;

public class MatchPhoneNumbersTests
{
    
    [TestCase("+359-2-124-5678, +359 2 986 5432, +359-2-555-5555", "+359-2-124-5678, +359 2 986 5432, +359-2-555-5555")]
    [TestCase("359-2-124-5678, +159 2 986 5432, +351-2-555-5555, +359 2-124-5678, +359-1-124-5678," +
        "+359-2-24-5678, +359-2-124-56781", "")]
    [TestCase("", "")]
    [TestCase("+359-2-666-1234, +359 21 666 1234, +359 2 444 1236", "+359-2-666-1234, +359 2 444 1236")]
    [TestCase("+359-2-666-1234, +359 21 666 1234, +359 2 444 1236, +351-2-555-5555, +359 2-124-5678", "+359-2-666-1234, +359 2 444 1236")]

    public void Test_Match_ValidPhoneNumbers_ReturnsMatchedNumbers(string input, string expectedResult)
    {
        // Act
        string result = MatchPhoneNumbers.Match(input);
        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
