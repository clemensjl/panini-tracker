# Mein Album ’26 — Panini WM 2026 Sticker-Tracker

Single-File-Tracker für die Panini FIFA World Cup 2026 Kollektion (980 offizielle Sticker + 14 Coca-Cola-Extras).

**Live:** https://clemensjl.github.io/panini-tracker/

**Lokal:** `index.html` im Browser öffnen, keine Installation und kein Server nötig.

## Features
- Album-Ansicht wie das echte Heft: gestrichelte Leerslots, „Einkleben“-Animation, Foil-Schimmer
- Tap = Sticker besitzen · gedrückt halten = Duplikat +1
- Übersicht mit Fortschritt pro Team (48 Teams, Gruppen A–L)
- Tauschliste (Suche/Biete) mit Copy-Button für WhatsApp
- Import/Export des `SA26|…`-Backup-Codes der App „Sticker Album 2026“ (MoovTech) — verlustfrei kompatibel
- Speicherung im Browser (localStorage), keine Server, kein Login

## Build
`index.html` wird generiert aus `template.html` + `checklist.json` + `sa26-code.txt` (Python 3, nur Standardbibliothek). Änderungen gehören in `template.html`, nicht in `index.html`:

```
python build_site.py
```

## Hintergrund
Die App-Nummerierung (1–994) wurde per APK-Dekompilierung geklärt: 994 = 980 offizielle + 14 Coca-Cola (Nr. 21–34). Details in `numbering-findings.md`, Design-Entscheidungen in `design-plan.md`.

## Beitragen
Hinweise in [CONTRIBUTING.md](./CONTRIBUTING.md).

## Lizenz
MIT, siehe [LICENSE](./LICENSE). Inoffizielles Fan-Projekt, nicht mit Panini oder der FIFA verbunden. Namen und Marken gehören ihren Inhabern.
