#1. Erstelle ein Python-Programm, in dem die Teilnehmer ein Dictionary erstellen. Das Dictionary soll mindestens 10 deutsche Wörter mit ihren englischen Übersetzungen enthalten.

# 2. Danach soll das Programm den Benutzer per Eingabe (input) fragen, welches deutsche Wort ins Englische übersetzt werden soll.
#    Falls das Wort nicht im Dictionary ist, soll eine entsprechende Fehlermeldung angezeigt werden.


ger_en = {'fenster': 'window',
            'auto': 'car',
            'weg': 'road',
            'haus': 'house',
            'regen': 'rain',
            'schnee': 'snow',
            'sonne': 'sun',
            'stift': 'pen',
            'tor': 'gate',
            'eingang': 'entrance'              
                }


user = input(f'Choose a german word to be translated: ').lower()



if user in ger_en:
    print(f'The translation of {user} into english is {ger_en[user]}')
else:
    print(f'Das Wort befindet sich nicht im Worterbuch')

    #1. Einheitliche Eingaben: Stelle sicher, dass die Eingaben unabhängig von der Groß- und Kleinschreibung erkannt werden (arbeite mit .lower()).
#    2. Erweiterung des Wörterbuchs: Implementiere eine Funktion, mit der Benutzer das Wörterbuch erweitern können:
#   Verwende eine while True-Schleife mit einer Abbruchbedingung (z. B. Eingabe von „exit“), um neue Übersetzungen hinzuzufügen.