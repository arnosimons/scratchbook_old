# from classes import *

### Scalars
#############################################################

def steps(n):
    return [[1/n, 1/n, i/n] for i in range(n)]

_1s = steps(1)
_2s = steps(2)
_3s = steps(3)
_4s = steps(4)
_6s = steps(6)
_8s = steps(8)

### Curves
#############################################################

def _N(x):
    return (-np.cos(np.pi * x) + 1) / 2
def _Nr(x):
    return (np.cos(np.pi * x) + 1) / 2
def _X(x):
    return 1 - np.sqrt(1 - (x ** 2))
def _Xr(x):
    return np.sqrt(1 - ((x - 0) ** 2))
def _D(x):
    return np.sqrt(1 - ((x - 1) ** 2))
def _Dr(x):
    return 1 - np.sqrt(1 - ((x - 1) ** 2))

finv = {
    _N:_Nr,
    _Nr:_N,
    _X:_Xr,
    _Xr:_X,
    _D:_Dr,
    _Dr:_D,
}

fneg = {
    _N:_Nr,
    _Nr:_N,
    _X:_Dr,
    _Xr:_D,
    _D:_Xr,
    _Dr:_X,
}

### Clicks
#############################################################

_ = np.array(())
_0 = np.array((0,))
_2 = np.array((1/2,))
_3 = np.array((1/3, 2/3))
_4 = np.array((1/4, 2/4, 3/4))
_5 = np.array((1/5, 2/5, 3/5, 4/5))
_6 = np.array((1/6, 2/6, 3/6, 4/6, 5/6))
_7 = np.array((1/7, 2/7, 3/7, 4/7, 5/7, 6/7))
_8 = np.array((1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8))
_9 = np.array((1/9, 2/9, 3/9, 4/9, 5/9, 6/9, 7/9, 8/9))

### Base scratches
#############################################################

b = Scratch([[_1s[0], _N, "k", _]])
bX = Scratch([[_1s[0], _X, "k", _]])
bD = Scratch([[_1s[0], _D, "k", _]])

g = Scratch([[_1s[0], _N, "w", _]])
gX = Scratch([[_1s[0], _X, "w", _]])
gD = Scratch([[_1s[0], _D, "w", _]])

tr1 = Scratch([[_1s[0], _N, "k", _0]])
tr1X = Scratch([[_1s[0], _X, "k", _0]])
tr1D = Scratch([[_1s[0], _D, "k", _0]])

tr2 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _2))]])
tr2X = Scratch([[_1s[0], _X, "k", np.hstack((_0, _2))]])
tr2D = Scratch([[_1s[0], _D, "k", np.hstack((_0, _2))]])

tr3 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _3))]])
tr3X = Scratch([[_1s[0], _X, "k", np.hstack((_0, _3))]])
tr3D = Scratch([[_1s[0], _D, "k", np.hstack((_0, _3))]])

tr4 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _4))]])
tr4X = Scratch([[_1s[0], _X, "k", np.hstack((_0, _4))]])
tr4D = Scratch([[_1s[0], _D, "k", np.hstack((_0, _4))]])

f1 = Scratch([[_1s[0], _N, "k", _2]])
f1X = Scratch([[_1s[0], _X, "k", _2]])
f1D = Scratch([[_1s[0], _D, "k", _2]])

f2 = Scratch([[_1s[0], _N, "k", _3]])
f2X = Scratch([[_1s[0], _X, "k", _3]])
f2D = Scratch([[_1s[0], _D, "k", _3]])

f3 = Scratch([[_1s[0], _N, "k", _4]])
f3X = Scratch([[_1s[0], _X, "k", _4]])
f3D = Scratch([[_1s[0], _D, "k", _4]])

### Tears
#############################################################

t1N = t1 = Scratch([[_s, _N, "k", _] for _s in steps(2)])
t2N = t2 = Scratch([[_s, _N, "k", _] for _s in steps(3)])
t3N = t3 = Scratch([[_s, _N, "k", _] for _s in steps(4)])

t1X = Scratch([[_s, _X, "k", _] for _s in steps(2)])
t2X = Scratch([[_s, _X, "k", _] for _s in steps(3)])
t3X = Scratch([[_s, _X, "k", _] for _s in steps(4)])

