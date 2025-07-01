using System;

class PasswordValidator
{
    static void Main()
    {
        string password = Console.ReadLine();
        ValidatePassword(password);
    }

    static void ValidatePassword(string password)
    {
        bool isValid = true;

        if (!IsLengthValid(password))
        {
            Console.WriteLine("Password must be between 6 and 10 characters");
            isValid = false;
        }

        if (!ContainsOnlyLettersAndDigits(password))
        {
            Console.WriteLine("Password must consist only of letters and digits");
            isValid = false;
        }

        if (!ContainsAtLeastTwoDigits(password))
        {
            Console.WriteLine("Password must have at least 2 digits");
            isValid = false;
        }

        if (isValid)
        {
            Console.WriteLine("Password is valid");
        }
    }

    static bool IsLengthValid(string password)
    {
        return password.Length >= 6 && password.Length <= 10;
    }

    static bool ContainsOnlyLettersAndDigits(string password)
    {
        foreach (char ch in password)
        {
            if (!char.IsLetterOrDigit(ch))
            {
                return false;
            }
        }
        return true;
    }

    static bool ContainsAtLeastTwoDigits(string password)
    {
        int digitsCount = 0;
        foreach (char ch in password)
        {
            if (char.IsDigit(ch))
            {
                digitsCount++;
            }
        }
        return digitsCount >= 2;
    }
}
