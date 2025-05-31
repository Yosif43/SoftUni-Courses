using NUnit.Framework;

namespace TestApp.Tests
{
    public class HashTagCheckerTests
    {
        [Test]
        public void Test_GetHashTags_ValidTextWithOneHashTag_ReturnMessageForOneHashTags()
        {
            // Arrange
            string input = "This is a test #tag.";
            string expected = "Only one! You know exactly what you #tag.";

            // Act
            string result = HashTagChecker.GetHashTags(input);

            // Assert
            Assert.AreEqual(expected, result);
        }

        [Test]
        public void Test_GetHashTags_ValidText_ReturnMessageForEvenHashTags()
        {
            //Arrange
            string input = "This is a test with even #tag1 and #tag2.";
            string expected = "The text contains an even number of #tags (2 in total).";

            // Act
            string result = HashTagChecker.GetHashTags(input);

            // Assert
            Assert.AreEqual(expected, result);
        }

        [Test]
        public void Test_GetHashTags_ValidText_ReturnMessageForOddHashTags()
        {
            // Arrange
            string input = "This is a test with odd #tag1, #tag2, and #tag3.";
            string expected = "The text contains an odd number of #tags (3 in total).";

            // Act
            string result = HashTagChecker.GetHashTags(input);

            // Assert
            Assert.AreEqual(expected, result);
        }

        [Test]
        public void Test_GetHashTags_NullOrEmptyText_ReturnsErrorMessage()
        {
            // Arrange
            string input = "";
            string expected = "No content...";

            // Act
            string result = HashTagChecker.GetHashTags(input);

            // Assert
            Assert.AreEqual(expected, result);
        }

        [Test]
        public void Test_GetHashTags_TestWithoutHashTags_ReturnsErrorMessage()
        {
            // Arrange
            string input = "This is a test without hash tags.";
            string expected = "The text does not contain #tags.";

            // Act
            string result = HashTagChecker.GetHashTags(input);

            // Assert
            Assert.AreEqual(expected, result);
        }
    }
}

