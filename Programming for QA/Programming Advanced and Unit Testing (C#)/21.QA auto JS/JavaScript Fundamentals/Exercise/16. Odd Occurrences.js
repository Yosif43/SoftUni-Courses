function findOddOccurrences(sentence) {
    let words = sentence.toLowerCase().split(' ');

    let wordCount = new Map();
    words.forEach(word => {
        if (wordCount.has(word)) {
            wordCount.set(word, wordCount.get(word) + 1);
        } else {
            wordCount.set(word, 1);
        }
    });

    let result = Array.from(wordCount).filter(([word, count]) => count % 2 !== 0).map(([word]) => word).join(' ');

    console.log(result);
}

findOddOccurrences('Java C# Php PHP Java PhP 3 C# 3 1 5 C#');
findOddOccurrences('Cake IS SWEET is Soft CAKE sweet Food');