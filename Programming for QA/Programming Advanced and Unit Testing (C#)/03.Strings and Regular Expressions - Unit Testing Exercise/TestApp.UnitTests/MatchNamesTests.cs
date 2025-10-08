using NUnit.Framework;

namespace TestApp.UnitTests;

public class MatchNamesTests
{
    [TestCase("John Smith and Alice Johnson", "John Smith Alice Johnson")]
    [TestCase("Stoyan Shopov is here", "Stoyan Shopov")]
    [TestCase("Hello, Nikolay Kostov", "Nikolay Kostov")]
    [TestCase("Hello, Viktor Dakov my frient", "Viktor Dakov")]
    [TestCase("Hello, Viktor my friend", "")]
    [TestCase("Ivaylo", "")]
    [TestCase("ivaylo Kenov", "")]
    [TestCase("ivaylo kenov", "")]
    [TestCase("Ivaylo kenov", "")]
    [TestCase("", "")]
    [TestCase("Stoyan-Shopov", "")]
    [TestCase("Stoyan  Shopov", "")]
    public void Test_Match_ValidNames_ReturnsMatchedNames(string input, string expected)
    {

        // Act
        string result = MatchNames.Match(input);

        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }
}
