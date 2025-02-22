#Výjimku přeskočíš a tvůj program doběhne až do konce nebo jak je potřeba
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
        print(vysledek)

    except TypeError:
        print("Nemůžeš dělit string")
    
    
for cislo in (1, 2, 3, "4", 5):
    vrat_vysledek(cislo, 2)

#množství výjimek - try/except/except
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
        print(vysledek)
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)   

#množství výjimek - try/except/else
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    # proveď pouze bez výjimek
    else:                     
        print(vysledek)
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

#try\except\else\finally
def vrat_vysledek(cislo: int, delitel: int) -> float:
    try:
        vysledek = cislo / delitel
    # první výjimka
    except TypeError:          
        print("Nemůžeš dělit string")
    # druhá výjimka
    except ZeroDivisionError:  
        print("Nemůžeš dělit nulou")
    # proveď pouze bez výjimek
    else:                      
        print(vysledek)
    # proveď pokaždé
    finally:                   
        print("..zpracováno")
    
    
for cislo, delitel in zip((1, 2, 3, "4", 5), (1, 2, 0, 3, 4)):
    vrat_vysledek(cislo, delitel)

#cviceni
data_1 = {
    'order': {
        'id': '1234', 'type': 'order.created', 'channel': 'eshop CZ'
    }
}


data_2 = {
    'order': {
        'id': '1234', 'type': 'order.created', 'channel': ''
    }
}


data_3 = {
    'order': {
        'id': '1234', 'type': 'order.created'
    }
}

vlozeny_dict = dict[str, dict[str,str]]
def vrat_zemi_objednavky (data: vlozeny_dist, key:str "channel"):
    try:
        return (data["order"]["channel"].split(" ")[1])
    except KeyError:
        print ("channel nenalezen")
        return None
    except IndexError:
        print ("channel je prázdný")
        return None


#debugování
def precist_soubor(cesta: str) -> list[str]:
    with open['emaily.txt', 'r'] as soubor:
              return soubor.readlines()

def ziskat_jmeno_domenu(radek: str):
      jmeno, domena=radek.split("@")
      return jmeno, domena

def projdi_vsechny_udaje(radky: list[str]) -> tuple[list[str],list[str]]:
    jmena,domeny=[],[]
    for radek in radky:
        if "end" == radek.strip().lower():
            break
        
        jmeno,domena = ziskat_jmeno_domeny(radek)
        jmena.append (jmeno)
        domeny.append (domena)
    return jmena,domeny

radky = precti_soubor ("emaily.txt")
print(projdi_vsechny_udaje(radky))
