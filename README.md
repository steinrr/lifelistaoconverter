# Convert Life List to Artsobservasjoner

Et Python-script for å konvertere data fra Life List-app til Artsobservasjoner-format.

## Installasjon

1. Last ned og installer Python3
2. Installer tkinter-modulen til Python3 (pip3 install tkinter)
3. Installer pyperclip-modulen til Python3 (pip3 install pyperclip)
4. Kjør programmet (python3 convert_lifetlist_ao.py)

## Bruk

1. Eksporter fil fra Life List-app og overfør til datamaskin. Jeg eksporterer f.eks. til Dropbox som da automatisk overfører.
2. Når du kjører programmet, så ber det deg velge en fil - velg da den eksporterte filen
3. Programmet vil så gjøre konverteringen og legge resultatet på utklippstavlen
4. Du kan lime inn dette resultatet rett inn i "Importer"-bildet i Artsobservasjoner, eller ta det inn i Excel og jobbe ytterligere med det der først

## Viktig

Life List-app'en støtter ikke å legge til kjønn, aktivitet eller kommentarer.
Men hvis en i "Notes"-feltet under observasjon skriver på formen:
kjønn/aktivitet/kommentar

så vil programmet konvertere dette til riktige AO-felter. For eksempel:
Hunn/Ved fôring/Estimat

En kan også bare oppgi noen av feltene:
Hunn//Estimat