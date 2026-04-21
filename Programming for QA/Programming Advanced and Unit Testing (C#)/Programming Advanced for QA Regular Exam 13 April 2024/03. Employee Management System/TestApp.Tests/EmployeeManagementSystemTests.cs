using System;
using System.Collections.Generic;

using NUnit.Framework;

namespace TestApp.Tests;

[TestFixture]
public class EmployeeManagementSystemTests
{
    private EmployeeManagementSystem _system;
    [SetUp]
    public void SetUp()
    {
        _system = new EmployeeManagementSystem();
    }

    [Test]
    public void Test_Constructor_CheckInitialEmptyEmployeeCollectionAndCount()
    {
        
        // Act
        var count = _system.EmployeeCount;

        // Assert
        Assert.AreEqual(0, count);


    }

    [Test]
    public void Test_AddEmployee_ValidEmployeeName_AddNewEmployee()
    {
        // Arange
        var employeeName = "Yosif Yosifov";

        // Act
        _system.AddEmployee(employeeName);
        var employees = _system.GetAllEmployees();

        // Assert
        Assert.That(employees.Contains(employeeName), Is.True);

    }

    [Test]
    public void Test_AddEmployee_NullOrEmptyEmployeeName_ThrowsArgumentException()
    {
        // Act
        var employeeName = "";

        // Act & Assert
        var ex = Assert.Throws<ArgumentException>(() => _system.AddEmployee(employeeName));
        Assert.That(ex.Message, Is.EqualTo("Employee name cannot be empty or whitespace."));

    }

    [Test]
    public void Test_RemoveEmployee_ValidEmployeeName_RemoveFirstEmployeeName()
    {
        // Arange
        var employeeName = "Yosif Yosifov";
        _system.AddEmployee(employeeName);

        // Act
        _system.RemoveEmployee(employeeName);
        var employees = _system.GetAllEmployees();

        // Assert
        Assert.That(employees.Contains(employeeName), Is.False);

    }

    [Test]
    public void Test_RemoveEmployee_NullOrEmptyEmployeeName_ThrowsArgumentException()
    {
        // Arange
        var employeeName = "Nonexistent Employee";

        // Act & Assert
        var ex = Assert.Throws<ArgumentException>(() => _system.RemoveEmployee(employeeName));
        Assert.That(ex.Message, Is.EqualTo("Employee not found in the system."));

    }

    [Test]
    public void Test_GetAllEmployees_AddedAndRemovedEmployees_ReturnsExpectedEmployeeCollection()
    {
        // Arange
        var employeeName1 = "Yosif Yosifov";
        var employeeName2 = "Radoslav Petrov";
        _system.AddEmployee(employeeName1);
        _system.AddEmployee(employeeName2);
        _system.RemoveEmployee(employeeName1);

        // Act
        var employees = _system.GetAllEmployees();

        // Assert
        Assert.AreEqual(1, employees.Count, "Should contain exactly one employee.");
        Assert.Contains(employeeName2, employees, "Employee collection should contain 'Radoslav Petrov'.");

    }
}