t1D = Scratch([[_s, _D, "k", _] for _s in steps(2)])
t2D = Scratch([[_s, _D, "k", _] for _s in steps(3)])
t3D = Scratch([[_s, _D, "k", _] for _s in steps(4)])

ct1N = ct1 = Scratch([[_s, _N, "k", _0] for _s in steps(2)])
ct2N = ct2 = Scratch([[_s, _N, "k", _0] for _s in steps(3)])
ct3N = ct3 = Scratch([[_s, _N, "k", _0] for _s in steps(4)])

ct1X = Scratch([[_s, _X, "k", _0] for _s in steps(2)])
ct2X = Scratch([[_s, _X, "k", _0] for _s in steps(3)])
ct3X = Scratch([[_s, _X, "k", _0] for _s in steps(4)])

ct1D = Scratch([[_s, _D, "k", _0] for _s in steps(2)])
ct2D = Scratch([[_s, _D, "k", _0] for _s in steps(3)])
ct3D = Scratch([[_s, _D, "k", _0] for _s in steps(4)])

### Orbits, Special Scratches, and DataFrame
#############################################################

from itertools import permutations
from itertools import combinations_with_replacement
import re
import pandas as pd

### make elements and formulas

letters = {
    "b":  (1, 0),
    "g":  (0, 0),
    "tr1":(1, 1),
    "tr2":(2, 2),
    "tr3":(3, 3),
    "tr4":(4, 4),
    "f1": (2, 1),
    "f2": (3, 2),
    "f3": (4, 3),
    "t1": (2, 0),
    "t2": (3, 0),
    "t3": (4, 0),
    "ct1":(2, 1),
    "ct2":(3, 2),
    "ct3":(4, 3),
}
curves = ["", "X", "D"]
elements = [
    "".join([l, c]) 
    for l in letters.keys() 
    for c in curves
]
variants = sorted(set(
    list(permutations(elements, 2)) 
    + list(combinations_with_replacement(elements, 2))
))
ratios = [
    ("(1/2)", "(1/2)", ""), 
    ("(1/3)", "(2/3)", "_R3"), 
    ("(2/3)", "(1/3)", "_L3"), 
    ("(1/4)", "(3/4)", "_R4"), 
    ("(3/4)", "(1/4)", "_L4"),
]
formulas = [
    f'{"_".join(p)}{r[2]} = {p[0]} / {r[0]} + ~{p[1]} / {r[1]}' 
    for p in variants for r in ratios
]

### functions for table
def soundsAndClicks(name):
    els = re.sub(r"[XDN]|_[RL][3,4]", "", name).split("_")
    return (
        sum(letters[i][0] for i in els), 
        sum(letters[i][1] for i in els),
    )

def isOrbit(name):
    return "Yes" if "_" in name else "No"

def turning_point(name):
    if not "_" in name:
        return "None"
    if "R4" in name:
        return "1/4"
    if "R3" in name:
        return "1/3"
    if "L3" in name:
        return "2/3"
    if "L4" in name:
        return "3/4"
    return "1/2"

### make table

data_elements = [[
    name,
    name,
    1,
    *soundsAndClicks(name),
    isOrbit(name),
    turning_point(name),
    "element",
    "",
] for name in elements]

data_composites = [[
    name,
    name,
    1,
    *soundsAndClicks(name),
    isOrbit(name),
    turning_point(name),
    expression,
    "",
] for name, expression in [f.split(" = ") for f in formulas]]
#############################################################

df = pd.DataFrame(
    data=data_elements + data_composites,
    index=[i[0] for i in data_elements + data_composites],
    columns=[
        "Name", 
        "Code Name",
        "#Counts",
        "#Sounds", 
        "#Pauses",
        "Orbit", 
        "Turning Points", 
        "Composition",
        "Tutorial",
    ],
)

### add tutorials

