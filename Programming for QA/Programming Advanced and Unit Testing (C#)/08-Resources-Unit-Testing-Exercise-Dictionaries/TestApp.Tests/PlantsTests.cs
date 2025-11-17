using NUnit.Framework;

using System;
using System.Numerics;
using System.Text;

namespace TestApp.Tests;

public class PlantsTests
{
    //Input
    //["abc", "ccc", "rulz", "cost", "a"]

    //Output
    //Plants with 1 letters:
    //a
    //Plants with 3 letters:
    //abc
    //ccc
    //Plants with 4 letters:
    //rulz
    //cost

    [Test]
    public void Test_GetFastestGrowing_WithEmptyArray_ShouldReturnEmptyString()
    {
        //Arrange
        string[] input = new string[0];

        //Act
        string result = Plants.GetFastestGrowing(input);

        //Assert
        Assert.That(result, Is.Empty);
    }

    // TODO: finish test
    [Test]
    public void Test_GetFastestGrowing_WithSinglePlant_ShouldReturnPlant()
    {
        //Arrange
        string[] input = new string[] { "Jivko" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Plants with 5 letters:");
        sb.AppendLine("Jivko");
        string expectedResult = sb.ToString().TrimEnd();

        //Act
        string result = Plants.GetFastestGrowing(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_GetFastestGrowing_WithMultiplePlants_ShouldReturnGroupedPlants()
    {
        //Arrange
        string[] input = new string[] { "Jivko", "Ivo", "Stoyan" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Plants with 3 letters:");
        sb.AppendLine("Ivo");
        sb.AppendLine("Plants with 5 letters:");
        sb.AppendLine("Jivko");
        sb.AppendLine("Plants with 6 letters:");
        sb.AppendLine("Stoyan");
        string expectedResult = sb.ToString().TrimEnd();

        //Act
        string result = Plants.GetFastestGrowing(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }

    [Test]
    public void Test_GetFastestGrowing_WithMixedCasePlants_ShouldBeCaseInsensitive()
    {
        //Arrange
        string[] input = new string[] { "JiVKo", "IvO", "Stoyan", "Pesho", "Iva", "StoyNN" };

        StringBuilder sb = new StringBuilder();
        sb.AppendLine("Plants with 3 letters:");
        sb.AppendLine("IvO");
        sb.AppendLine("Iva");
        sb.AppendLine("Plants with 5 letters:");
        sb.AppendLine("JiVKo");
        sb.AppendLine("Pesho");
        sb.AppendLine("Plants with 6 letters:");
        sb.AppendLine("Stoyan");
        sb.AppendLine("StoyNN");
        string expectedResult = sb.ToString().TrimEnd();

        //Act
        string result = Plants.GetFastestGrowing(input);

        //Assert
        Assert.That(result, Is.EqualTo(expectedResult));
    }
}
