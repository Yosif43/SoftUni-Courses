function revealWords(words, sentence) {
    const allWords = words.split(', ');
    for (const word of allWords) {
        let textForReplace = '*'.repeat(word.length);
        sentence = sentence.replace(textForReplace, word);
    }
    console.log(sentence);
}

revealWords('great',
    'softuni is ***** place for learning new programming languages');

revealWords('great, learning',
    'softuni is ***** place for ******** new programming languages');