using System;
using NUnit.Framework;

using TestApp.Chat;

namespace TestApp.Tests;

[TestFixture]
public class ChatRoomTests
{
    private ChatRoom _chatRoom = null!;
    
    [SetUp]
    public void Setup()
    {
        this._chatRoom = new();
    }
    
    [Test]
    public void Test_SendMessage_MessageSentToChatRoom()
    {
        // Arange
        
        string sender = "Yosif";
        string message = "Start studying";

        // Act
        _chatRoom.SendMessage(sender, message);
        string actualResult = _chatRoom.DisplayChat();
        
        // Assert
        Assert.That(actualResult, Does.Contain("Chat Room Messages:"));
        Assert.That(actualResult, Does.Contain("Yosif: Start studying - Sent at "));
    }

    [Test]
    public void Test_DisplayChat_NoMessages_ReturnsEmptyString()
    {
        // Arange
        // ChatRoom chatRoom = new ChatRoom();
        

        // Act
        
        string actualResult = _chatRoom.DisplayChat();
        
        // Assert
        Assert.That(actualResult, Is.EqualTo(string.Empty));
    }

    [Test]
    public void Test_DisplayChat_WithMessages_ReturnsFormattedChat()
    {
        // Arange
        
        string sender = "Yosif";
        string message = "Start studying";
        string sender2 = "Ivan";
        string message2 = "Immediately";

        // Act
        _chatRoom.SendMessage(sender, message);
        _chatRoom.SendMessage(sender2, message2);
        string actualResult = _chatRoom.DisplayChat();
        
        // Assert
        Assert.That(actualResult, Does.Contain("Chat Room Messages:"));
        Assert.That(actualResult, Does.Contain("Yosif: Start studying - Sent at "));
        Assert.That(actualResult, Does.Contain("Ivan: Immediately - Sent at "));
    }
}
