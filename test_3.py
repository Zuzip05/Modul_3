#funkce dump
# bez knihovny nemůžeš pracovat s JSON objekty
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# funkci 'open' nachystáš objekt v Pythonu
json_soubor = open("prvni_json_soubor.json", mode="w")

# metoda 'dump' uloží objektu do souboru
json.dump(chuckuv_slovnik, json_soubor)

# ... nezapomeň objekt ukončit
json_soubor.close()

#---------------------------------------------------
#nahární json
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# metoda 'dumps' uloží objekt do stringu
vystup_s_jsonem = json.dumps(chuckuv_slovnik)

# metoda 'loads' přemapuje objekt ze stringu zpět na slovník
vystup_slovnik = json.loads(vystup_s_jsonem)
print(vystup_slovnik)

#------------------------------------------------------------
#užitečné argumenty
import json

chuckuv_slovnik = {
 "fanousek": "Łukasz"
}

# argument "ensure_ascii" součástí metody "dumps"
vystup_s_jsonem = json.dumps(chuckuv_slovnik, ensure_ascii=False)
print(vystup_s_jsonem)

#--------------------------------------------------
#zarovnání - indent
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# argument 'indent' součástí metody 'dumps'
# .. použité 4 mezery, ale hodnotu můžeš upravit
vystup_s_jsonem = json.dumps(chuckuv_slovnik, indent=4)
print(vystup_s_jsonem)

#-----------------------------------------------------
#seřazení klíčů
import json

chuckuv_slovnik = {
    "jmeno": "Chuck Norris",
    "neuspech": None,
    "kliky": "vsechny",
    "konkurence": False,
    "fanousek": "Łukasz"
}

# argument 'sort_keys' součástí metody 'dumps'
vystup_s_jsonem = json.dumps(chuckuv_slovnik, sort_keys=True)
print(vystup_s_jsonem)

#-----------------------------------------------------
#zápis nového csv
# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

# ... nachystáš nový soubor pro zápis
nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

# ... vytvoříš zapisovací objekt, který do souboru zapíše údaje
zapisovac = csv.writer(nove_csv)

# ... nejprve zapíšeš záhlaví
zapisovac.writerow(hlavicka)

# ... potom první údaj
zapisovac.writerow(osoba_1)

# ... druhý údaj
zapisovac.writerow(osoba_2)

# ... nakonec objekt a soubor uzavřeš
nove_csv.close()

#---------------------------------------------------
#writerows - zápis většího množství řádků
import csv

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

nove_csv = open("prvni_tabulkovy_soubor.csv", mode="w")

zapisovac = csv.writer(nove_csv)
zapisovac.writerows(
   ( 
       hlavicka,
       osoba_1,
       osoba_2
   )
)
nove_csv.close()

#------------------------------------------
#zápis s with
import csv

hlavicka = ["jmeno", "prijmeni", "vek"]
osoba_1 = ["Matous", "Pokoj", "28"]
osoba_2 = ["Petr", "Svetr", "27"]

with open("prvni_tabulkovy_soubor.csv", mode="w") as nove_csv:
   zapisovac = csv.writer(nove_csv)
   zapisovac.writerows(
      (
          hlavicka,
          osoba_1,
          osoba_2
      )
  )
   
#-------------------------------------------------------------
#dict writer
# Nezapomeň nahrát knihovnu, jinak soubor nevytvoříš
import csv

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

# ... nachystáš nový soubor pro zápis
nove_csv = open("druhy_tabulkovy_soubor.csv", mode="w")

# ... z existujících klíčů si vytvoříš záhlaví
zahlavi = osoba_1.keys()

# ... nachystáš si nový zapisovač, kterému nastavíš parametr "fieldnames"
zapisovac = csv.DictWriter(nove_csv, fieldnames=zahlavi)

# ... nejprve zapíšeš záhlaví
zapisovac.writeheader()

# ... následně oba údaje
zapisovac.writerow(osoba_1)
zapisovac.writerow(osoba_2)

# ... nakonec soubor ukončíš
nove_csv.close()

#----------------------------------------------
# čtení csv - reader
# Nezapomeň na potřebnou knihovnu
import csv

# Načteš soubor "csv" jako objekt "cteni_csv"
cteni_csv = open("prvni_tabulkovy_soubor.csv")

# Vytvoříš iterovatelný objekt se všemi záznamy ze souboru
cteni = csv.reader(cteni_csv)

# Vypíšeš obsah "csv" souboru s pomocí funkce "tuple"
print(tuple(cteni))

# Ukončíš soubor
cteni_csv.close()

#-----------------------------------------------
#čtení csv - reader s with
import csv

with open('prvni_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.reader(cteni_csv)
    print(tuple(cteni))

#-----------------------------------------------
#čtení csv - dictreader
# Nezapomeň na potřebnou knihovnu
import csv

# Načteš soubor "csv" jako objekt "cteni_csv"
cteni_csv = open("prvni_tabulkovy_soubor.csv")

# Vytvoříš iterovatelný objekt se všemi záznamy ze souboru
cteni = csv.DictReader(cteni_csv)

# Vypíšeš obsah "csv" souboru s pomocí funkce "tuple"
print(tuple(cteni))

# Ukončíš soubor
cteni_csv.close()

#----------------------------------------------------
#čtení csv - dictreader s with
import csv

with open('druhy_tabulkovy_soubor.csv') as cteni_csv:
    cteni = csv.DictReader(cteni_csv)
    print(tuple(cteni))


#-------------------------------------------------
#oddělovač - delimier
import csv

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    # přidaný parametr 'delimiter' s nastaveným středníkem
    zapisovac = csv.DictWriter(nove_csv, delimiter=";", fieldnames=zahlavi)
    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)

#--------------------------------------------------------
#dialect - vyber dialekt
import csv

osoba_1 = {"jmeno": "Matous", "prijmeni": "Pokoj", "vek": "28"}
osoba_2 = {"jmeno": "Petr", "prijmeni": "Svetr", "vek": "27"}

with open("druhy_tabulkovy_soubor.csv", mode="w") as nove_csv:
    zahlavi = osoba_1.keys()
    # přidaný parametr 'dialect' s nastaveným formátem 'excel-tab'
    zapisovac = csv.DictWriter(nove_csv, dialect="excel-tab", fieldnames=zahlavi)
    zapisovac.writeheader()
    zapisovac.writerow(osoba_1)
    zapisovac.writerow(osoba_2)

#-------------------------------------------------
#knihovna sys - řádné ukončení systému
import sys
jmeno = "Petr"
prijmeni = "Svetr"
if not jmeno or not prijmeni:
 print("Chybí jméno nebo příjmení")
 # jednička představuje obecně jakoukoliv chybu
 sys.exit(1)
else:
 print("Program pokračuje..")