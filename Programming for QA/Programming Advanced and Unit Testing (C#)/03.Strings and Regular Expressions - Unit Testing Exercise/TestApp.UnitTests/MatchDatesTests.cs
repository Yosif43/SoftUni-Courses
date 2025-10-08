using NUnit.Framework;
using System;

namespace TestApp.UnitTests;

public class MatchDatesTests
{
    
    [TestCase("31-Dec-2022", "Day: 31, Month: Dec, Year: 2022")]
    [TestCase("31.Dec.2022", "Day: 31, Month: Dec, Year: 2022")]
    [TestCase("31/Dec/2022", "Day: 31, Month: Dec, Year: 2022")]
    [TestCase("Test", "")]
    [TestCase("31-Dec-2022 13-Jan-2023", "Day: 31, Month: Dec, Year: 2022")]
    [TestCase("", "")]
    [TestCase("31-Dec/2022", "")]
    [TestCase("31-Dec.2022", "")]
    [TestCase("31-De.2022", "")]
    //[TestCase("41.Dec.2022", "")]
    //[TestCase("41.Dec.22", "")] Bug
    [TestCase("0.Dec.2022", "")]
    //[TestCase("31\\Dec\\2022", "Day: 31, Month: Dec, Year: 2022")] Bug
    public void Test_Match_ValidDate_ReturnsExpectedResult(string input, string expected)
    {

        // Act
        string result = MatchDates.Match(input);
        // Assert
        Assert.That(result, Is.EqualTo(expected));
    }

    [Test]
    public void Test_Match_NullInput_ThrowsArgumentException()
    {
        Assert.Throws<ArgumentException>(() => MatchDates.Match(null));
    }
}