df.at["b", "Tutorial"] = "https://www.youtube.com/watch?v=rtqTmUVjsuY" # baby
df.at["b_g", "Tutorial"] = "https://www.youtube.com/watch?v=Fl-JlMxQlxc" # stab
df.at["b_tr1", "Tutorial"] = "https://www.youtube.com/watch?v=pKe3OUKaK2k" # chirp
df.at["f1", "Tutorial"] = "https://www.youtube.com/watch?v=P33Obuj0zAI" # 1-click-flare
df.at["f1_f1", "Tutorial"] = "https://www.youtube.com/watch?v=P33Obuj0zAI" # 1-click-flare orbit
df.at["f2", "Tutorial"] = "https://www.youtube.com/watch?v=1yqMmsQhnHU&t=189s" # 2-click-flare
df.at["f2_f2", "Tutorial"] = "https://www.youtube.com/watch?v=1yqMmsQhnHU&t=189s" # 2-click-flare orbit
df.at["~bD_f1D_R3", "Tutorial"] = "https://www.youtube.com/watch?v=JRaUuXhw6Qk" # 1-click tazer
df.at["~bD_f2D_R4", "Tutorial"] = "https://www.youtube.com/watch?v=JRaUuXhw6Qk" # 2-click tazer

for name in df.index: # transformers and pure transformer orbits
    if ("_" in name and re.match(r"tr\d[XD]?_tr\d[XD]?", name)) or re.match(r"tr\d[XD]?$", name):
        df.at[name, "Tutorial"] = "https://www.youtube.com/watch?v=XdkNAePjM7o"
for name in df.index: # tears and pure tear orbits
    if ("_" in name and re.match(r"t\d[XD]?_t\d[XD]?", name)) or re.match(r"t\d[XD]?$", name):
        df.at[name, "Tutorial"] = "https://www.youtube.com/watch?v=WN8ity9B35U"

### add special names

df.at["b", "Code Name"] = "baby, b"
df.at["bX", "Code Name"] = "babyX, bX"
df.at["bD", "Code Name"] = "babyD, bD"

df.at["g", "Code Name"] = "ghost, g"
df.at["gX", "Code Name"] = "ghostX, gX"
df.at["gD", "Code Name"] = "ghostD, gD"

df.at["tr1", "Code Name"] = "transformer1, trans1, tr1"
df.at["tr1X", "Code Name"] = "transformer1X, trans1X, tr1X"
df.at["tr1D", "Code Name"] = "transformer1D, trans1D, tr1D"
df.at["tr2", "Code Name"] = "transformer2, trans2, tr2"
df.at["tr2X", "Code Name"] = "transformer2X, trans2X, tr2X"
df.at["tr2D", "Code Name"] = "transformer2D, trans2D, tr2D"
df.at["tr3", "Code Name"] = "transformer3, trans3, tr3"
df.at["tr3X", "Code Name"] = "transformer3X, trans3X, tr3X"
df.at["tr3D", "Code Name"] = "transformer3D, trans3D, tr3D"
df.at["tr4", "Code Name"] = "transformer4, trans4, tr4"
df.at["tr4X", "Code Name"] = "transformer4X, trans4X, tr4X"
df.at["tr4D", "Code Name"] = "transformer4D, trans4D, tr4D"

df.at["f1", "Code Name"] = "flare1, f1"
df.at["f1X", "Code Name"] = "flare1X, f1X"
df.at["f1D", "Code Name"] = "flare1D, f1D"
df.at["f2", "Code Name"] = "flare2, f2"
df.at["f2X", "Code Name"] = "flare2X, f2X"
df.at["f2D", "Code Name"] = "flare2D, f2D"
df.at["f3", "Code Name"] = "flare3, f3"
df.at["f3X", "Code Name"] = "flare3X, f3X"
df.at["f3D", "Code Name"] = "flare3D, f3D"

df.at["t1", "Code Name"] = "tear1, t1"
df.at["t1X", "Code Name"] = "tear1X, t1X"
df.at["t1D", "Code Name"] = "tear1D, t1D"
df.at["t2", "Code Name"] = "tear2, t2"
df.at["t2X", "Code Name"] = "tear2X, t2X"
df.at["t2D", "Code Name"] = "tear2D, t2D"
df.at["t3", "Code Name"] = "tear3, t3"
df.at["t3X", "Code Name"] = "tear3X, t3X"
df.at["t3D", "Code Name"] = "tear3D, t3D"

