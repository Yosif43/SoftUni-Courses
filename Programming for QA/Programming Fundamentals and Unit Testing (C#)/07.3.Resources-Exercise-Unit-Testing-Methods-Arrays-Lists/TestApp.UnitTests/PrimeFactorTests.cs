using NUnit.Framework;

namespace TestApp.UnitTests;

public class PrimeFactorTests
{
    [Test]
    public void Test_FindLargestPrimeFactor_PrimeNumber()
    {
        // Arrange
        long primeNumber = 13;
        long expected = 13;

        // Act
        long actual = PrimeFactor.FindLargestPrimeFactor(primeNumber);

        // Assert
        Assert.AreEqual(expected, actual);

    }

    [Test]
    public void Test_FindLargestPrimeFactor_LargeNumber()
    {
        // Arrange
        long largeNumber = 13195;
        long expected = 29;

        // Act
        long actual = PrimeFactor.FindLargestPrimeFactor(largeNumber);

        // Assert
        Assert.AreEqual(expected, actual);

    }
}
