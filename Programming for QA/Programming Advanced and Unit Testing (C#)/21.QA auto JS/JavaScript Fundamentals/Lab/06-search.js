function countWordOccurrences(text, searchWord) {
    const words = text.split(' ');

    let count = 0;
    for (let word of words) {
        if (word === searchWord) {
            count++;
        }
    }
    return count;
}

// Example usage:
console.log(countWordOccurrences('This is a word and it also is a sentence', 'is')); // Output: 2
console.log(countWordOccurrences('softuni is great place for learning new programming languages', 'softuni')); // Output: 1