using NUnit.Framework;

using System;

namespace TestApp.UnitTests;

public class ArticleTests
{
    private Article _article;

    [SetUp]
    public void SetUp()
    {
        _article = new Article();
    }

    // TODO: finish test
    [Test]
    public void Test_AddArticles_ReturnsArticleWithCorrectData()
    {
        // Arrange
        string[] input =
        {
            "Article Content Author",
            "Article2 Content2 Author2",
            "Article3 Content3 Author3"
        };
        // Act
        var result = _article.AddArticles(input);
        // Assert
        Assert.That(result.ArticleList, Has.Count.EqualTo(3));
        Assert.That(result.ArticleList[0].Title, Is.EqualTo("Article"));
        Assert.That(result.ArticleList[1].Content, Is.EqualTo("Content2"));
        Assert.That(result.ArticleList[2].Author, Is.EqualTo("Author3"));
    }

    [Test]
    public void Test_GetArticleList_SortsArticlesByTitle()
    {
        // Arrange
        string[] input =
        {
            "CArticle Content Author",
            "Article2 Content2 Author2",
            "BArticle3 Content3 Author3"
        };
        string sortCriteria = "title";
        var result = _article.AddArticles(input);
        string expected = $"Article2 - Content2: Author2{Environment.NewLine}" + 
            $"BArticle3 - Content3: Author3{Environment.NewLine}" + 
            $"CArticle - Content: Author";
        // Act
        var output = _article.GetArticleList(result, sortCriteria);
        // Assert
        Assert.That(output, Is.EqualTo(expected));
    }

    [Test]
    public void Test_GetArticleList_ReturnsEmptyString_WhenInvalidPrintCriteria()
    {
        // Arrange
        string[] input =
        {
            "CArticle Content Author",
            "Article2 Content2 Author2",
            "BArticle3 Content3 Author3"
        };
        string sortCriteria = "home";
        var result = _article.AddArticles(input);
        string expected = string.Empty;
        // Act
        var output = _article.GetArticleList(result, sortCriteria);
        // Assert
        Assert.That(output, Is.EqualTo(expected));
    }
}
