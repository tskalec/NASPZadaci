# Spellchecker

Napišite *spellchecker* koji će ispravljati tekst i računati kvalitetu napisanih rečenica.
Tekst se sastojati od malih slova engleske abecede odvojenih s po jednim zarezom, no neke riječi su zbog pogreška pri tipkanju pogrešno napisane.
Spellchecker ima dostupan popis svih ispravnih riječi u jeziku te mora svaku riječ koja se ne nalazi u rječniku zamijeniti najbližom riječi iz rječnika.

Dozvoljene su 3 operacije primjenom kojih se zadana riječ može pretvoriti u neku riječ iz rječnika:
1. **umetanje znaka** s troškom `insertCost` (npr. abc -> abca)
2. **brisanje znaka** s troškom `deleteCost` (npr. abc -> ac)
3. **zamjena znaka** s troškom `modifyCost` (npr. abc -> adc)

Cilj je pretvoriti napisanu riječ u neku riječ iz rječnika i to učiniti uz najmanji *trošak pretvorbe* primjenom navedenih operacija (tj. pronaći riječ u rječniku za koju bi *trošak pretvorbe* bio najmanji).
U slučaju da više riječi iz rječnika ima jednak trošak, zamijenite je onom koja leksički dolazi prije.
Uz to, potrebno je izračunati mjeru netočnosti napisanog teksta kao ukupni trošak pretvorbe svih riječi u riječi iz rječnika.

Prototip funkcije koju treba napisati je:
```
std::pair<std::string, uint32_t> correctText(const std::string &text,
                                                 const std::set<std::string> &dictionary,
                                                 uint16_t insertCost, uint16_t deleteCost, uint16_t modifyCost)
```
gdje su:
* **text** - napisani tekst (mala slova engleske abecede odvojena s po jednim razmakom)
* **dictionary** - rječnik ispravnih riječi

Rješenje čini par koji se sastoji od:
* tekst s ispravljenim riječima
* mjera netočnosti napisanog teksta (ukupni minimalni trošak pretvorbe u ispravnu rečenicu)
