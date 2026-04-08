function inventory(input) {

    let heroes = [];

    for (const hero of input) {
        let currentHeroArray = hero.split(' / ');
        let currentObject = {
            name: currentHeroArray[0],
            level: currentHeroArray[1],
            items: currentHeroArray[2],
        }
        heroes.push(currentObject);
    }

    heroes.sort((hero1, hero2) =>
        hero1.level - hero2.level);

    for (const hero of heroes) {
        console.log(`Hero: ${hero.name}`);
        console.log(`level => ${hero.level}`);
        console.log(`items => ${hero.items}`);
    }
}

inventory([
    'Isacc / 25 / Apple, GravityGun',
    'Derek / 12 / BarrelVest, DestructionSword',
    'Hes / 1 / Desolator, Sentinel, Antara'
])

inventory([
    'Batman / 2 / Banana, Gun',
    'Superman / 18 / Sword',
    'Poppy / 28 / Sentinel, Antara'
])