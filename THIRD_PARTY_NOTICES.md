# Drittbestandteile

## chess.js 1.4.0

Projekt: https://github.com/jhlywa/chess.js

Eingebettet in `vendor/chess-1.4.0.js`. BSD-2-Clause; vollständiger Lizenztext in `vendor/chess-LICENSE.txt` und im eingebetteten Code.

## Schachfigurengrafiken

Die SVG-Figuren in `vendor/pieces.json` wurden mittels `chess.svg.piece()` aus python-chess erzeugt. Quelle: https://github.com/niklasf/python-chess/blob/master/chess/svg.py

Python-chess ist GPL-3.0-or-later. Für die eingebetteten Figurenvorlagen ist vor öffentlicher Freigabe die genaue Zuordnung der Grafiklizenz einschließlich Urhebernennung zu prüfen. Die Grafiken sind kein neu geschaffener TabiaScout-Code. Alternativ können sie durch eindeutig lizenzierte eigene Assets ersetzt werden.

## Daten

Lichess veröffentlicht seine Partieexporte unter CC0: https://database.lichess.org/

Die verwendete Elite-Auswahl stammt von Nikonoel: https://database.nikonoel.fr/ . Auswahl und Quellen werden ausdrücklich genannt; TabiaScout ist kein offizielles Lichess-Produkt.

Die Lichess-Eröffnungsnamen stehen unter CC0: https://github.com/lichess-org/chess-openings

## ChessDB

Online-Dienst: https://www.chessdb.cn/ ; API: https://www.chessdb.cn/cloudbookc_api.html

Das Programm fragt den Dienst ab; dessen Engine und vollständige Datenbank werden nicht mitgeliefert. Keine Verfügbarkeitsgarantie. Abgerufene Bewertungen sind von der statischen Lichess-Auswertung getrennt.
