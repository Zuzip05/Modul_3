#PŘEČTI SLOVA
#Vytvoř program, který přečte textový soubor a zobrazí slova, která obsahují 7 a více znaků.
# Otevri textovy soubor v modu cteni
def zobraz_slova(textovy_soubor):
    """
    Vytvor funkci, ktera otevre textovy soubor a precte slova.
    """
    zadana_slova = open(textovy_soubor, "r")

    data = zadana_slova.read()
    slova = data.split()

    for slovo in slova:
        if len(slovo) >= 7:
            print(slovo, end=" ")
    zadana_slova.close()


if __name__ == "__main__":
    zobraz_slova("slova.txt")

#-------------------------------------------------------------------------------------------------
#Vytvoř textový soubor
# zapiš pomocné proměnné
prvni_radek = "První řádek v souboru,\n"
druhy_radek = "druhý řádek v souboru,\n"
treti_radek = "třetí řádek v souboru."

# zapiš proměnné do nového txt souboru
txt_soubor = open("txt_soubor.txt", mode="w")
txt_soubor.write(prvni_radek)
txt_soubor.write(druhy_radek)
txt_soubor.write(treti_radek)

txt_soubor.close()

# přečti a ulož obsah txt souboru
cteni_txt = open("txt_soubor.txt")
obsah_txt = cteni_txt.readlines()

# vypiš výsledek
print(obsah_txt)

#---------------------------------------------------------------------------------------------
#Zaokrouhli hodnoty
# Vstupní proměnné
kombinace = 1.234
presnost_str = "Hello"
presnost_cisla = 123.4567

# Přesnost pro číselné znaky
formatovana_presnost = \
    f"|{presnost_cisla:.3}|{presnost_cisla:.4}|{presnost_cisla:.5}|"

# Přesnost a ostatní specifikátory
formatovana_kombinace = f"|{kombinace:$<6.4}|"

# Přesnost u stringu
formatovana_presnost_str = f"|{presnost_str:.4}|"

# Výpis hodnot
print(f"""\
Naformátovaná přesnost: \t{formatovana_presnost},
Naformátovaná kombinace: \t{formatovana_kombinace},
Naformátovaný string: \t\t{formatovana_presnost_str}.""")

# Ulož proměnné do souboru 'vysledek.txt'
print("Zapisuji do souboru")

with open("vysledek.txt", mode="w") as txt:
    txt.write("\n".join(
        (formatovana_presnost, formatovana_kombinace, formatovana_presnost_str)
        )
    )