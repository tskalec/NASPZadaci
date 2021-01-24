# Kriptovalute

Prijatelj iz budućnosti poslao vam je informacije o tome kako će se kretati tečaj između 2 kriptovalute (bitcoina i litecoina) u sljedećih nekoliko mjeseci u budućnosti.
Koristeći te informacije, maksimizirajte svoju zaradu koristeći svoj početni iznos u bitcoinima, pri ćemu na kraju sav novac treba biti u bitcoinima.

Prototip funkcije koju treba napisati je:
```
std::pair<double, std::vector<Action>> maximizeProfit(const std::vector<double> &exchangeRate, double initialBitcoin)
```
gdje su:
* **exchangeRate** - kretanje tečaja bitcoina i litecoina (koliko 1 BTC iznosi LTC-a tog dana), počevši od 1. dana
* **initialBitcoin** - početna svota bitcoina kojom raspolažete 0. dana

Rješenje čini par koji se sastoji od:
* maksimalnog broja bitcoina na kraju razdoblja, zadnjeg dana za koji je dostupan tečaj
* akcije koje trebate poduzeti svakog dana da biste dobili maksimalnu svotu bitcoina

Akcije su definirane enum-om i predstavljaju zamjenu u drugu kriptovalutu ili ne činjenje ništa tog dana:
```
enum Action{
    exchange = 1, nothing = 0
};
```


