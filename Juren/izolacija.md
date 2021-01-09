# Problemi s izolacijom

2020 godina pokazala je moć prirode globalnom pandemijom i razornim potresima, stoga je vlada odlučila posegnuti za **Vašom** pomoći da digitalizacijom pobjedi nevolje.

Vaš zadatak je pomoći u sprječavanju pandemije. Zna se da se virus širi **direktnim društvenim interakcijama**. Podaci o društvenim interakcijama pribavljeni su od tajnih službi i predstavljeni su grafom. U grafu dvoje ljudi ima društvenu interakciju ako je **graph[i][j] = 1**

U trenutku nabave podatka neki od ljudi su inficirani virusom. U svim direktnim interakcijama gdje je **barem jedan** sudionik inficiran, **inficirat će se i drugi** sudionik. Takva transmisija virusa nastavit će se sve dok se više nema tko zaraziti. 

Zbog ograničenih resursa, u cilju sprječavanja pandemije moguće je izabrati **samo jednu** osobu koja će biti smještena u karantenu i time će se iz početnog grafa interakcija privremeno ukloniti **sve njezine direktne interakcije**.

Vaš zadatak je odabrati **jednu osobu** tako da se **maksimizira broj neinficiranih** osoba u zajednici. Ako postoji više osoba čija bi izolacija dovela do jednako dobre situacije, odabrati onu s **manjim indeksom**.

#### Primjer 1:
>Input: graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
Output: 0

#### Primjer 2:
> Input: graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
Output: 1

#### Primjer 3:
> Input: graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
Output: 1


#### Naputci:
>1 < graph.length = graph[0].length <= 300,
0 <= graph[i][j] == graph[j][i] <= 1,
graph[i][i] = 1,
1 <= initial.length < graph.length,
0 <= initial[i] < graph.length


