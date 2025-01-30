import pytest
from bs4 import BeautifulSoup

HTML_TARTALOM = """<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<title>névtelen</title>
</head>
<body>
 
<!-- A HP-UX -->
A HP-UX a Hewlett Packard Unix rövidítése. 
A HP-UX, a Unix operációs rendszer Hewlett Packard vállalat 
által megvalósított kereskedelmi verziója. 
Alapja a Unix System V. A HP-UX első verziója
1984-ben jelent meg. A legújabb verziók támogatják a 
HP 9000-s számítógépes rendszereket, amelyekben
PA-RISC utasításkészletű architektúra található,
és a HPE Integrity Servers-t, amit Intel és Itanium 
architektúrával rendelkezik. 
 
 
<!-- Korábbi verziók  -->
A HP-UX korábbi verziói támogatták a Motorolla 68000
sorozatú processzoron alapuló HP Integral PC és 
HP 9000 Series 200, 300 és 400-s számítógépes 
rendszereket. 
 
<!-- Fájlrendszer -->
A HP-UX az első Unix, amely Unix engedélyezési rendszer 
alternatívájaként, lehetővé teszi az ACL használatát. 
A HP hosszú ideje együttműködik a Veritas szoftverrel,
fájlrendszerként így a VxFS-t használja. 
 
</body>
</html>"""

def teszt_nyelv_es_cim():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze a nyelvi attribútumot
    assert soup.html.get('lang') == 'hu', "Az oldal nyelve nem magyar."
    # Ellenőrizze a dokumentum címét
    assert soup.title.string == 'HP-UX', "A böngésző fülön nem a 'HP-UX' jelenik meg."

def teszt_focim():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze, hogy van-e főcím
    h1 = soup.find('h1')
    assert h1 is not None and h1.string == 'HP-UX', "Az egyesszintű HP-UX cím nem található."

def teszt_szakasz_cimek():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze a kettes szintű címek meglétét és tartalmát
    h2_cimek = [h2.string for h2 in soup.find_all('h2')]
    vart_cimek = ['A HP-UX', 'Korábbi verziók', 'Fájlrendszer']
    assert h2_cimek == vart_cimek, "A kettes szintű fejezetcímek nem megfelelőek."

def teszt_kiemeles_es_rovidites():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze, hogy a Hewlett Packard Unix ki van-e emelve és rövidítve
    rovidites = soup.find('abbr', {'title': 'Hewlett Packard Unix'})
    assert rovidites is not None and rovidites.string == 'Hewlett Packard Unix', "A Hewlett Packard Unix nincs kiemelve és rövidítve."

def teszt_felkövér_szoveg():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze, hogy a "Unix operációs" félkövér
    felkover_szoveg = soup.find('strong')
    assert felkover_szoveg is not None and felkover_szoveg.string == 'Unix operációs', "A 'Unix operációs' szöveg nincs félkövéren jelölve."

def teszt_dolt_szoveg():
    soup = BeautifulSoup(HTML_TARTALOM, 'html.parser')
    # Ellenőrizze, hogy a "VxFS-t" dőlt
    dolt_szoveg = soup.find('em')
    assert dolt_szoveg is not None and dolt_szoveg.string == 'VxFS-t', "A 'VxFS-t' szöveg nincs dőltként jelölve."

if __name__ == "__main__":
    pytest.main()
