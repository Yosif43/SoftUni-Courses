using NUnit.Framework;

namespace TestApp.UnitTests;

public class GradesTests
{
    [TestCase(2, "Fail")]
    [TestCase(2.50, "Fail")]
    [TestCase(3, "Average")]
    [TestCase(3.40, "Average")]
    [TestCase(3.50, "Good")]
    [TestCase(3.80, "Good")]
    [TestCase(4, "Very Good")]
    [TestCase(4.30, "Very Good")]
    [TestCase(4.50, "Excellent")]
    [TestCase(5, "Excellent")]
    [TestCase(6, "Invalid!")]
    [TestCase(-1, "Invalid!")]
    [TestCase(0, "Invalid!")]
    
    public void Test_GradeAsWords_ReturnsCorrectString(double grade, string expected)
    {
        // Arrange
         
        // Act
        string actual = Grades.GradeAsWords(grade);

        // Assert
        Assert.AreEqual(expected, actual);
    }

    [TestCase(1.99, "Invalid!")]
    [TestCase(2.99, "Fail")]
    [TestCase(3, "Average")]
    [TestCase(3.49, "Average")]
    [TestCase(3.50, "Good")]
    [TestCase(3.99, "Good")]
    [TestCase(4, "Very Good")]
    [TestCase(4.49, "Very Good")]
    [TestCase(4.50, "Excellent")]
    [TestCase(5, "Excellent")]
    [TestCase(5.01, "Invalid!")]
    public void Test_GradeAsWords_ReturnsCorrectString_EdgeCases(double grade, string expected)
    {
        // Arrange

        // Act
        string actual = Grades.GradeAsWords(grade);

        // Assert
        Assert.AreEqual(expected, actual);
    }
}
