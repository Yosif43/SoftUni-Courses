using NUnit.Framework;

using System.Collections.Generic;

namespace TestApp.UnitTests;

public class MatchUrlsTests
{
    [TestCase("https://softuni.bg", new string[] { "https://softuni.bg" })]
    [TestCase("https://www.softuni.bg", new string[] { "https://www.softuni.bg" })]
    [TestCase("http://softuni.bg", new string[] { "http://softuni.bg" })]
    [TestCase("http://www.softuni.bg", new string[] { "http://www.softuni.bg" })]
    [TestCase("https://softuni.bg?id=1484", new string[] { "https://softuni.bg?id=1484" })]
    [TestCase("Test one", new string[] { })]
    [TestCase("https://softuni.bg https://judge.softuni.org", new string[] { "https://softuni.bg", "https://judge.softuni.org" })]
    
    //[TestCase("https://softuni.bg/blog", new string[] { "https://softuni.bg/blog" })] Bug
    public void Test_ExtractUrls_EmptyText_ReturnsEmptyList(string input, string[] expected)
    {

        // Act
        List<string> result = MatchUrls.ExtractUrls(input);
        // Assert
        CollectionAssert.AreEqual(expected, result);
    }
}
