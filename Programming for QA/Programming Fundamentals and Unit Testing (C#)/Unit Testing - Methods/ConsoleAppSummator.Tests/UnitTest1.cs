namespace ConsoleAppSummator.Tests
{
    [SetUp]   
    
    public void Setup()
    {
        ;
    }

    [TearDown]
    public void TearDown()
    {
        ;
    }

    public class AppSummatorTest
    {

        [Test]
        public void ProgramSumShouldReturnSummedNumbers()
        {
            int sumOfArray = Program.Sum(new int[] { 1, 2, 3 });
            Assert.That(sumOfArray == 6);
            Assert.That(6, Is.EqualTo(sumOfArray));
        }

        [Test]
        public void ProgramSumShouldReturn0IfNothingIsPassed()
        {
            int sumOfArray = Program.Sum(new int[0]);
            Assert.That(sumOfArray == 0);
        }

    }
}