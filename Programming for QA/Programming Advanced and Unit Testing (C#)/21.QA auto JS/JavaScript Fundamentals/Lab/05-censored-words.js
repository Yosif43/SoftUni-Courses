function censorWord(text, word) {
    const replacement = '*'.repeat(word.length);
    const newText = text.split(word).join(replacement);

    return newText;
}


console.log(censorWord('A small sentence with some words', 'small')); // Output: A ***** sentence with some words
console.log(censorWord('Find the hidden word', 'hidden')); // Output: Find the ****** word