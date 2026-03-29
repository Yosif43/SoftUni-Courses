function solve(input) {
    let phonebook = {};

    for (const entry of input) {
        let [name, phone] = entry.split(' ');

        phonebook[name] = phone;
    }

    for (const name in phonebook) {
        console.log(`${name} -> ${phonebook[name]}`);
    }
}


solve(['Tim 0834212554',
    'Peter 0877547887',
    'Bill 0896543112',
    'Tim 0876566344']
);
