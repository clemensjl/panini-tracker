# Beitragen

Der Tracker ist eine einzelne HTML-Datei, erzeugt aus `template.html`, `checklist.json` und `sa26-code.txt`.

## Setup

Fork klonen, dann bauen:

```
python build_site.py
```

Das Skript (Python 3, nur Standardbibliothek) schreibt `index.html` neben sich. `index.html` nie von Hand ändern, Anpassungen gehören in `template.html`, Daten in `checklist.json`.

## Testen

Es gibt keine automatisierten Tests. Nach dem Bauen `index.html` im Browser öffnen und prüfen:

- Album, Übersicht und Tauschliste laden ohne Fehler in der Konsole
- Sticker antippen und halten (Duplikat) funktioniert, der Stand bleibt nach einem Neuladen erhalten
- Export und Import des `SA26|…`-Codes liefern denselben Bestand zurück

`build_site.py` bricht ab, wenn die Zahl der offiziellen Sticker nicht 980 ergibt, und listet unbekannte App-Nummern auf.

## Pull Request

1. Branch anlegen, `template.html` oder die Daten ändern, neu bauen.
2. `template.html`, `checklist.json` und die erzeugte `index.html` gemeinsam committen, damit GitHub Pages den neuen Stand ausliefert.
3. Pull Request gegen `main` öffnen und kurz beschreiben, was sich sichtbar ändert.

`sa26-code.txt` ist der Start-Bestand, den die Seite bei leerem Browserspeicher lädt.

Mit dem Pull Request stimmst du zu, dass dein Beitrag unter der [MIT-Lizenz](./LICENSE) steht.
