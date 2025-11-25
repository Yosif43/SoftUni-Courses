using System;

public class Article
{
    public string Title { get; private set; }
    public string Content { get; private set; }
    public string Author { get; private set; }

    public Article(string title, string content, string author)
    {
        Title = title;
        Content = content;
        Author = author;
    }

    public void Edit(string newContent)
    {
        Content = newContent;
    }

    public void ChangeAuthor(string newAuthor)
    {
        Author = newAuthor;
    }

    public void Rename(string newTitle)
    {
        Title = newTitle;
    }

    public override string ToString()
    {
        return $"{Title} - {Content}: {Author}";
    }
}

class Program
{
    static void Main(string[] args)
    {
        string[] articleParts = Console.ReadLine().Split(", ");
        Article article = new Article(articleParts[0], articleParts[1], articleParts[2]);

        int commandCount = int.Parse(Console.ReadLine());

        for (int i = 0; i < commandCount; i++)
        {
            string[] commandParts = Console.ReadLine().Split(": ");
            string command = commandParts[0];
            string argument = commandParts[1];

            switch (command)
            {
                case "Edit":
                    article.Edit(argument);
                    break;
                case "ChangeAuthor":
                    article.ChangeAuthor(argument);
                    break;
                case "Rename":
                    article.Rename(argument);
                    break;
            }
        }

        Console.WriteLine(article);
    }
}
