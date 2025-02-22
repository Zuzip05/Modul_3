#Nejprve ručně vytvoříš JSON soubor. Potom vytvoř program, který načte zadaný json a získá z něj hodnoty ze specifických klíčů.
import json


# Následně pomocí funkce získej všechny klíče "jmeno"
def najdi_zadane_klice(jmeno_souboru: str) -> list:
    with open(jmeno_souboru) as json_soubor:
        obsah_jsonu = json.load(json_soubor)
    return [
            slovnik.get("jmeno") for slovnik in obsah_jsonu
    ]


if __name__ == "__main__":
    # Zavolej funkci a pomocí print() zobraz hodnoty
    print(najdi_zadane_klice("udaje.json"))

#-------------------------------------------------------------
#Seřaď klíče
#vytvoř program, který nejprve seřadí klíče slovníku a uloží je jako JSON soubor,přečte seřazený obsah a zobrazí jej.
import json


# Vytvoř funkci, která uloží seřazené klíče do JSON souboru
def zapis_serazene_klice(jmeno_souboru: str, data: dict) -> None:
    with open(jmeno_souboru, mode="w") as json_soubor:
        json.dump(data, json_soubor, sort_keys=True)


# Vytvoř funkci, která načte a vypíše obsah vytvořeného JSON souboru
def vypis_obsah_souboru(jmeno_souboru):
    with open(jmeno_souboru) as json_soubor:
        return json.load(json_soubor)


# Definuj proměnné 'jmeno_souboru' a 'data'
jmeno_souboru = "serazene.json"
data = {'4': 5, '6': 7, '1': 3, '2': 4}

# Zavolej obě funkce
zapis_serazene_klice(jmeno_souboru, data)
vysledek = vypis_obsah_souboru(jmeno_souboru)
print(vysledek)

#-----------------------------------------------------------------
#zapiš a přečti csv
import csv

# Vytvoř proměnnou 'data'
data = [
    [10, "a1", 1],
    [12, "a2", 3],
    [14, "a3", 5],
    [16, "a4", 7],
    [18, "a5", 9]
]


# Zapiš soubor typu CSV se jménem 'nove.csv'
with open("nove.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Přečti nově zapsaný CSV soubor
with open("nove.csv", newline="") as csvfile:
    csv_data = csv.reader(csvfile, delimiter=" ")

    for row in csv_data:
        print(", ".join(row))

