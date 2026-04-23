using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class BankAccountTests
{
    [Test]
    public void Test_Constructor_InitialBalanceIsSet()
    {
        // Arange
        double initialAmount = 1000;
        // Act
        BankAccount account = new BankAccount(initialAmount);

        // Assert
        Assert.That(account.Balance, Is.EqualTo(initialAmount));
    }

    [Test]
    public void Test_Deposit_PositiveAmount_IncreasesBalance()
    {
        // Arange
        double initialAmount = 1000;
        double moreMoney = 500;
        double expectedMoney = 1500;
        // Act
        BankAccount account = new BankAccount(initialAmount);
        account.Deposit(moreMoney);
        // Assert
        Assert.That(account.Balance, Is.EqualTo(expectedMoney));
    }

    [Test]
    public void Test_Deposit_NegativeAmount_ThrowsArgumentException()
    {
        // Arange
        double initialAmount = 1000;
        double moreMoney = -500;
        
        // Act
        BankAccount account = new BankAccount(initialAmount);
        
        // Assert
        Assert.That(() => account.Deposit(moreMoney), Throws.ArgumentException);
    }

    [Test]
    public void Test_Withdraw_ValidAmount_DecreasesBalance()
    {
        // Arange
        double initialAmount = 1000;
        double getMoney = 400;
        double expectedMoney = 600;
        // Act
        BankAccount account = new BankAccount(initialAmount);
        account.Withdraw(getMoney);
        // Assert
        Assert.That(account.Balance, Is.EqualTo(expectedMoney));
    }

    [Test]
    public void Test_Withdraw_NegativeAmount_ThrowsArgumentException()
    {
        // Arange
        double initialAmount = 1000;
        double getMoney = -400;

        // Act
        BankAccount account = new BankAccount(initialAmount);

        // Assert
        Assert.That(() => account.Withdraw(getMoney), Throws.ArgumentException);
    }

    [Test]
    public void Test_Withdraw_AmountGreaterThanBalance_ThrowsArgumentException()
    {

        // Arange
        double initialAmount = 1000;
        double getMoney = 1200;

        // Act
        BankAccount account = new BankAccount(initialAmount);

        // Assert
        Assert.That(() => account.Withdraw(getMoney), Throws.ArgumentException);
    }
}
