namespace TestApp;

public class WordEraser
{
    public string Erase(List<string>? words, string? wordToErase)
    {
        if (words == null || words.Count == 0)
        {
            return string.Empty;
        }

        if (string.IsNullOrEmpty(wordToErase))
        {
            return string.Join(" ", words);
        }

        for (int i = 0; i < words.Count; i++)
        {
            if (words[i] == wordToErase)
            {
                words.Remove(wordToErase);
                i--;
            }
        }

        return string.Join(" ", words);
    }
}

