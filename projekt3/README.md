# Engeto - 3 - projekt
Třetí projekt na Python Akademii od Engeta.

## Popis projektu
Tento projekt slouží k extrahování výsledků parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložené v souboru requirements.txt. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:

§ pip3 --version                        #overim verzi manazeru
§ pip3 install -r requirements.txt      #nainstalujeme knihovny

## Spuštění projektu
Spuštění souboru main.py v rámci příkazového řádku požaduje dva povinné argumenty.

python main.py <odkaz-uzemniho-celku> <vysledny-soubor>

Následně se vám stáhnou výsledky jako soubor s příponou .csv.

## Ukázka projektu
Výsledky hlasování pro okres Jihlava:
1.argument: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102
2.argument: vysledky_jihlava.csv

Spuštění programu:
python main.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102' 'vysledky_jihlava.csv'

Průběh stahování:
STAHUJI DATA Z VYBRANEHO URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=10&xnumnuts=6102
UKLADAM DO SOUBORU: vysledky_jihlava.csv
UKONCUJI main.py

Částečný výstup:
586854,Arnolec,133,96,96,13,0,0,9,0,2,9,0,1,1,0,0,5,0,0,37,0,9,2,0,2,0,6,0
586862,Batelov,1925,1244,1238,88,0,0,83,3,23,127,11,18,8,0,0,137,0,37,397,8,129,1,21,6,2,135,4
.....