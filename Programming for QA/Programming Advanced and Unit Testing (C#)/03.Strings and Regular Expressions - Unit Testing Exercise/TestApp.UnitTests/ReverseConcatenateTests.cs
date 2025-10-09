using NUnit.Framework;

using System;
using System.Linq;

namespace TestApp.UnitTests;

public class ReverseConcatenateTests
{

    [TestCase(new string[] { }, "")]
    [TestCase(new string[] { "" }, "")]
    [TestCase(new string[] { "yosko" }, "yosko")]
    [TestCase(new string[] { "Razlog", "Sofia", "Varna" }, "VarnaSofiaRazlog")]
    [TestCase(new string[] { null }, "")]
    [TestCase(null, "")]
    [TestCase(new string[] { "" }, "")]

    [TestCase(new string[] { "Ivan Shopov", "Ilko Kirilov", "Some More Words", "To be Added" }, "To be AddedSome More WordsIlko KirilovIvan Shopov")]
    public void Test_ReverseAndConcatenateStrings_EmptyInput_ReturnsEmptyString(
        string[] input,
        string expectedResult)
    {
        // Act
        string result = ReverseConcatenate.ReverseAndConcatenateStrings(input);

        // Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}