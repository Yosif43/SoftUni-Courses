using NUnit.Framework;

using System.Collections.Generic;

namespace TestApp.UnitTests;

public class GaussTrickTests
{
    [Test]
    public void Test_SumPairs_InputIsEmptyList_ShouldReturnEmptyList()
    {
        // Arrange
        List<int> emptyList = new();

        // Act
        List<int> result = GaussTrick.SumPairs(emptyList);

        // Assert
        CollectionAssert.AreEqual(emptyList, result);
    }

    // TODO: finish the test
    [Test]
    public void Test_SumPairs_InputHasSingleElement_ShouldReturnSameElement()
    {
        // Arrange
        List<int> singleElementList = new List<int> { 5 };

        // Act
        List<int> result = GaussTrick.SumPairs(singleElementList);

        // Assert
        CollectionAssert.AreEqual(singleElementList, result);
    }

    // TODO: finish the test
    [Test]
    public void Test_SumPairs_InputHasEvenCountElements_ShouldReturnSumPairs()
    {
        // Arrange
        List<int> evenList = new List<int> { 1, 2, 3, 4 };
        List<int> expected = new List<int> { 5, 5 };

        // Act
        List<int> result = GaussTrick.SumPairs(evenList);

        // Assert
        CollectionAssert.AreEqual(expected, result);
    }

    [Test]
    public void Test_SumPairs_InputHasOddCountElements_ShouldReturnWithMiddleElement()
    {
        // Arrange
        List<int> oddList = new List<int> { 1, 2, 3, 4, 5 };
        List<int> expected = new List<int> { 6, 6, 3 };

        // Act
        List<int> result = GaussTrick.SumPairs(oddList);

        // Assert
        CollectionAssert.AreEqual(expected, result);
    }

    [Test]
    public void Test_SumPairs_InputHasLargeEvenCountElements_ShouldReturnSumPairs()
    {
        // Arrange
        List<int> largeEvenList = new List<int> { 10, 20, 30, 40, 50, 60 };
        List<int> expected = new List<int> { 70, 70, 70 };

        // Act
        List<int> result = GaussTrick.SumPairs(largeEvenList);

        // Assert
        CollectionAssert.AreEqual(expected, result);
    }

    [Test]
    public void Test_SumPairs_InputHasLargeOddCountElements_ShouldReturnWithMiddleElement()
    {
        // Arrange
        List<int> largeOddList = new List<int> { 10, 20, 30, 40, 50, 60, 70 };
        List<int> expected = new List<int> { 80, 80, 80, 40 };

        // Act
        List<int> result = GaussTrick.SumPairs(largeOddList);

        // Assert
        CollectionAssert.AreEqual(expected, result);
    }
}
