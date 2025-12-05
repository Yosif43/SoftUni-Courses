using Players;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StartUp
{
    public class Program
    {
        public static void Main()
        {

            Hero hero = new Hero("Yosko", 100);
            Elf elf = new Elf("Relinda", 80);
            MuseElf museElf = new MuseElf("Jastralina", 110);
            Knight knight = new Knight("Frozenfinger", 80);
            DarkKnight darkKnight = new DarkKnight("Lastpain", 80);
            BladeKnight bladeKnight = new BladeKnight("Finalhit", 80);

            Console.WriteLine(hero);
            Console.WriteLine(elf);
            Console.WriteLine(museElf);
            Console.WriteLine(knight);
            Console.WriteLine(darkKnight);
            Console.WriteLine(bladeKnight);
            
        }
    }
}
