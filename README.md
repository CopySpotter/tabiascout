# TabiaScout

**Eröffnungsstellungen entdecken, prüfen und vergleichen.**

TabiaScout unterstützt die Suche nach passenden Tabien. Der aktuelle Prototyp zeigt 5.820 unterschiedliche Stellungen nach sechs Halbzügen aus einer definierten Auswahl starker Lichess-Spieler. Mit ChessDB lassen sich Bewertungen, Zugvorschläge und Hauptvarianten abrufen.

## Starten

Auf GitHub **Code → Download ZIP** wählen, entpacken und `index.html` im Browser öffnen. Keine Installation, kein Server und kein API-Schlüssel erforderlich. Die Sammlung und Bretter laufen offline. Nur die ausdrücklich gestartete ChessDB-Abfrage benötigt Internet.

## Vorhandene Funktionen

- 5.820 Stellungen, sortiert nach Partienzahl; 50 Einträge pro Seite.
- Suche nach Eröffnungsname, ECO-Code und Zugfolge.
- Anklickbares Brett mit den ersten sechs Halbzügen; Vor/Zurück und Brett drehen.
- Partienzahlen und Ergebnisverteilung, zusammengefasste Zugumstellungen.
- Export aller Einträge als CSV, PGN oder JSON samt Herkunftsdaten.
- ChessDB-Abfrage der aktuell gezeigten Stellung, Bewertungen aus Sicht von Weiß.
- Zugvorschläge und Hauptvariante auf einem zweiten Brett nachspielen.
- Behandlung fehlender Daten, Netzfehler und verspäteter Antworten nach Stellungswechsel.

## Was die Rangliste bedeutet

Die Nummer ist der Häufigkeitsrang, keine Qualitätsbewertung. Die Einträge sind konkrete Stellungen, nicht unterschiedliche Eröffnungssysteme. Auch eine häufige Stellung muss nicht zu den eigenen Zielen passen. Eine optimale Grenze bei 200, 300 oder 500 wurde bislang nicht nachgewiesen.

Grundlage: **3.439.091 Partien** aus der Lichess Elite Database, **Dezember 2024 bis November 2025**. Beide Spieler mindestens 2300, mindestens einer mindestens 2500 Lichess-Elo; ohne Bullet. 3.433.977 Partien erreichen sechs Halbzüge. Von 48.783 unterschiedlichen Endstellungen erfüllen 5.820 die Grenze von mindestens 20 Partien. Dies ist keine OTB-Meisterdatenbank und keine Vollauswertung aller Lichess-Partien.

## Entwicklung

Quellcode und eingebettete Daten sind getrennt. Die veröffentlichbare Einzeldatei lässt sich ohne Downloads mit Python 3 erzeugen:

```sh
python scripts/build.py
python scripts/check.py
```

Optional lokal über HTTP starten:

```sh
python -m http.server 8000
```

Danach `http://localhost:8000` öffnen.

| Pfad | Inhalt |
| --- | --- |
| `index.html` | Direkt startbare Einzeldatei |
| `src/template.html` | Oberfläche und Gestaltung |
| `src/app.js` | Sammlung, Suche, Bretter und Export |
| `src/chessdb.js` | Cloud-Abfrage und Variantenanzeige |
| `data/positions.json` | 5.820 ausgezählte Stellungen |
| `data/provenance.json` | Quellen, Monatsstatistik und Prüfsummen |
| `vendor/` | Eingebettete Drittbestandteile |
| `scripts/` | Build und Konsistenzprüfung |
| `docs/` | Methodik, Entwicklung und Veröffentlichung |

## Daten und Schnittstellen

- Elite-PGN-Sammlung: https://database.nikonoel.fr/
- Ursprung der Partien: https://database.lichess.org/
- Eröffnungsnamen: https://github.com/lichess-org/chess-openings
- ChessDB: https://www.chessdb.cn/cloudbookc_api.html

Bei einer Cloud-Abfrage werden die ausgewählte FEN und technische Verbindungsdaten an ChessDB übertragen. Abfragen erfolgen mit `learn=0`; keine automatische Massenabfrage und keine aktive Einreihung in die Berechnungswarteschlange. Ergebnisse werden für bis zu 100 Stellungen während der Sitzung zwischengespeichert.

OpenAI ist noch nicht integriert. Eine spätere Integration soll Erklärungen und Vergleiche liefern; Enginebewertungen bleiben Aufgabe der Schachanalyse. Ein geheimer API-Schlüssel gehört nicht in diese HTML-Datei.

## Stand und Grenzen

Entwicklungsstand **v0.1.0**, noch kein veröffentlichtes Release. Build, Datenkonsistenz, Bedienlogik und ChessDB-Schnittstelle wurden geprüft. Eine vollständige visuelle Prüfung in aktuellen Windows-/Linux-Browsern steht aus. Details: `docs/VALIDATION.md`.

Lizenzhinweise und noch offene Entscheidung für den eigenen Programmcode: `LICENSE.md` und `THIRD_PARTY_NOTICES.md`.