df.at["b_g", "Code Name"] = "stab, st, b_g"
df.at["bX_g", "Code Name"] = "stabX, stX, bX_g"
df.at["bD_g", "Code Name"] = "stabD, stD, bD_g"
df.at["b_g_R4", "Code Name"] = "stab_R4, st_R4, b_g_R4"
df.at["bX_g_R4", "Code Name"] = "stabX_R4, stX_R4, bX_g_R4"
df.at["bD_g_R4", "Code Name"] = "stabD_R4, stD_R4, bD_g_R4"
df.at["b_g_R3", "Code Name"] = "stab_R3, st_R3, b_g_R3"
df.at["bX_g_R3", "Code Name"] = "stabX_R3, stX_R3, bX_g_R3"
df.at["bD_g_R3", "Code Name"] = "stabD_R3, stD_R3, bD_g_R3"
df.at["b_g_L3", "Code Name"] = "stab_L3, st_L3, b_g_L3"
df.at["bX_g_L3", "Code Name"] = "stabX_L3, stX_L3, bX_g_L3"
df.at["bD_g_L3", "Code Name"] = "stabD_L3, stD_L3, bD_g_L3"
df.at["b_g_L4", "Code Name"] = "stab_L4, st_L4, b_g_L4"
df.at["bX_g_L4", "Code Name"] = "stabX_L4, stX_L4, bX_g_L4"
df.at["bD_g_L4", "Code Name"] = "stabD_L4, stD_L4, bD_g_L4"

df.at["b_tr1", "Code Name"] = "chirp, c, b_tr1"
df.at["bX_tr1X", "Code Name"] = "chirpX, cX, bX_tr1X"
df.at["bD_tr1D", "Code Name"] = "chirpD, cD, bD_tr1D"
df.at["b_tr1_R4", "Code Name"] = "chirp_R4, c_R4, b_tr1_R4"
df.at["bX_tr1X_R4", "Code Name"] = "chirpX_R4, cX_R4, bX_tr1X_R4"
df.at["bD_tr1D_R4", "Code Name"] = "chirpD_R4, cD_R4, bD_tr1D_R4"
df.at["b_tr1_R3", "Code Name"] = "chirp_R3, c_R3, b_tr1_R3"
df.at["bX_tr1X_R3", "Code Name"] = "chirpX_R3, cX_R3, bX_tr1X_R3"
df.at["bD_tr1D_R3", "Code Name"] = "chirpD_R3, cD_R3, bD_tr1D_R3"
df.at["b_tr1_L3", "Code Name"] = "chirp_L3, c_L3, b_tr1_L3"
df.at["bX_tr1X_L3", "Code Name"] = "chirpX_L3, cX_L3, bX_tr1X_L3"
df.at["bD_tr1D_L3", "Code Name"] = "chirpD_L3, cD_L3, bD_tr1D_L3"
df.at["b_tr1_L4", "Code Name"] = "chirp_L4, c_L4, b_tr1_L4"
df.at["bX_tr1X_L4", "Code Name"] = "chirpX_L4, cX_L4, bX_tr1X_L4"
df.at["bD_tr1D_L4", "Code Name"] = "chirpD_L4, cD_L4, bD_tr1D_L4"

df.at["tr1_tr1", "Code Name"] = "fakechirp, fc, tr1_tr1"
df.at["tr1X_tr1X", "Code Name"] = "fakechirpX, fcX, tr1X_tr1X"
df.at["tr1D_tr1D", "Code Name"] = "fakechirpD, fcD, tr1D_tr1D"
df.at["tr1_tr1_R4", "Code Name"] = "fakechirp_R4, fc_R4, tr1_tr1_R4"
df.at["tr1X_tr1X_R4", "Code Name"] = "fakechirpX_R4, fcX_R4, tr1X_tr1X_R4"
df.at["tr1D_tr1D_R4", "Code Name"] = "fakechirpD_R4, fcD_R4, tr1D_tr1D_R4"
df.at["tr1_tr1_R3", "Code Name"] = "fakechirp_R3, fc_R3, tr1_tr1_R3"
df.at["tr1X_tr1X_R3", "Code Name"] = "fakechirpX_R3, fcX_R3, tr1X_tr1X_R3"
df.at["tr1D_tr1D_R3", "Code Name"] = "fakechirpD_R3, fcD_R3, tr1D_tr1D_R3"
df.at["tr1_tr1_L3", "Code Name"] = "fakechirp_L3, fc_L3, tr1_tr1_L3"
df.at["tr1X_tr1X_L3", "Code Name"] = "fakechirpX_L3, fcX_L3, tr1X_tr1X_L3"
df.at["tr1D_tr1D_L3", "Code Name"] = "fakechirpD_L3, fcD_L3, tr1D_tr1D_L3"
df.at["tr1_tr1_L4", "Code Name"] = "fakechirp_L4, fc_L4, tr1_tr1_L4"
df.at["tr1X_tr1X_L4", "Code Name"] = "fakechirpX_L4, fcX_L4, tr1X_tr1X_L4"
df.at["tr1D_tr1D_L4", "Code Name"] = "fakechirpD_L4, fcD_L4, tr1D_tr1D_L4"

