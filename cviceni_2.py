#čtečka řádků - funkce, která načte soubor a pokud soubor nenalezne
def nacti_radky(cesta_k_souboru: str):
    try:
        soubor = open(cesta_k_souboru)

    except FileNotFoundError:
        print(f'Soubor: {cesta_k_souboru} neexistuje!')
        obsah = []
    else:
        obsah = soubor.read()
        soubor.close()
    finally:
        return obsah


vysledek = nacti_radky("jazyky.txt")
print(vysledek)

#---------------------------------------------------------------
#sčítáme špinavý list
#Nyní bude tvým úkolem vytvořit funkci secti_hodnoty, která bude umět sečíst všechna čísla, která najde v zadaném listu. Jak v číselné, tak v textové podobě.
#Skript by si měl poradit i v takovém případě, kdy v listu nebudou jen čísla. Bude se snažit přetypovat hodnotu na float a pokud neuspěje, na hodnotu upozorní.

def secti_hodnoty(udaje):
    vysledek = 0.0

    for hodnota in udaje:
        try:
            cislo = float(hodnota)

        except Exception:
            print(f"Hodnota {hodnota} není číselný údaj.")
        else:
            vysledek += float(cislo)

    return vysledek


test = [1, 'asda', {'zvire': 'kocka'}, '3.0', 2.0, [], '\\n', 4]
print("Výsledek:", secti_hodnoty(test))

#----------------------------------------------------------------------
#slovníkový vyhledávač
muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990
}

def obsahuje_klic_a_hodnotu(klic: str, hodnota: str, slovnik: dict) -> bool:
    try:
        nalezena_hodnota = slovnik[klic]

    except KeyError:
        print(f'Klíč: {klic}, nenalezen.')
        vysledek = False
    else:
        print(f"Klíč: {klic}, nalezen.")

        if nalezena_hodnota == hodnota:
            vysledek = True
        else:
            print(f"Hodnota: {hodnota}, nenalezena.")
            vysledek = False
    finally:
        return vysledek


print(obsahuje_klic_a_hodnotu("jmeno", "Pepa", muj_slovnik))