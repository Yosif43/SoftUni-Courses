using NUnit.Framework;
using System;

namespace TestApp.Tests;

public class ExtractFileTests
{
    [Test]
    public void Test_GetFile_NullPath_ThrowsArgumentNullException()
    {
        // Arrange
        string? nullPath = null;
        //Act

        //Assert
        Assert.Throws<ArgumentNullException>(() =>
        {
            ExtractFile.GetFile(nullPath);
        });
    }

    [Test]
    public void Test_GetFile_EmptyPath_ThrowsArgumentNullException()
    {
        // Arrange
        string emptyPath = string.Empty;
        //Act

        //Assert
        Assert.Throws<ArgumentNullException>(() =>
        {
            ExtractFile.GetFile(emptyPath);
        });
    }

    [Test]
    public void Test_GetFile_ValidPath_ReturnsFileNameAndExtension()
    {
        // Arrange
        string validPath = @"C:\Users\Yoo\Desktop\03-Extract-File-Resources\ExamPreparation.sln";
        string expectedResult = "File name: ExamPreparation\nFile extension: sln";
        //Act
        string actualResult = ExtractFile.GetFile(validPath);
        //Assert
        Assert.AreEqual(expectedResult, actualResult);

    }

    [Test]
    public void Test_GetFile_PathWithNoExtension_ReturnsFileNameOnly()
    {
        // Arrange
        string validPath = @"C:\Users\Yoo\Desktop\03-Extract-File-Resources\ExamPreparation";
        string expectedResult = $"File name: ExamPreparation";
        //Act
        string actualResult = ExtractFile.GetFile(validPath);
        //Assert
        Assert.AreEqual (expectedResult, actualResult);
    }

    [Test]
    public void Test_GetFile_PathWithSpecialCharacters_ReturnsFileNameAndExtension()
    {
        // Arrange
        string validPathWithSpecialCharacters = @"C:\Users\Yoo\Desktop\03-Extract-File-Resources\readMe.pdf.txt";
        string expectedResult = "File name: readMe\nFile extension: pdf";
        //Act
        string actualResult = ExtractFile.GetFile(validPathWithSpecialCharacters);
        //Assert
        Assert.AreEqual (expectedResult, actualResult);
    }
}