df.at["tr1_b", "Code Name"] = "slice, sl, tr1_b"
df.at["tr1X_bX", "Code Name"] = "sliceX, slX, tr1X_bX"
df.at["tr1D_bD", "Code Name"] = "sliceD, slD, tr1D_bD"
df.at["tr1_b_R4", "Code Name"] = "slice_R4, sl_R4, tr1_b_R4"
df.at["tr1X_bX_R4", "Code Name"] = "sliceX_R4, slX_R4, tr1X_bX_R4"
df.at["tr1D_bD_R4", "Code Name"] = "sliceD_R4, slD_R4, tr1D_bD_R4"
df.at["tr1_b_R3", "Code Name"] = "slice_R3, sl_R3, tr1_b_R3"
df.at["tr1X_bX_R3", "Code Name"] = "sliceX_R3, slX_R3, tr1X_bX_R3"
df.at["tr1D_bD_R3", "Code Name"] = "sliceD_R3, slD_R3, tr1D_bD_R3"
df.at["tr1_b_L3", "Code Name"] = "slice_L3, sl_L3, tr1_b_L3"
df.at["tr1X_bX_L3", "Code Name"] = "sliceX_L3, slX_L3, tr1X_bX_L3"
df.at["tr1D_bD_L3", "Code Name"] = "sliceD_L3, slD_L3, tr1D_bD_L3"
df.at["tr1_b_L4", "Code Name"] = "slice_L4, sl_L4, tr1_b_L4"
df.at["tr1X_bX_L4", "Code Name"] = "sliceX_L4, slX_L4, tr1X_bX_L4"
df.at["tr1D_bD_L4", "Code Name"] = "sliceD_L4, slD_L4, tr1D_bD_L4"

df.at["f1_f1", "Code Name"] = "ocf, f1_f1"
df.at["f1X_f1X", "Code Name"] = "ocfX, f1X_f1X"
df.at["f1D_f1D", "Code Name"] = "ocfD, f1D_f1D"
df.at["f1_f1_R4", "Code Name"] = "ocf_R4, f1_f1_R4"
df.at["f1X_f1X_R4", "Code Name"] = "ocfX_R4, f1X_f1X_R4"
df.at["f1D_f1D_R4", "Code Name"] = "ocfD_R4, f1D_f1D_R4"
df.at["f1_f1_R3", "Code Name"] = "ocf_R3, f1_f1_R3"
df.at["f1X_f1X_R3", "Code Name"] = "ocfX_R3, f1X_f1X_R3"
df.at["f1D_f1D_R3", "Code Name"] = "ocfD_R3, f1D_f1D_R3"
df.at["f1_f1_L3", "Code Name"] = "ocf_L3, f1_f1_L3"
df.at["f1X_f1X_L3", "Code Name"] = "ocfX_L3, f1X_f1X_L3"
df.at["f1D_f1D_L3", "Code Name"] = "ocfD_L3, f1D_f1D_L3"
df.at["f1_f1_L4", "Code Name"] = "ocf_L4, f1_f1_L4"
df.at["f1X_f1X_L4", "Code Name"] = "ocfX_L4, f1X_f1X_L4"
df.at["f1D_f1D_L4", "Code Name"] = "ocfD_L4, f1D_f1D_L4"

