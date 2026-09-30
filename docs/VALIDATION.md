# Prüfstand

Bereits durchgeführt:

- 5.820 Endstellungen auf mindestens 20 Partien, sechs Halbzüge und FEN-Konsistenz geprüft.
- Stichprobe von 100 Partien mit einem unabhängigen vollständigen PGN-Leseweg verglichen.
- JavaScript-Syntax und DOM-basierte Bedienprüfungen: Suche, Seitennavigation, Stellungswahl, Vor/Zurück, Brett drehen, CSV/PGN/JSON-Export.
- Reale ChessDB-Abfragen für `queryall` und `querypv`, einschließlich CORS für lokal geöffnete Dateien.
- DOM-Prüfungen der Cloudanzeige mit Netzantworten: Fortsetzung, fehlende Daten, Netzfehler, Perspektive der Bewertung, veraltete Antworten nach Stellungswechsel.
- Der Repository-Build und seine Dateninvarianten werden mit `scripts/check.py` geprüft.

Noch offen: vollständige visuelle Browserprüfung. DOM-Prüfungen ersetzen diese nicht. Die früheren interaktiven Prüfhilfen sind nicht als dauerhafte Testsuite eingebunden.
