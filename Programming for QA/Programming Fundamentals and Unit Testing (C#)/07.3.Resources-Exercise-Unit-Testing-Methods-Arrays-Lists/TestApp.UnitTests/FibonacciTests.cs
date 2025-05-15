using NUnit.Framework;

namespace TestApp.UnitTests;

public class FibonacciTests
{
    [Test]
    public void Test_CalculateFibonacci_ZeroInput()
    {
        int result = Fibonacci.CalculateFibonacci(0);
        Assert.AreEqual(0, result);
    }


    [Test]
    [TestCase(0, 0)]
    [TestCase(1, 1)]
    [TestCase(2, 1)]
    [TestCase(3, 2)]
    [TestCase(4, 3)]
    [TestCase(5, 5)]
    [TestCase(6, 8)]
    [TestCase(7, 13)]
    [TestCase(8, 21)]
    [TestCase(9, 34)]
    [TestCase(10, 55)]
    [TestCase(11, 89)]
    [TestCase(12, 144)]
    [TestCase(13, 233)]
    [TestCase(14, 377)]
    [TestCase(15, 610)]
    public void Test_CalculateFibonacci_PositiveInput(int input, int expected)
    {
        int result = Fibonacci.CalculateFibonacci(input);
        Assert.AreEqual(expected, result);

    }
}