df.at["f2_f2", "Code Name"] = "tcf, f2_f2"
df.at["f2X_f2X", "Code Name"] = "tcfX, f2X_f2X"
df.at["f2D_f2D", "Code Name"] = "tcfD, f2D_f2D"
df.at["f2_f2_R4", "Code Name"] = "tcf_R4, f2_f2_R4"
df.at["f2X_f2X_R4", "Code Name"] = "tcfX_R4, f2X_f2X_R4"
df.at["f2D_f2D_R4", "Code Name"] = "tcfD_R4, f2D_f2D_R4"
df.at["f2_f2_R3", "Code Name"] = "tcf_R3, f2_f2_R3"
df.at["f2X_f2X_R3", "Code Name"] = "tcfX_R3, f2X_f2X_R3"
df.at["f2D_f2D_R3", "Code Name"] = "tcfD_R3, f2D_f2D_R3"
df.at["f2_f2_L3", "Code Name"] = "tcf_L3, f2_f2_L3"
df.at["f2X_f2X_L3", "Code Name"] = "tcfX_L3, f2X_f2X_L3"
df.at["f2D_f2D_L3", "Code Name"] = "tcfD_L3, f2D_f2D_L3"
df.at["f2_f2_L4", "Code Name"] = "tcf_L4, f2_f2_L4"
df.at["f2X_f2X_L4", "Code Name"] = "tcfX_L4, f2X_f2X_L4"
df.at["f2D_f2D_L4", "Code Name"] = "tcfD_L4, f2D_f2D_L4"

df.at["~bD_f1D_R3", "Code Name"] = "tazer1, lazer1, ~bD_f1D_R3"
df.at["~bD_f2D_R4", "Code Name"] = "tazer2, lazer2, ~bD_f2D_R4"

### add special scratches

special_scratches = [
    [
        "scribble", 
        "scribble, sc",         
        1, 
        4, 
        0, 
        "Yes", 
        "1/2", 
        "b_b * 2 / 1", 
        "https://www.youtube.com/watch?v=rtqTmUVjsuY",
    ],
    [
        "drills", 
        "drills, dr",             
        1, 
        8, 
        0, 
        "Yes", 
        "1/2", 
        "b_b * 4 / 1", 
        ""
    ],
    [
        "swingflare", 
        "sf",                 
        1, 
        4, 
        3, 
        "Yes", 
        "???", 
        "(sl + c + ~c) / 1", 
        "https://www.youtube.com/watch?v=h3o5OTIy-kQ",
    ],
    [
        "chirpflare1", 
        "chirpflare1, cf1",  
        1, 
        4, 
        2, 
        "Yes", 
        "???", 
        "(c / (1/3) + f1_f1 / (2/3)) / 2", 
        "https://www.youtube.com/watch?v=DUaY6gMONmA",
    ],
    [
        "chirpflare2", 
        "chirpflare2, cf2",  
        2, 
        6, 
        4, 
        "Yes", 
        "???", 
        "c / (1/2) + f2_f2 / (3/2)", 
        "",
    ],
    [
        "prizm", 
        "prizm, pr",               
        2, 
        6, 
        5, 
        "Yes", 
        "???", 
        "(f1 + ~tr1 / (1/2) + tr1 / (1/2) + ~tr2) / 2", 
        "https://www.youtube.com/watch?v=B32m9Jqqrpo",
        ],
    [
        "slicecut", 
        "slicecut, slc",        
        1, 
        3, 
        2, 
        "No",  
        "???", 
        "sl / (2/3) + tr1 / (1/3)", 
        "",
    ],
    [
        "boomerang", 
        "boomerang, boom, bo", 
        2, 
        6, 
        4, 
        "Yes", 
        "???", 
        "slc + ~slc", 
        "https://www.youtube.com/watch?v=c2IrbYGs0eU",
    ],
    [
        "autobahn", 
        "autobahn, ab",         
        3, 
        9, 
        7, 
        "Yes", 
        "???", 
        "sl // (1/3) / (2/3) + ct1 // (2/3) / (2/3) + (~b // (1/3) / (1/3) + ct1 // (2/3) / (2/3)).yshift(1/3) + ~ct1 / (2/3)", 
        "https://www.youtube.com/watch?v=nqzwiWkKV_s",
    ],
    [
        "seesaw", 
        "seesaw, ss",             
        1, 
        4, 
        2, 
        "Yes", 
        "???", "(b + ~b + g + ~b + b + ~g) / 1", 
        "https://www.youtube.com/watch?v=6ZHYnUdPw3g&t=141s",
    ],
]