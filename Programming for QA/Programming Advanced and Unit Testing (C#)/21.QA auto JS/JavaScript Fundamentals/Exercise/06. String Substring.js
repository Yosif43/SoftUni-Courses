function findWord(word, text) {
    const isFoundWord = text.toLowerCase().split(' ').includes(word);


    if (isFoundWord) {
        console.log(word);
    } else {
        console.log(`${word} not found!`);
    }
}

findWord('javascript',
    'JavaScript is the best programming language')

findWord('python',
    'JavaScript is the best programming language')