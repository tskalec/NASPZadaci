# Debeli imenik

Skupina studenata radi projekt za kolegij PROGI (https://www.fer.unizg.hr/predmet/proinz/obavijesti) i treba **Vašu** pomoć. Zbog velikog broja korisnika potrebno im je **efikasno** i **brzo** rješenje za filtriranje riječi iz imenika. 

Zadatak je sljedeći: 
Potrebno je napisati implementaciju dvije funkcije.
- void addToDictionary(List list); prima i sprema listu svih rijeci.
- int find(String prefix,String suffix); prima **prefix i suffix** riječi koje se traže, a vraća **index pronađene riječi u prethodno učitanoj listi** 

### Napomene:
- ako ima **više riječi** koje imaju traženi prefix i suffix, vratiti onu koja je **prvo učitana** (najmanji index u listi)
- ako **nema riječi** koja bi zadovoljavala tražene uvjete, vratiti **null**
- metoda addToDictionary poziva se prilikom konfiguracije sustava (jednom) dok se metoda find poziva izrazito **mnogo puta**
- riječi se sastoje od **malih slova engleske abecede**

Primjer:
Input
addToDictionary(["wafer", "wafafel", "wafel", "apple", "apple"])
find("w","r")           output: 0
find("w","l")           output: 1
find("waf","fel")       output: 1
find("ap","le")         output: 3

### Dodatne napomene:
- 1 <= words.length <= 15000
- 1 <= words[i].length <= 10
- 1 <= prefix.length, suffix.length <= 10
