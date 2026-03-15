using System;
using System.Collections.Generic;

using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class GradesTests
{
    [Test]
    public void Test_GetBestStudents_ReturnsBestThreeStudents()
    {
        // Arange
        Dictionary<string, int> gradesDictionary = new()
        {
            { "Ivan", 4 },
            { "Yosif", 6 },
            { "Goshko", 5 },
            { "Nadejda", 6 }
        };
        // Act
        string actualResult = Grades.GetBestStudents(gradesDictionary);
        string expectedResult = $"Nadejda with average grade 6.00{Environment.NewLine}" +
            $"Yosif with average grade 6.00{Environment.NewLine}" +
            $"Goshko with average grade 5.00";
        // Assert
        Assert.That(expectedResult, Is.EqualTo(actualResult));
    }

    [Test]
    public void Test_GetBestStudents_EmptyGrades_ReturnsEmptyString()
    {
        // Arange
        Dictionary<string, int> gradesDictionary = new()
        {
           
        };
        // Act
        string actualResult = Grades.GetBestStudents(gradesDictionary);
        string expectedResult = "";
        // Assert
        Assert.That(expectedResult, Is.EqualTo(actualResult));
    }

    [Test]
    public void Test_GetBestStudents_LessThanThreeStudents_ReturnsAllStudents()
    {
        // Arange
        Dictionary<string, int> gradesDictionary = new()
        {
            { "Nadejda", 6 },
            { "Yosif", 6 },
           
        };
        // Act
        string actualResult = Grades.GetBestStudents(gradesDictionary);
        string expectedResult = $"Nadejda with average grade 6.00{Environment.NewLine}" +
            $"Yosif with average grade 6.00";
        // Assert
        Assert.That(expectedResult, Is.EqualTo(actualResult));
    }

    [Test]
    public void Test_GetBestStudents_SameGrade_ReturnsInAlphabeticalOrder()
    {
        // Arange
        Dictionary<string, int> gradesDictionary = new()
        {
            { "Ivan", 6 },
            { "Yosif", 6 },
            { "Nadejda", 6 }
        };
        // Act
        string actualResult = Grades.GetBestStudents(gradesDictionary);
        string expectedResult = $"Ivan with average grade 6.00{Environment.NewLine}" +
            $"Nadejda with average grade 6.00{Environment.NewLine}" +
            $"Yosif with average grade 6.00";
        // Assert
        Assert.That(expectedResult, Is.EqualTo(actualResult));
    }
}
