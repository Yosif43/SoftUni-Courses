namespace TestApp;

public class HashTagChecker
{
    public static string GetHashTags(string text)
    {
        if (string.IsNullOrWhiteSpace(text))
        {
            return "No content...";
        }
        int hashTagsNumber = GetHashTagsCount(text);

        if (hashTagsNumber == 0)
        {
            return "The text does not contain #tags.";
        }

        if (hashTagsNumber == 1)
        {
            return "Only one! You know exactly what you #tag.";
        }
        else if (hashTagsNumber % 2 == 0)
        {
            return $"The text contains an even number of #tags ({hashTagsNumber} in total).";
        }
        else
        {
            return $"The text contains an odd number of #tags ({hashTagsNumber} in total).";
        }
    }

    private static int GetHashTagsCount(string text)
    {
        int hashTagsNumber = 0;

        foreach (var tag in text)
        {
            if (tag == '#')
            {
                hashTagsNumber++;
            }
        }

        return hashTagsNumber;
    }
}

