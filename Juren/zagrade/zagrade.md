# Ivica i zagrade


Jednog dana, Ivica je naišao na problem provjeravanja je li neki niz zagrada točan.

Niz zagrada je točan ako je njima moguće sastaviti aritmetički izraz, recimo “(())()()”, “(()())” su točni , a “)(()” primjer netočnog niza. Pošto je Ivica vičan programer, taj zadatak mu je bio prejednostavan, pa je odlučio zakomplicirati stvari (jer zašto ne?) i sada se ne zna ispetljati iz problema i traži **Vašu pomoć**.

Dan vam je velik broj (ne nužno točnih) izraza sastavljenih od zagrada. Zadatak je spojiti neke od tih izraza u poredane parove tako da se svaki izraz zagrada ponavlja u najviše jednom paru i konkatenacija izraza zagrada u svakom paru je ispravan/točan izraz zagrada. Cilj je sastaviti što je više parova moguće.

## Ulaz

- n - broj izraza (1<n<10^5)

- svaki od sljedećih n linija sadrži jedan niz zagrada (neprazan string sačinjen od “(“ i “)” )

- ukupna duljina svih stringova je najviše 5*10^5

- isti se izraz u ulaznim podacima može pojaviti više puta . U ovom slučaju svaku kopiju izraza možete koristiti zasebno.

## Izlaz

- maksimalni broj parova koji se mogu napraviti tako da zadovoljavaju uvjete zadatka.

## Primjeri
#### Primjer 1
**Ulaz :**
7
)())
)
((
((
(
)
)
**Izlaz :** 2
**Objašnjenje:** optimalno je konstruirati dva para “(( )())" i "( )".

### Primjer 2
**Ulaz :**
4
(
((
(((
(())
**Izlaz :** 0

### Primjer 3
**Ulaz:**:
2
(())
()
**Izlaz :** 1

