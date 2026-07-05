# Nummerierungs-Schema der App "Stickeralbum 2026" — geklärt

## Welche App
- **Name (Store):** "Sticker Album 2026" / dt. **"WM Stickeralbum 2026"**
- **Entwickler:** **MoovTech** (MOOVTECH DIGITAL LTDA), Brasilien
- **Website:** https://moovtech.app/stickers2026/
- **iOS:** https://apps.apple.com/us/app/sticker-album-2026/id6761956390 (Bundle-ID `com.moovtech.stickers2026`, Version 1.3.2, Build 35)
- **Android:** `com.moovtech.stickers2026` (Google Play)
- **Tech:** React Native / Expo SDK 54, Hermes-Bytecode. Backup "im kompakten Textformat" (= `SA26|...`).
- Rein numerischer Tracker: der Nutzer markiert Nummern, es sind KEINE Spielernamen/Bilder in der App hinterlegt (die App speichert pro Sektion nur `startNumber`/`endNumber`, keine Spielerliste).

## Quelle der Klärung: APK-Dekompilierung (definitiv, nicht Hypothese)
Die APK (`com.moovtech.stickers2026`, 65 MB) wurde heruntergeladen, entpackt und der
Hermes-Bytecode (`assets/index.android.bundle`) mit `hermes-dec` disassembliert.
Im Bytecode stehen die Sektions-Objekte **wörtlich** mit exakten Nummernbereichen.

### Die 3 App-Sektionen (verbatim aus dem Bundle)
```
{'id':'figurinhas-iniciais','name':'FWC', 'icon':'star',    'startNumber':1,  'endNumber':20}
{'id':'coca-cola',          'name':'CC',  'icon':'cupSoda', 'startNumber':21, 'endNumber':34}
{'id':'team-MEX', ... 'startNumber':35,  'endNumber':54}
{'id':'team-RSA', ... 'startNumber':55,  'endNumber':74}
... (alle 48 Teams, lückenlos) ...
{'id':'team-PAN', ... 'startNumber':975, 'endNumber':994}
```

## Flaches Nummerierungs-Schema (1 – 994)

| App-Nr.   | Inhalt                                             | offizieller Code |
|-----------|----------------------------------------------------|------------------|
| **1**     | Panini-Logo ("We Are Panini")                      | `00`             |
| **2–20**  | FWC-Specials (Emblem, Maskottchen, Ball, Host-Cities, WM-History) | `FWC1`–`FWC19` |
| **21–34** | Coca-Cola-Sticker (14 Stück)                       | `CC1`–`CC14` *(NICHT in offiziellen 980)* |
| **35–54** | Team 1 = Mexiko                                    | `MEX1`–`MEX20`   |
| 55–74     | Team 2 = Südafrika                                 | `RSA1`–`RSA20`   |
| …         | … 48 Teams in WM-Gruppenreihenfolge …              | …                |
| **975–994** | Team 48 = Panama                                 | `PAN1`–`PAN20`   |

**Gesamt App = 994 Sticker** (lückenlos 1–994, keine Gaps).

### Umrechnung offizieller Code → App-Nummer
- `00` → App **1**
- `FWCn` → App **n + 1** (FWC1→2 … FWC19→20)
- Team-Sticker: `app_number = startNumber(Team) + (Sticker-Nr − 1)`
  - z.B. MEX1 = 35, MEX13 = 47, PAN20 = 994

Diese Zuordnung wurde in `checklist.json` bei jedem der 980 offiziellen Sticker
als Feld `app_number` mit abgelegt.

## Warum 994 statt 980 — die 14er-Differenz ERKLÄRT
- Offizielle Kollektion = **980** (20 Specials + 48×20 Team).
- Die App fügt zusätzlich die **14 Coca-Cola-Sticker** (App-Nr. 21–34) als eigene Sektion ein.
- 980 + 14 = **994** = App-Maximum (= PAN20).
- Die vom Nutzer beobachtete höchste Nummer **993** ist PAN19; das tatsächliche Maximum
  ist **994** (PAN20). Die 993 war also nur die höchste zufällig gesehene, nicht das Limit.

## Team-Reihenfolge (App = laststicker = stickermanager, bestätigt identisch)
MEX, RSA, KOR, CZE, CAN, BIH, QAT, SUI, BRA, MAR, HAI, SCO, USA, PAR, AUS, TUR,
GER, CUW, CIV, ECU, NED, JPN, SWE, TUN, BEL, EGY, IRN, NZL, ESP, CPV, KSA, URU,
FRA, SEN, IRQ, NOR, ARG, ALG, AUT, JOR, POR, COD, UZB, COL, ENG, CRO, GHA, PAN
→ entspricht der WM-2026-Gruppenauslosung (Gruppe A–L, je 4 Teams).

## Wichtige Nuance zur Album-Reihenfolge vs. App-Reihenfolge
- Im **physischen Panini-Album**: `00` + `FWC1`–`FWC8` stehen VORNE, aber
  `FWC9`–`FWC19` ("FIFA World Cup History") stehen physisch am **ENDE** des Albums.
- Die **App** fasst dagegen alle 20 Intro/FWC-Sticker vorne in der Sektion
  `figurinhas-iniciais` (Nr. 1–20) zusammen — die App-Nummerierung folgt also der
  logischen Checklisten-Reihenfolge (00, FWC1–19), nicht der physischen Seitenlage.

## stickermanager.com (994-Kollektion)
- URL: https://www.stickermanager.com/en/collection/4304/...
- Nummeriert **nicht flach**, sondern mit denselben Panini-Codes (`00`, `FWC1`…, `MEX1`…, `CC1`…).
- Reihenfolge & Basis identisch zu laststicker/App. Coca-Cola dort als `CC1`–`CC12` (nur 12
  sichtbar in der Basisliste; regionale Varianten separat). Die App verwendet 14 CC-Plätze.
- Deren "994 Items" = dieselbe Rechnung (980 offiziell + Coca-Cola-Extras).

## Coca-Cola-Sticker: Detailhinweis
- Die App reserviert generisch **14** CC-Plätze (Nr. 21–34) ohne Namen.
- laststicker führt CC als **regionale Varianten**: CC-US1..12, CC-LAM1..14, CC-RW1..14, CC-EU1..12
  (Star-Spieler wie Lamine Yamal, Kimmich, Kane, Mbappé …). Je nach Region 12 oder 14 Motive.
- D.h. die 14 App-Plätze entsprechen am ehesten der 14er-Region (Latin America / Rest of World).
