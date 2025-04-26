using NUnit.Framework;

namespace TestApp.UnitTests;

public class FactorialTests
{
    [Test]
    public void Test_CalculateFactorial_InputZero_ReturnsOne()
    {
        int factorial = 0;
        int actualResult = Factorial.CalculateFactorial(factorial);
        int expectedResult = 1;
        Assert.AreEqual(expectedResult, actualResult);
    }

    [Test]
    public void Test_CalculateFactorial_InputPositiveNumber_ReturnsCorrectFactorial()
    {
        int factorial = 5;
        int actualResult = Factorial.CalculateFactorial(factorial);
        int expectedResult = 120;
        Assert.AreEqual(expectedResult, actualResult);
    }
}
