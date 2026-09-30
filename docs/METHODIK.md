# Datenbasis und Methodik

Die zwölf ausgewerteten Monatsdateien reichen von 2024-12 bis 2025-11. Die genaue Liste einschließlich SHA-256 und Monatsstatistik steht in `data/provenance.json`. Die vollständigen Roh-PGNs sind nicht im Repository enthalten.

Jede Partie wird anhand ihrer Lichess-URL einmal gezählt. Bewertungsgrenzen: Minimum beider Ratings 2300, Maximum mindestens 2500. Nichtstandard-Startstellungen und Bullet werden ausgeschlossen. Gezählt wird ausschließlich die Stellung direkt nach dem sechsten Halbzug. Partien mit weniger Halbzügen entfallen.

Der Identitätsschlüssel berücksichtigt Brettstellung, Zugrecht, Rochaderechte und tatsächlich mögliche En-passant-Züge. Die Halbzug- und Zugnummernzähler gehören nicht zum Schlüssel. Zugumstellungen werden dadurch zusammengeführt. Angezeigt wird die häufigste beobachtete Zugfolge zur Stellung.

Die Sortierung erfolgt absteigend nach Partienzahl; Gleichstände werden lexikografisch nach EPD sortiert. Aufgenommen sind Stellungen mit mindestens 20 Partien innerhalb der genannten Datenbasis.

Benennung: exakter Eintrag aus der Lichess-Eröffnungssammlung, sonst der letzte benannte Vorläufer innerhalb der gezeigten Zugfolge. Der Name entscheidet nicht über die Aufnahme. Sieg/Remis/Niederlage bezeichnet das spätere Partieergebnis.

Häufigkeit ist kein Qualitätsurteil. Die Auswahl bevorzugt die Eröffnungen besonders aktiver Spieler und spiegelt den ausgewählten Zeitraum und die Online-Bedenkzeiten wider. Eine feste optimale Zahl von Tabien wurde nicht ermittelt.

Die ursprüngliche Auswertung wurde in dieser Arbeitssitzung durchgeführt; ein wiederverwendbarer vollständiger Rohdaten-Import gehört noch zur Aufgabenliste. Der beigefügte Build reproduziert die Anwendung aus den bereits ausgezählten Daten, nicht die Auszählung aus Roh-PGN.
