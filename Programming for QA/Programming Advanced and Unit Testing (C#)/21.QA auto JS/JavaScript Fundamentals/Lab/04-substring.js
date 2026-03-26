function substring(str, start, count) {
    const result = str.substring(start, start + count);
    console.log(result);
}


substring('ASentence', 1, 8); // Should log 'Sentence'
substring('SkipWord', 4, 4); // Should log 'Word'