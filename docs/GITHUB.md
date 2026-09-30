# GitHub-Repository

Repository: https://github.com/CopySpotter/tabiascout

## Herunterladen und starten

Auf der Repository-Seite **Code → Download ZIP** wählen, entpacken und `index.html` doppelklicken.

## Mit Git arbeiten

```sh
git clone https://github.com/CopySpotter/tabiascout.git
cd tabiascout
python scripts/build.py
python scripts/check.py
```

Die fertige Einzeldatei liegt im Hauptverzeichnis. Kein Node/npm für Build oder Nutzung erforderlich.

## Stand

Der erste Entwicklungsstand liegt auf `main`. Bei Push und Pull Request prüft GitHub Actions den Build, die Datenkonsistenz und die JavaScript-Syntax. Es gibt noch keinen Release und kein aktiviertes Website-Hosting. Eine öffentliche Code-Ablage legt die Lizenz für eigenen Code nicht automatisch fest; siehe `LICENSE.md`.
