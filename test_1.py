#metoda write
jmeno_souboru = "novy_soubor.txt"
pozdrav = "Ahoj, toto je první zápis do textového souboru"

txt_soubor = open(jmeno_souboru, mode="w")
txt_soubor.write(pozdrav)

txt_soubor.close()


#metoda writelines
jmeno_souboru = "novy_soubor.txt"
pozdrav = ["Ahoj", "toto", "je", "zápis", "pomocí", "seznamu."]
txt_soubor = open(jmeno_souboru, mode="w")

txt_soubor.writelines(pozdrav)

txt_soubor.close()

#kontrola - Je soubor zavřený, nebo ne, true  - zabřený, false - pořád načtený
print(txt_soubor.closed)

#čtení existujícího souboru
txt_soubor = open("novy_soubor.txt", mode="r")
obsah_txt = txt_soubor.read()
print(obsah_txt)
txt_soubor.close()

#Čtení a zápis současně
druhy_radek = "Ted pridavas druhy radek"

txt_soubor = open("novy_soubor.txt", mode="r+")
obsah_txt = txt_soubor.read()
txt_soubor.write(druhy_radek)

txt_soubor.close()

#přidávání do souboru
treti_radek = "
Toto je treti radek tveho puvodniho souboru souboru ^.^"

txt_soubor = open("druhy_soubor.txt", mode="a")
txt_soubor.write(treti_radek)
txt_soubor.close()

#úvod do manažeru
with open("dalsi_soubor.txt", mode="w") as txt_soubor:
    txt_soubor.write("Nový txt s kontextovým manažerem!")

#formátování
jmeno = "Lukas"
vek = 28

print("Ahoj, jmenuji se %s a je mi %d let" % (jmeno, vek))

#víceřádkový f-string
jmeno = "Petr"
vek = 66
povolani = "kouzelnik"

zprava = f"""
 Jmenuji se {jmeno},
 je mi {vek} let,
 a jsem {povolani}
"""
print(zprava)