# Design-Plan: Panini WM 2026 Tracker ("Mein Album")

## Subjekt
Physisches Panini-Album digital gespiegelt. Nutzer: Clemens, 17, sammelt WM-2026-Sticker, tauscht in Schule/Arbeit. Job der Seite: in <5 Sek. sehen "wie weit bin ich, was fehlt, was kann ich tauschen" + Sticker schnell abhaken.

## Aesthetic Direction
NICHT: generisches Dashboard mit Cards + Fortschrittsbalken auf dunklem Grund (AI-Default #2).
SONDERN: Das Album selbst als Interface. Checkliste = Albumseiten: leere Sticker-Slots als gestrichelte Rahmen mit Nummer (wie im echten Album), besessene Sticker = "eingeklebt" (gefüllt, minimal rotiert, Schlagschatten). Foil-Sticker mit dezentem Prisma-Schimmer (CSS gradient). Duplikate = Sticker-Stapel-Optik mit Zähler-Badge.

## Palette (WM26-Gastgeber-Trikolore, sparsam)
- `--pitch`: #0E1B12 (dunkles Stadion-Grün, Hintergrund/Chrome)
- `--paper`: #F7F5EF (Albumseiten — Papier, NICHT cream-hero, nur als Seitenfläche im dunklen Rahmen)
- `--ink`: #1A2321 (Text auf Papier)
- `--host-red`: #D33A2C (Kanada — Akzent fehlend/Aktionen)
- `--host-green`: #1E7A46 (Mexiko — Fortschritt/besessen)
- `--host-blue`: #1D4E89 (USA — Links/Sekundär)
- `--foil`: linear-gradient Silber/Regenbogen für Foil-Slots

## Typo
- Display: "Archivo Black" o.ä. system-nah kondensiert fett (Sticker-Nummern-Ästhetik, wie Rückennummern) — via system font stack: 'Arial Narrow'/'Archivo'... Single-File ohne CDN → System-Stack: `'Segoe UI Variable Display', 'Segoe UI'` fett + kondensierte Fake-Caps mit letter-spacing. Alternativ: WOFF2 embedded? Zu groß. → Systemfonts, Charakter über Gewicht/Spacing/Größenkontrast.
- Body: 'Segoe UI', system-ui
- Daten/Nummern: 'Cascadia Mono', 'Consolas' (Sticker-Codes, Backup-Code)

## Layout
```
┌──────────────────────────────────────────┐
│ MEIN ALBUM WM26        [328/980] ████░░  │ ← sticky Kopf: Gesamt%
├──────────────────────────────────────────┤
│ [Dashboard] [Album] [Doppelte] [Tausch]  │ ← Tabs
│                                          │
│ ALBUM-TAB:                               │
│ Team-Leiste (horizontal scroll, Flaggen+ │
│ Mini-Fortschrittsring pro Team)          │
│ ┌────── Papier-Seite ─────────┐          │
│ │ GER · Deutschland  14/20    │          │
│ │ [▩][▩][░6][▩][░8]...        │ ← Slots  │
│ └─────────────────────────────┘          │
└──────────────────────────────────────────┘
```
Slot-Interaktion: Tap = besitzen/nicht; Long-press/Plus = Duplikat++.

## Signature
Der Sticker-Slot: leerer gestrichelter Rahmen mit großer Slot-Nummer → beim Abhaken "klebt" Sticker ein (scale 1.15→1, random ±2° Rotation, kurzer Schatten-Pop). Einmalige, subjektgetriebene Interaktion. Alles andere ruhig.

## Mobile
Primär Handy-Nutzung (beim Einkleben/Tauschen). Grid 4-5 Slots/Reihe auf 390px. Große Tap-Targets (min 44px).

## Quality floor
prefers-reduced-motion respektiert, Fokus-Ringe sichtbar, localStorage-Persistenz + SA26-Code Import/Export.
