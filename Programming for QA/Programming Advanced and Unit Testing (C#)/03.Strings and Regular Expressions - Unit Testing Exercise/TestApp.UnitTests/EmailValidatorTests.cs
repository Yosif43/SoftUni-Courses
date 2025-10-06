using NUnit.Framework;

namespace TestApp.UnitTests;

public class EmailValidatorTests
{
    [TestCase("stoyanshopov032@gmail.com")]
    [TestCase("stoyan.shopov@gmail.com")]
    [TestCase("stoyan_shopov@gmail.com")]
    [TestCase("stoyan%shopov@gmail.com")]
    [TestCase("stoyan+shopov@gmail.com")]
    [TestCase("stoyan-shopov@gmail.com")]
    [TestCase("stoyan-shopov@gmail123.com")]
    [TestCase("stoyan-shopov@gmail-123.com")]
    [TestCase("stoyan-shopov@gmail.123.com")]
    public void Test_ValidEmails_ReturnsTrue(string email)
    {
        // Arrange

        // Act
        bool result = EmailValidator.IsValidEmail(email);

        // Assert
        Assert.That(result, Is.True);
    }

    [TestCase("stoyanshopov032@gmailcom")]
    [TestCase("stoyan.shopovgmail.com")]
    [TestCase("stoyan_shopov@@gmail.com")]
    [TestCase("@gmail.com")]
    [TestCase("gmail.com")]
    [TestCase("stoyan-shopovgmailcom")]
    [TestCase("")]
    [TestCase("1")]

    public void Test_InvalidEmails_ReturnsFalse(string email)
    {
        // Arrange

        // Act
        bool result = EmailValidator.IsValidEmail(email);
        
        // Assert
        Assert.That(result, Is.False);
    }
}
