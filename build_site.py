# -*- coding: utf-8 -*-
"""Injiziert checklist.json + SA26-Seed in template.html -> index.html"""
import json, re, io, os

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SP, "index.html")

with io.open(os.path.join(SP, "checklist.json"), encoding="utf-8") as f:
    cl = json.load(f)
with io.open(os.path.join(SP, "sa26-code.txt"), encoding="utf-8-sig") as f:
    code = f.read().strip()

# --- DATA ---
specials = [[s["code"], s["name"], 1 if s["foil"] else 0, s["app_number"]] for s in cl["specials"]]
cc = [["CC%d" % i, "Coca-Cola Sticker %d" % i, 20 + i] for i in range(1, 15)]
teams = []
for t in cl["teams"]:
    teams.append({
        "c": t["code"], "n": t["name"], "g": t["group"],
        "s": [[s["num"], s["name"], 1 if s["foil"] else 0, s["app_number"]] for s in t["stickers"]],
    })
data = {"specials": specials, "cc": cc, "teams": teams}

# --- SEED aus SA26 ---
parts = code.split("|")
assert parts[0] == "SA26", parts[0]
owned = []
for p in parts[2].split(","):
    if not p:
        continue
    if "-" in p:
        a, b = p.split("-")
        owned.extend(range(int(a), int(b) + 1))
    else:
        owned.append(int(p))
dupes = {}
if len(parts) > 3 and parts[3]:
    for p in parts[3].split(","):
        a, c = p.split(":")
        dupes[int(a)] = int(c)
seed = {"owned": owned, "dupes": dupes}

# --- Kontrolle ---
official_apps = set(s[3] for s in specials)
for t in teams:
    official_apps.update(s[3] for s in t["s"])
own_official = [a for a in owned if a in official_apps]
own_cc = [a for a in owned if 21 <= a <= 34]
print("Sticker gesamt (App):", len(owned))
print("davon offiziell (980er):", len(own_official))
print("davon Coca-Cola:", len(own_cc))
print("Duplikate:", dupes)
print("Offizielle Sticker gesamt:", len(official_apps))
assert len(official_apps) == 980
unknown = [a for a in owned if a not in official_apps and not (21 <= a <= 34)]
print("Unbekannte App-Nummern:", unknown)

# --- Injektion ---
with io.open(os.path.join(SP, "template.html"), encoding="utf-8") as f:
    tpl = f.read()
js = lambda o: json.dumps(o, ensure_ascii=False, separators=(",", ":"))
out = tpl.replace("__DATA__", js(data)).replace("__SEED__", js(seed))
assert "__DATA__" not in out and "__SEED__" not in out

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, "w", encoding="utf-8") as f:
    f.write(out)
print("OK ->", OUT, "(%d KB)" % (len(out.encode('utf-8')) // 1024))
