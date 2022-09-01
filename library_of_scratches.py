#%%
from scratchbook import *
def makeLib(f, names):
    table = []
    for name in names:
        formula = f(name) if not f == element else name
        row = getInfo(makeScratch(formula))
        row["Name(s)"] = name
        row["Formula"] = formula
        table.append(row)
    return table


### ELEMENTS

fN, trN = 3, 3
fs = [f"{io}f{n}{dasq}" for n in range(1, fN + 1) for io in ["", "i", "o"] 
    for dasq in ["", "D", "A", "S", "Q"] if not f"{io}f{n}{dasq}" in [
     "f1S", "f1Q", "if1S", "if1Q", "of1S", "of1Q",]]
trs = [f"tr{n}{dasq}" for n in range(2, trN + 1) 
    for dasq in ["", "D", "A", "S", "Q"] if not f"tr{n}{dasq}" in [
    "tr2S", "tr2Q",]]
names = ["h", "gh", "g"] + [f"{base}{crv}" 
    for base in ["b", "i", "o", "d"] + fs + trs for crv in [
    "", "Ex", "Log"]]
ELEMENTS = makeLib(element, names)


### TEARS

tN = 3
names = [f"{base}t{n}{crv}" for n in range(2, tN + 1) 
        for base in ["", "i", "o", "d", "if", "of", "tr"]
        for crv in ["", "Ex", "Log"] ]
TEARS = makeLib(tear, names)


### ORBITS
base_names = ["g_d", "b_b", "i_o", "o_i", "d_d", "d_g"]
f_names = [
    f'b_f{n}_1{n+1}'
    for pair in ["b_f", "i_of", "o_if"]
    for n in range(1, fN + 1)
    ] + [
    f'{l}{n}_{r}_{n+1}1' 
    for l,r in [["f","b"], ["if","o"], ["of","i"]]
    for n in range(1, fN + 1)
    ] + [
    f'{l}{n}_{r}{m}{f"_{n+1}{m+1}" if not n == m else ""}' 
    for n in range(1, fN + 1)
    for m in range(1, fN + 1)
    for l, r in [["f","f"], ["if","of"], ["of","if"]]
    ] 
tr_names = [
    f"{el}_tr{n}_1{n}" 
    for el in "gb"
    for n in range(2, trN + 1)
    ] + [
    f'tr{n}_{el}_{n}1'
    for el in "gb"
    for n in range(2, trN + 1)
    ] + [
    f'tr{n}_tr{m}{f"_{n}{m}" if not n == m else ""}' 
    for n in range(2, trN + 1)
    for m in range(2, trN + 1)
    ]
names = base_names + f_names + tr_names
# print("Orbits without ExLog", len(names))
names += [
    f'{p.split("_")[0]}{l}_{p.split("_")[1]}{r}{"_" + p.split("_")[2] if p.split("_")[2:] else ""}'
    for p in names
    for l in ["", "Ex", "Log"] for r in ["", "Ex", "Log"]
    if not l == r == ""
]
# print("Orbits with ExLog", len(names))
ORBITS = makeLib(orbit, names)

print(ORBITS[0])
# %%
