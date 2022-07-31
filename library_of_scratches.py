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

# https://math.stackexchange.com/questions/501598/define-y-value-from-the-equation-of-circle
def _N(x):
    return (-np.cos(np.pi * x) + 1) / 2
def _NR(x):
    return (np.cos(np.pi * x) + 1) / 2
def _Ex(x):
    return 1 - np.sqrt(1 - (x ** 2))
def _ExR(x):
    return np.sqrt(1 - ((x - 0) ** 2))
def _Log(x):
    return np.sqrt(1 - ((x - 1) ** 2))
def _LogR(x):
    return 1 - np.sqrt(1 - ((x - 1) ** 2))

finv = {
    _N:_NR,
    _NR:_N,
    _Ex:_ExR,
    _ExR:_Ex,
    _Log:_LogR,
    _LogR:_Log,
}

fneg = {
    _N:_NR,
    _NR:_N,
    _Ex:_LogR,
    _ExR:_Log,
    _Log:_ExR,
    _LogR:_Ex,
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
bEx = Scratch([[_1s[0], _Ex, "k", _]])
bLog = Scratch([[_1s[0], _Log, "k", _]])

g = Scratch([[_1s[0], _N, "w", _]])
gEx = Scratch([[_1s[0], _Ex, "w", _]])
gLog = Scratch([[_1s[0], _Log, "w", _]])

tr1 = Scratch([[_1s[0], _N, "k", _0]])
tr1Ex = Scratch([[_1s[0], _Ex, "k", _0]])
tr1Log = Scratch([[_1s[0], _Log, "k", _0]])

tr2 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _2))]])
tr2Ex = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _2))]])
tr2Log = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _2))]])
tr2D = Scratch([[_1s[0], _N, "k", np.hstack((_0, _3[:1]))]])
tr2DEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _3[:1]))]])
tr2DLog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _3[:1]))]])
tr2A = Scratch([[_1s[0], _N, "k", np.hstack((_0, _3[1:]))]])
tr2AEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _3[1:]))]])
tr2ALog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _3[1:]))]])

tr3 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _3))]])
tr3Ex = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _3))]])
tr3Log = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _3))]])
tr3D = Scratch([[_1s[0], _N, "k", np.hstack((_0, _4[:2]))]])
tr3DEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _4[:2]))]])
tr3DLog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _4[:2]))]])
tr3A = Scratch([[_1s[0], _N, "k", np.hstack((_0, _4[1:]))]])
tr3AEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _4[1:]))]])
tr3ALog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _4[1:]))]])
tr3S = Scratch([[_1s[0], _N, "k", np.hstack((_0, _4[0], _4[2]))]])
tr3SEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _4[0], _4[2]))]])
tr3SLog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _4[0], _4[2]))]])

tr4 = Scratch([[_1s[0], _N, "k", np.hstack((_0, _4))]])
tr4Ex = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _4))]])
tr4Log = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _4))]])
tr4D = Scratch([[_1s[0], _N, "k", np.hstack((_0, _5[:3]))]])
tr4DEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _5[:3]))]])
tr4DLog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _5[:3]))]])
tr4A = Scratch([[_1s[0], _N, "k", np.hstack((_0, _5[1:]))]])
tr4AEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, _5[1:]))]])
tr4ALog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, _5[1:]))]])
tr4S = Scratch([[_1s[0], _N, "k", np.hstack((_0, 1/2, _5[0], _5[3]))]])
tr4SEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_0, 1/2, _5[0], _5[3]))]])
tr4SLog = Scratch([[_1s[0], _Log, "k", np.hstack((_0, 1/2, _5[0], _5[3]))]])

f1 = Scratch([[_1s[0], _N, "k", _2]])
f1Ex = Scratch([[_1s[0], _Ex, "k", _2]])
f1Log = Scratch([[_1s[0], _Log, "k", _2]])
f1D = Scratch([[_1s[0], _N, "k", _3[:1]]])
f1DEx = Scratch([[_1s[0], _Ex, "k", _3[:1]]])
f1DLog = Scratch([[_1s[0], _Log, "k", _3[:1]]])
f1A = Scratch([[_1s[0], _N, "k", _3[1:]]])
f1AEx = Scratch([[_1s[0], _Ex, "k", _3[1:]]])
f1ALog = Scratch([[_1s[0], _Log, "k", _3[1:]]])

f2 = Scratch([[_1s[0], _N, "k", _3]])
f2Ex = Scratch([[_1s[0], _Ex, "k", _3]])
f2Log = Scratch([[_1s[0], _Log, "k", _3]])
f2D = Scratch([[_1s[0], _N, "k", _4[:2]]])
f2DEx = Scratch([[_1s[0], _Ex, "k", _4[:2]]])
f2DLog = Scratch([[_1s[0], _Log, "k", _4[:2]]])
f2A = Scratch([[_1s[0], _N, "k", _4[1:]]])
f2AEx = Scratch([[_1s[0], _Ex, "k", _4[1:]]])
f2ALog = Scratch([[_1s[0], _Log, "k", _4[1:]]])
f2S = Scratch([[_1s[0], _N, "k", np.hstack((_4[0], _4[2]))]])
f2SEx = Scratch([[_1s[0], _Ex, "k", np.hstack((_4[0], _4[2]))]])
f2SLog = Scratch([[_1s[0], _Log, "k", np.hstack((_4[0], _4[2]))]])

f3 = Scratch([[_1s[0], _N, "k", _4]])
f3Ex = Scratch([[_1s[0], _Ex, "k", _4]])
f3Log = Scratch([[_1s[0], _Log, "k", _4]])
f3D = Scratch([[_1s[0], _N, "k", _5[:3]]])
f3DEx = Scratch([[_1s[0], _Ex, "k", _5[:3]]])
f3DLog = Scratch([[_1s[0], _Log, "k", _5[:3]]])
f3A = Scratch([[_1s[0], _N, "k", _5[1:]]])
f3AEx = Scratch([[_1s[0], _Ex, "k", _5[1:]]])
f3ALog = Scratch([[_1s[0], _Log, "k", _5[1:]]])
f3S = Scratch([[_1s[0], _N, "k", np.hstack((1/2, _5[0], _5[3]))]])
f3SEx = Scratch([[_1s[0], _Ex, "k", np.hstack((1/2, _5[0], _5[3]))]])
f3SLog = Scratch([[_1s[0], _Log, "k", np.hstack((1/2, _5[0], _5[3]))]])

f4 = Scratch([[_1s[0], _N, "k", _5]])
f4Ex = Scratch([[_1s[0], _Ex, "k", _5]])
f4Log = Scratch([[_1s[0], _Log, "k", _5]])
f4D = Scratch([[_1s[0], _N, "k", _6[:4]]])
f4DEx = Scratch([[_1s[0], _Ex, "k", _6[:4]]])
f4DLog = Scratch([[_1s[0], _Log, "k", _6[:4]]])
f4A = Scratch([[_1s[0], _N, "k", _6[1:]]])
f4AEx = Scratch([[_1s[0], _Ex, "k", _6[1:]]])
f4ALog = Scratch([[_1s[0], _Log, "k", _6[1:]]])
f4S = Scratch([[_1s[0], _N, "k", np.hstack((1/2, _6[0], _6[3]))]])
f4SEx = Scratch([[_1s[0], _Ex, "k", np.hstack((1/2, _6[0], _6[3]))]])
f4SLog = Scratch([[_1s[0], _Log, "k", np.hstack((1/2, _6[0], _6[3]))]])

### Tears
#############################################################

t1N = t1 = Scratch([[_s, _N, "k", _] for _s in steps(2)])
t1Ex = Scratch([[_s, _Ex, "k", _] for _s in steps(2)])
t1Log = Scratch([[_s, _Log, "k", _] for _s in steps(2)])

t2N = t2 = Scratch([[_s, _N, "k", _] for _s in steps(3)])
t2Ex = Scratch([[_s, _Ex, "k", _] for _s in steps(3)])
t2Log = Scratch([[_s, _Log, "k", _] for _s in steps(3)])

t3N = t3 = Scratch([[_s, _N, "k", _] for _s in steps(4)])
t3Ex = Scratch([[_s, _Ex, "k", _] for _s in steps(4)])
t3Log = Scratch([[_s, _Log, "k", _] for _s in steps(4)])

t4N = t4 = Scratch([[_s, _N, "k", _] for _s in steps(5)])
t4Ex = Scratch([[_s, _Ex, "k", _] for _s in steps(5)])
t4Log = Scratch([[_s, _Log, "k", _] for _s in steps(5)])

ct1N = ct1 = Scratch([[_s, _N, "k", _0] for _s in steps(2)])
ct1Ex = Scratch([[_s, _Ex, "k", _0] for _s in steps(2)])
ct1Log = Scratch([[_s, _Log, "k", _0] for _s in steps(2)])

ct2N = ct2 = Scratch([[_s, _N, "k", _0] for _s in steps(3)])
ct2Ex = Scratch([[_s, _Ex, "k", _0] for _s in steps(3)])
ct2Log = Scratch([[_s, _Log, "k", _0] for _s in steps(3)])

ct3N = ct3 = Scratch([[_s, _N, "k", _0] for _s in steps(4)])
ct3Ex = Scratch([[_s, _Ex, "k", _0] for _s in steps(4)])
ct3Log = Scratch([[_s, _Log, "k", _0] for _s in steps(4)])

ct4N = ct4 = Scratch([[_s, _N, "k", _0] for _s in steps(5)])
ct4Ex = Scratch([[_s, _Ex, "k", _0] for _s in steps(5)])
ct4Log = Scratch([[_s, _Log, "k", _0] for _s in steps(5)])

### Orbits, Special Scratches, and DataFrame
#############################################################

from itertools import permutations
from itertools import combinations_with_replacement
import re
import pandas as pd

### make elements and formulas

letters = {
    "b":   (1, 0),
    "g":   (0, 0),
    "tr1": (1, 1),
    "tr2": (2, 2),
    "tr2D":(2, 2),
    "tr2A":(2, 2),
    "tr3": (3, 3),
    "tr3D":(3, 3),
    "tr3A":(3, 3),
    "tr3S":(3, 3),
    "tr4": (4, 4),
    "tr4D":(4, 4),
    "tr4A":(4, 4),
    "tr4S":(4, 4),
    "f1":  (2, 1),
    "f1D": (2, 1),
    "f1A": (2, 1),
    "f2":  (3, 2),
    "f2D": (3, 2),
    "f2A": (3, 2),
    "f2S": (3, 2),
    "f3":  (4, 3),
    "f3D": (4, 3),
    "f3A": (4, 3),
    "f3S": (4, 3),
    "f4":  (5, 4),
    "f4D": (5, 4),
    "f4A": (5, 4),
    "f4S": (5, 4),
    "t1":  (2, 0),
    "t2":  (3, 0),
    "t3":  (4, 0),
    "t4":  (5, 0),
    "ct1": (2, 1),
    "ct2": (3, 2),
    "ct3": (4, 3),
    "ct4": (5, 4),
}
curves = ["", "Ex", "Log"]
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
#     els = re.sub(r"[XDN]|_[RL][3,4]", "", name).split("_")
    els = re.sub(r"(?:Ex|Log)|_[RL][3,4]", "", name).split("_")
    return (
        sum(letters[i][0] for i in els), 
        sum(letters[i][1] for i in els),
    )

def isOrbit(name):
    return "Yes" if "_" in name else "No"


### make table

data_elements = [[
    name,
    name,
    1,
    *soundsAndClicks(name),
    isOrbit(name),
    " is element",
    "",
    999,
] for name in elements]

data_composites = [[
    name,
    name,
    1,
    *soundsAndClicks(name),
    isOrbit(name),
    expression,
    "",
    999,
] for name, expression in [f.split(" = ") for f in formulas]]

columns = [
        "Name", 
        "CodeName",
        "#Counts",
        "#Sounds", 
        "#Pauses",
        "Orbit", 
        "Composition",
        "Tutorial",
        "MostImportant"
    ]

df = pd.DataFrame(
    data=data_elements + data_composites,
    index=[i[0] for i in data_elements + data_composites],
    columns=columns,
)



### extra_data

extra_data = {
    
    # Baby
    "b":{
        "Name":"Baby",
        "CodeName":"baby",
    },
    "bEx":{
        "Name":"Baby (Ex-Curve)",
        "CodeName":"babyX",
    },
    "bLog":{
        "Name":"Baby (Log-Curve)",
        "CodeName":"babyD",
    },
    
    # Ghost
    "g":{
        "Name":"Ghost",
        "CodeName":"ghost",
    },
    "gEx":{
        "Name":"Ghost (Ex-Curve)",
        "CodeName":"ghostEx",
    },
    "gLog":{
        "Name":"Ghost (Log-Curve)",
        "CodeName":"ghostLog",
    },
    
    # Transformers
    "tr1":{
        "Name":"1-Click-Transformer",
        "CodeName":"trans1",
    },
    "tr1Ex":{
        "Name":"1-Click-Transformer (Ex-Curve)",
        "CodeName":"trans1Ex",
    },
    "tr1Log":{
        "Name":"1-Click-Transformer (Log-Curve)",
        "CodeName":"trans1Log",
    },
    "tr2":{
        "Name":"2-Click-Transformer",
        "CodeName":"trans2",
    },
    "tr2Ex":{
        "Name":"2-Click-Transformer (Ex-Curve)",
        "CodeName":"trans2Ex",
    },
    "tr2Log":{
        "Name":"2-Click-Transformer (Log-Curve)",
        "CodeName":"trans2Log",
    },
    "tr2D":{
        "Name":"2-Click-Transformer (Diminished)",
        "CodeName":"trans2D",
    },
    "tr2DEx":{
        "Name":"2-Click-Transformer (Diminished, Ex-Curve)",
        "CodeName":"trans2DEx",
    },
    "tr2DLog":{
        "Name":"2-Click-Transformer (Diminished, Log-Curve)",
        "CodeName":"trans2DLog",
    },
    "tr2A":{
        "Name":"2-Click-Transformer (Augmented)",
        "CodeName":"trans2A",
    },
    "tr2AEx":{
        "Name":"2-Click-Transformer (Augmented, Ex-Curve)",
        "CodeName":"trans2AEx",
    },
    "tr2ALog":{
        "Name":"2-Click-Transformer (Augmented, Log-Curve)",
        "CodeName":"trans2ALog",
    },
    "tr3":{
        "Name":"3-Click-Transformer",
        "CodeName":"trans3",
    },
    "tr3Ex":{
        "Name":"3-Click-Transformer (Ex-Curve)",
        "CodeName":"trans3Ex",
    },
    "tr3Log":{
        "Name":"3-Click-Transformer (Log-Curve)",
        "CodeName":"trans3Log",
    },
    "tr3D":{
        "Name":"3-Click-Transformer (Diminished)",
        "CodeName":"trans3D",
    },
    "tr3DEx":{
        "Name":"3-Click-Transformer (Diminished, Ex-Curve)",
        "CodeName":"trans3DEx",
    },
    "tr3DLog":{
        "Name":"3-Click-Transformer (Diminished, Log-Curve)",
        "CodeName":"trans3DLog",
    },
    "tr3A":{
        "Name":"3-Click-Transformer (Augmented)",
        "CodeName":"trans3A",
    },
    "tr3AEx":{
        "Name":"3-Click-Transformer (Augmented, Ex-Curve)",
        "CodeName":"trans3AEx",
    },
    "tr3ALog":{
        "Name":"3-Click-Transformer (Augmented, Log-Curve)",
        "CodeName":"trans3ALog",
    },
    "tr3S":{
        "Name":"3-Click-Transformer (Stretched)",
        "CodeName":"trans3S",
    },
    "tr3SEx":{
        "Name":"3-Click-Transformer (Stretched, Ex-Curve)",
        "CodeName":"trans3SEx",
    },
    "tr3SLog":{
        "Name":"3-Click-Transformer (Stretched, Log-Curve)",
        "CodeName":"trans3SLog",
    },
    "tr4":{
        "Name":"4-Click-Transformer",
        "CodeName":"trans4",
    },
    "tr4Ex":{
        "Name":"4-Click-Transformer (Ex-Curve)",
        "CodeName":"trans4Ex",
    },
    "tr4Log":{
        "Name":"4-Click-Transformer (Log-Curve)",
        "CodeName":"trans4Log",
    },
    "tr4D":{
        "Name":"4-Click-Transformer (Diminished)",
        "CodeName":"trans4D",
    },
    "tr4DEx":{
        "Name":"4-Click-Transformer (Diminished, Ex-Curve)",
        "CodeName":"trans4DEx",
    },
    "tr4DLog":{
        "Name":"4-Click-Transformer (Diminished, Log-Curve)",
        "CodeName":"trans4DLog",
    },
    "tr4A":{
        "Name":"4-Click-Transformer (Augmented)",
        "CodeName":"trans4A",
    },
    "tr4AEx":{
        "Name":"4-Click-Transformer (Augmented, Ex-Curve)",
        "CodeName":"trans4AEx",
    },
    "tr4ALog":{
        "Name":"4-Click-Transformer (Augmented, Log-Curve)",
        "CodeName":"trans4ALog",
    },
    "tr4S":{
        "Name":"4-Click-Transformer (Stretched)",
        "CodeName":"trans4S",
    },
    "tr4SEx":{
        "Name":"4-Click-Transformer (Stretched, Ex-Curve)",
        "CodeName":"trans4SEx",
    },
    "tr4SLog":{
        "Name":"4-Click-Transformer (Stretched, Log-Curve)",
        "CodeName":"trans4SLog",
    },
    
    # Flares
    "f1":{
        "Name":"1-Click-Flare",
        "CodeName":"flare1",
    },
    "f1Ex":{
        "Name":"1-Click-Flare (Ex-Curve)",
        "CodeName":"flare1Ex",
    },
    "f1Log":{
        "Name":"1-Click-Flare (Log-Curve)",
        "CodeName":"flare1Log",
    },
    "f1D":{
        "Name":"1-Click-Flare (Diminished)",
        "CodeName":"flare1D",
    },
    "f1DEx":{
        "Name":"1-Click-Flare (Diminished, Ex-Curve)",
        "CodeName":"flare1DEx",
    },
    "f1DLog":{
        "Name":"1-Click-Flare (Diminished, Log-Curve)",
        "CodeName":"flare1DLog",
    },
    "f1A":{
        "Name":"1-Click-Flare (Augmented)",
        "CodeName":"flare1A",
    },
    "f1AEx":{
        "Name":"1-Click-Flare (Augmented, Ex-Curve)",
        "CodeName":"flare1AEx",
    },
    "f1ALog":{
        "Name":"1-Click-Flare (Augmented, Log-Curve)",
        "CodeName":"flare1ALog",
    },
    "f2":{
        "Name":"2-Click-Flare",
        "CodeName":"flare2",
    },
    "f2Ex":{
        "Name":"2-Click-Flare (Ex-Curve)",
        "CodeName":"flare2Ex",
    },
    "f2Log":{
        "Name":"2-Click-Flare (Log-Curve)",
        "CodeName":"flare2Log",
    },
    "f2D":{
        "Name":"2-Click-Flare (Diminished)",
        "CodeName":"flare2D",
    },
    "f2DEx":{
        "Name":"2-Click-Flare (Diminished, Ex-Curve)",
        "CodeName":"flare2DEx",
    },
    "f2DLog":{
        "Name":"2-Click-Flare (Diminished, Log-Curve)",
        "CodeName":"flare2DLog",
    },
    "f2A":{
        "Name":"2-Click-Flare (Augmented)",
        "CodeName":"flare2A",
    },
    "f2AEx":{
        "Name":"2-Click-Flare (Augmented, Ex-Curve)",
        "CodeName":"flare2AEx",
    },
    "f2ALog":{
        "Name":"2-Click-Flare (Augmented, Log-Curve)",
        "CodeName":"flare2ALog",
    },
    "f2S":{
        "Name":"2-Click-Flare (Stretched)",
        "CodeName":"flare2S",
    },
    "f2SEx":{
        "Name":"2-Click-Flare (Stretched, Ex-Curve)",
        "CodeName":"flare2SEx",
    },
    "f2SLog":{
        "Name":"2-Click-Flare (Stretched, Log-Curve)",
        "CodeName":"flare2SLog",
    },
    "f3":{
        "Name":"3-Click-Flare",
        "CodeName":"flare3",
    },
    "f3Ex":{
        "Name":"3-Click-Flare (Ex-Curve)",
        "CodeName":"flare3Ex",
    },
    "f3Log":{
        "Name":"3-Click-Flare (Log-Curve)",
        "CodeName":"flare3Log",
    },
    "f3D":{
        "Name":"3-Click-Flare (Diminished)",
        "CodeName":"flare3D",
    },
    "f3DEx":{
        "Name":"3-Click-Flare (Diminished, Ex-Curve)",
        "CodeName":"flare3DEx",
    },
    "f3DLog":{
        "Name":"3-Click-Flare (Diminished, Log-Curve)",
        "CodeName":"flare3DLog",
    },
    "f3A":{
        "Name":"3-Click-Flare (Augmented)",
        "CodeName":"flare3A",
    },
    "f3AEx":{
        "Name":"3-Click-Flare (Augmented, Ex-Curve)",
        "CodeName":"flare3AEx",
    },
    "f3ALog":{
        "Name":"3-Click-Flare (Augmented, Log-Curve)",
        "CodeName":"flare3ALog",
    },
    "f3S":{
        "Name":"3-Click-Flare (Stretched)",
        "CodeName":"flare3S",
    },
    "f3SEx":{
        "Name":"3-Click-Flare (Stretched, Ex-Curve)",
        "CodeName":"flare3SEx",
    },
    "f3SLog":{
        "Name":"3-Click-Flare (Stretched, Log-Curve)",
        "CodeName":"flare3SLog",
    },
    "f4":{
        "Name":"4-Click-Flare",
        "CodeName":"flare4",
    },
    "f4Ex":{
        "Name":"4-Click-Flare (Ex-Curve)",
        "CodeName":"flare4Ex",
    },
    "f4Log":{
        "Name":"4-Click-Flare (Log-Curve)",
        "CodeName":"flare4Log",
    },
    "f4D":{
        "Name":"4-Click-Flare (Diminished)",
        "CodeName":"flare4D",
    },
    "f4DEx":{
        "Name":"4-Click-Flare (Diminished, Ex-Curve)",
        "CodeName":"flare4DEx",
    },
    "f4DLog":{
        "Name":"4-Click-Flare (Diminished, Log-Curve)",
        "CodeName":"flare4DLog",
    },
    "f4A":{
        "Name":"4-Click-Flare (Augmented)",
        "CodeName":"flare4A",
    },
    "f4AEx":{
        "Name":"4-Click-Flare (Augmented, Ex-Curve)",
        "CodeName":"flare4AEx",
    },
    "f4ALog":{
        "Name":"4-Click-Flare (Augmented, Log-Curve)",
        "CodeName":"flare4ALog",
    },
    "f4S":{
        "Name":"4-Click-Flare (Stretched)",
        "CodeName":"flare4S",
    },
    "f4SEx":{
        "Name":"4-Click-Flare (Stretched, Ex-Curve)",
        "CodeName":"flare4SEx",
    },
    "f4SLog":{
        "Name":"4-Click-Flare (Stretched, Log-Curve)",
        "CodeName":"flare4SLog",
    },
    
    
    # Tears
    "t1":{
        "Name":"1-Tear",
        "CodeName":"tear1",
    },
    "t1Ex":{
        "Name":"1-Tear (Ex-Curve)",
        "CodeName":"tear1Ex",
    },
    "t1Log":{
        "Name":"1-Tear (Log-Curve)",
        "CodeName":"tear1Log",
    },
    "t2":{
        "Name":"2-Tear",
        "CodeName":"tear2",
    },
    "t2Ex":{
        "Name":"2-Tear (Ex-Curve)",
        "CodeName":"tear2Ex",
    },
    "t2Log":{
        "Name":"2-Tear (Log-Curve)",
        "CodeName":"tear2Log",
    },
    "t3":{
        "Name":"3-Tear",
        "CodeName":"tear3",
    },
    "t3Ex":{
        "Name":"3-Tear (Ex-Curve)",
        "CodeName":"tear3Ex",
    },
    "t3Log":{
        "Name":"3-Tear (Log-Curve)",
        "CodeName":"tear3Log",
    },
    "t4":{
        "Name":"4-Tear",
        "CodeName":"tear4",
    },
    "t4Ex":{
        "Name":"4-Tear (Ex-Curve)",
        "CodeName":"tear4Ex",
    },
    "t4Log":{
        "Name":"4-Tear (Log-Curve)",
        "CodeName":"tear4Log",
    },
    
    # Click Tears
    "ct1":{
        "Name":"1-Click-Tear",
        "CodeName":"clicktear1",
    },
    "ct1Ex":{
        "Name":"1-Click-Tear (Ex-Curve)",
        "CodeName":"clicktear1Ex",
    },
    "ct1Log":{
        "Name":"1-Click-Tear (Log-Curve)",
        "CodeName":"clicktear1Log",
    },
    "ct2":{
        "Name":"2-Click-Tear",
        "CodeName":"clicktear2",
    },
    "ct2Ex":{
        "Name":"2-Click-Tear (Ex-Curve)",
        "CodeName":"clicktear2Ex",
    },
    "ct2Log":{
        "Name":"2-Click-Tear (Log-Curve)",
        "CodeName":"clicktear2Log",
    },
    "ct3":{
        "Name":"3-Click-Tear",
        "CodeName":"clicktear3",
    },
    "ct3Ex":{
        "Name":"3-Click-Tear (Ex-Curve)",
        "CodeName":"clicktear3Ex",
    },
    "ct3Log":{
        "Name":"3-Click-Tear (Log-Curve)",
        "CodeName":"clicktear3Log",
    },
     "ct4":{
        "Name":"4-Click-Tear",
        "CodeName":"clicktear4",
    },
    "ct4Ex":{
        "Name":"4-Click-Tear (Ex-Curve)",
        "CodeName":"clicktear4Ex",
    },
    "ct4Log":{
        "Name":"4-Click-Tear (Log-Curve)",
        "CodeName":"clicktear4Log",
    },
    
    # Baby-Orbits
    "b_b":{
        "Name":"Baby-Orbit",
        "CodeName":"babyorbit, bo",
    },
    "bEx_bEx":{
        "Name":"Baby-Orbit (Ex-Curve)",
        "CodeName":"babyorbitEx, boEx",
    },
    "bLog_bLog":{
        "Name":"Baby-Orbit (Log-Curve)",
        "CodeName":"babyorbitLog, boLog",
    },
    "b_b_R4":{
        "Name":"Baby-Orbit (Right-Skewed at 1/4)",
        "CodeName":"babyorbit_R4, bo_R4",
    },
    "bEx_bEx_R4":{
        "Name":"Baby-Orbit (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"babyorbitEx_R4, boEx_R4",
    },
    "bLog_bLog_R4":{
        "Name":"Baby-Orbit (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"babyorbitLog_R4, boLog_R4",
    },
    "b_b_R3":{
        "Name":"Baby-Orbit (Right-Skewed at 1/3)",
        "CodeName":"babyorbit_R3, bo_R3",
    },
    "bEx_bEx_R3":{
        "Name":"Baby-Orbit (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"babyorbitEx_R3, boEx_R3",
    },
    "bLog_bLog_R3":{
        "Name":"Baby-Orbit (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"babyorbitLog_R3, boLog_R3",
    },
    "b_b_L3":{
        "Name":"Baby-Orbit (Left-Skewed at 1/3)",
        "CodeName":"babyorbit_L3, bo_L3",
    },
    "bEx_bEx_L3":{
        "Name":"Baby-Orbit (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"babyorbitEx_L3, boEx_L3",
    },
    "bLog_bLog_L3":{
        "Name":"Baby-Orbit (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"babyorbitLog_L3, boLog_L3",
    },
    "b_b_L4":{
        "Name":"Baby-Orbit (Left-Skewed at 1/4)",
        "CodeName":"babyorbit_L4, bo_L4",
    },
    "bEx_bEx_L4":{
        "Name":"Baby-Orbit (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"babyorbitEx_L4, boEx_L4",
    },
    "bLog_bLog_L4":{
        "Name":"Baby-Orbit (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"babyorbitLog_L4, boLog_L4",
    },
    
    # Stabs
    "b_g":{
        "Name":"Stab",
        "CodeName":"stab, st",
    },
    "bEx_gEx":{
        "Name":"Stab (Ex-Curve)",
        "CodeName":"stabEx, stEx",
    },
    "bLog_gLog":{
        "Name":"Stab (Log-Curve)",
        "CodeName":"stabLog, stLog",
    },
    "b_g_R4":{
        "Name":"Stab (Right-Skewed at 1/4)",
        "CodeName":"stab_R4, st_R4",
    },
    "bEx_gEx_R4":{
        "Name":"Stab (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"stabEx_R4, stEx_R4",
    },
    "bLog_gLog_R4":{
        "Name":"Stab (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"stabLog_R4, stLog_R4",
    },
    "b_g_R3":{
        "Name":"Stab (Right-Skewed at 1/3)",
        "CodeName":"stab_R3, st_R3",
    },
    "bEx_gEx_R3":{
        "Name":"Stab (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"stabEx_R3, stEx_R3",
    },
    "bLog_gLog_R3":{
        "Name":"Stab (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"stabLog_R3, stLog_R3",
    },
    "b_g_L3":{
        "Name":"Stab (Left-Skewed at 1/3)",
        "CodeName":"stab_L3, st_L3",
    },
    "bEx_gEx_L3":{
        "Name":"Stab (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"stabEx_L3, stEx_L3",
    },
    "bLog_gLog_L3":{
        "Name":"Stab (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"stabLog_L3, stLog_L3",
    },
    "b_g_L4":{
        "Name":"Stab (Left-Skewed at 1/4)",
        "CodeName":"stab_L4, st_L4",
    },
    "bEx_gEx_L4":{
        "Name":"Stab (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"stabEx_L4, stEx_L4",
    },
    "bLog_gLog_L4":{
        "Name":"Stab (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"stabLog_L4, stLog_L4",
    },
    
    # Chirps
    "b_tr1":{
        "Name":"Chirp",
        "CodeName":"chirp, c",
    },
    "bEx_tr1Ex":{
        "Name":"Chirp (Ex-Curve)",
        "CodeName":"chirpEx, cEx",
    },
    "bLog_tr1Log":{
        "Name":"Chirp (Log-Curve)",
        "CodeName":"chirpLog, cLog",
    },
    "b_tr1_R4":{
        "Name":"Chirp (Right-Skewed at 1/4)",
        "CodeName":"chirp_R4, c_R4",
    },
    "bEx_tr1Ex_R4":{
        "Name":"Chirp (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"chirpEx_R4, cEx_R4",
    },
    "bLog_tr1Log_R4":{
        "Name":"Chirp (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"chirpLog_R4, cLog_R4",
    },
    "b_tr1_R3":{
        "Name":"Chirp (Right-Skewed at 1/3)",
        "CodeName":"chirp_R3, c_R3",
    },
    "bEx_tr1Ex_R3":{
        "Name":"Chirp (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"chirpEx_R3, cEx_R3",
    },
    "bLog_tr1Log_R3":{
        "Name":"Chirp (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"chirpLog_R3, cLog_R3",
    },
    "b_tr1_L3":{
        "Name":"Chirp (Left-Skewed at 1/3)",
        "CodeName":"chirp_L3, c_L3",
    },
    "bEx_tr1Ex_L3":{
        "Name":"Chirp (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"chirpEx_L3, cEx_L3",
    },
    "bLog_tr1Log_L3":{
        "Name":"Chirp (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"chirpLog_L3, cLog_L3",
    },
    "b_tr1_L4":{
        "Name":"Chirp (Left-Skewed at 1/4)",
        "CodeName":"chirp_L4, c_L4",
    },
    "bEx_tr1Ex_L4":{
        "Name":"Chirp (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"chirpEx_L4, cEx_L4",
    },
    "bLog_tr1Log_L4":{
        "Name":"Chirp (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"chirpLog_L4, cLog_L4",
    },
    
    # Fakechirps
    "tr1_tr1":{
        "Name":"Fake-Chirp",
        "CodeName":"fakechirp, fc",
    },
    "tr1Ex_tr1Ex":{
        "Name":"Fake-Chirp (Ex-Curve)",
        "CodeName":"fakechirpEx, fcEx",
    },
    "tr1Log_tr1Log":{
        "Name":"Fake-Chirp (Log-Curve)",
        "CodeName":"fakechirpLog, fcLog",
    },
    "tr1_tr1_R4":{
        "Name":"Fake-Chirp (Right-Skewed at 1/4)",
        "CodeName":"fakechirp_R4, fc_R4",
    },
    "tr1Ex_tr1Ex_R4":{
        "Name":"Fake-Chirp (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"fakechirpEx_R4, fcEx_R4",
    },
    "tr1Log_tr1Log_R4":{
        "Name":"Fake-Chirp (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"fakechirpLog_R4, fcLog_R4",
    },
    "tr1_tr1_R3":{
        "Name":"Fake-Chirp (Right-Skewed at 1/3)",
        "CodeName":"fakechirp_R3, fc_R3",
    },
    "tr1Ex_tr1Ex_R3":{
        "Name":"Fake-Chirp (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"fakechirpEx_R3, fcEx_R3",
    },
    "tr1Log_tr1Log_R3":{
        "Name":"Fake-Chirp (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"fakechirpLog_R3, fcLog_R3",
    },
    "tr1_tr1_L3":{
        "Name":"Fake-Chirp (Left-Skewed at 1/3)",
        "CodeName":"fakechirp_L3, fc_L3",
    },
    "tr1Ex_tr1Ex_L3":{
        "Name":"Fake-Chirp (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"fakechirpEx_L3, fcEx_L3",
    },
    "tr1Log_tr1Log_L3":{
        "Name":"Fake-Chirp (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"fakechirpLog_L3, fcLog_L3",
    },
    "tr1_tr1_L4":{
        "Name":"Fake-Chirp (Left-Skewed at 1/4)",
        "CodeName":"fakechirp_L4, fc_L4",
    },
    "tr1Ex_tr1Ex_L4":{
        "Name":"Fake-Chirp (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"fakechirpEx_L4, fcEx_L4",
    },
    "tr1Log_tr1Log_L4":{
        "Name":"Fake-Chirp (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"fakechirpLog_L4, fcLog_L4",
    },
    
    # Slice
    "tr1_b":{
        "Name":"Slice",
        "CodeName":"slice, sl",
    },
    "tr1Ex_bEx":{
        "Name":"Slice (Ex-Curve)",
        "CodeName":"sliceEx, slEx",
    },
    "tr1Log_bLog":{
        "Name":"Slice (Log-Curve)",
        "CodeName":"sliceLog, slLog",
    },
    "tr1_b_R4":{
        "Name":"Slice (Right-Skewed at 1/4)",
        "CodeName":"slice_R4, sl_R4",
    },
    "tr1Ex_bEx_R4":{
        "Name":"Slice (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"sliceEx_R4, slEx_R4",
    },
    "tr1Log_bLog_R4":{
        "Name":"Slice (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"sliceLog_R4, slLog_R4",
    },
    "tr1_b_R3":{
        "Name":"Slice (Right-Skewed at 1/3)",
        "CodeName":"slice_R3, sl_R3",
    },
    "tr1Ex_bEx_R3":{
        "Name":"Slice (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"sliceEx_R3, slEx_R3",
    },
    "tr1Log_bLog_R3":{
        "Name":"Slice (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"sliceLog_R3, slLog_R3",
    },
    "tr1_b_L3":{
        "Name":"Slice (Left-Skewed at 1/3)",
        "CodeName":"slice_L3, sl_L3",
    },
    "tr1Ex_bEx_L3":{
        "Name":"Slice (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"sliceEx_L3, slEx_L3",
    },
    "tr1Log_bLog_L3":{
        "Name":"Slice (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"sliceLog_L3, slLog_L3",
    },
    "tr1_b_L4":{
        "Name":"Slice (Left-Skewed at 1/4)",
        "CodeName":"slice_L4, sl_L4",
    },
    "tr1Ex_bEx_L4":{
        "Name":"Slice (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"sliceEx_L4, slEx_L4",
    },
    "tr1Log_bLog_L4":{
        "Name":"Slice (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"sliceLog_L4, slLog_L4",
    },
    
    # 1-Click Flare Orbits
    "f1_f1":{
        "Name":"1-Click-Flare-Orbit",
        "CodeName":"ocf",
    },
    "f1Ex_f1Ex":{
        "Name":"1-Click-Flare-Orbit (Ex-Curve)",
        "CodeName":"ocfEx",
    },
    "f1Log_f1Log":{
        "Name":"1-Click-Flare-Orbit (Log-Curve)",
        "CodeName":"ocfLog",
    },
    "f1_f1_R4":{
        "Name":"1-Click-Flare-Orbit (Right-Skewed at 1/4)",
        "CodeName":"ocf_R4",
    },
    "f1Ex_f1Ex_R4":{
        "Name":"1-Click-Flare-Orbit (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"ocfEx_R4",
    },
    "f1Log_f1Log_R4":{
        "Name":"1-Click-Flare-Orbit (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"ocfLog_R4",
    },
    "f1_f1_R3":{
        "Name":"1-Click-Flare-Orbit (Right-Skewed at 1/3)",
        "CodeName":"ocf_R3",
    },
    "f1Ex_f1Ex_R3":{
        "Name":"1-Click-Flare-Orbit (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"ocfEx_R3",
    },
    "f1Log_f1Log_R3":{
        "Name":"1-Click-Flare-Orbit (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"ocfLog_R3",
    },
    "f1_f1_L3":{
        "Name":"1-Click-Flare-Orbit (Left-Skewed at 1/3)",
        "CodeName":"ocf_L3",
    },
    "f1Ex_f1Ex_L3":{
        "Name":"1-Click-Flare-Orbit (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"ocfEx_L3",
    },
    "f1Log_f1Log_L3":{
        "Name":"1-Click-Flare-Orbit (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"ocfLog_L3",
    },
    "f1_f1_L4":{
        "Name":"1-Click-Flare-Orbit (Left-Skewed at 1/4)",
        "CodeName":"ocf_L4",
    },
    "f1Ex_f1Ex_L4":{
        "Name":"1-Click-Flare-Orbit (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"ocfEx_L4",
    },
    "f1Log_f1Log_L4":{
        "Name":"1-Click-Flare-Orbit (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"ocfLog_L4",
    },
    
    # 2-Click Flare Orbits
    "f2_f2":{
        "Name":"2-Click-Flare-Orbit",
        "CodeName":"tcf",
    },
    "f2Ex_f2Ex":{
        "Name":"2-Click-Flare-Orbit (Ex-Curve)",
        "CodeName":"tcfEx",
    },
    "f2Log_f2Log":{
        "Name":"2-Click-Flare-Orbit (Log-Curve)",
        "CodeName":"tcfLog",
    },
    "f2_f2_R4":{
        "Name":"2-Click-Flare-Orbit (Right-Skewed at 1/4)",
        "CodeName":"tcf_R4",
    },
    "f2Ex_f2Ex_R4":{
        "Name":"2-Click-Flare-Orbit (Ex-Curve, Right-Skewed at 1/4)",
        "CodeName":"tcfEx_R4",
    },
    "f2Log_f2Log_R4":{
        "Name":"2-Click-Flare-Orbit (Log-Curve, Right-Skewed at 1/4)",
        "CodeName":"tcfLog_R4",
    },
    "f2_f2_R3":{
        "Name":"2-Click-Flare-Orbit (Right-Skewed at 1/3)",
        "CodeName":"tcf_R3",
    },
    "f2Ex_f2Ex_R3":{
        "Name":"2-Click-Flare-Orbit (Ex-Curve, Right-Skewed at 1/3)",
        "CodeName":"tcfEx_R3",
    },
    "f2Log_f2Log_R3":{
        "Name":"2-Click-Flare-Orbit (Log-Curve, Right-Skewed at 1/3)",
        "CodeName":"tcfLog_R3",
    },
    "f2_f2_L3":{
        "Name":"2-Click-Flare-Orbit (Left-Skewed at 1/3)",
        "CodeName":"tcf_L3",
    },
    "f2Ex_f2Ex_L3":{
        "Name":"2-Click-Flare-Orbit (Ex-Curve, Left-Skewed at 1/3)",
        "CodeName":"tcfEx_L3",
    },
    "f2Log_f2Log_L3":{
        "Name":"2-Click-Flare-Orbit (Log-Curve, Left-Skewed at 1/3)",
        "CodeName":"tcfLog_L3",
    },
    "f2_f2_L4":{
        "Name":"2-Click-Flare-Orbit (Left-Skewed at 1/4)",
        "CodeName":"tcf_L4",
    },
    "f2Ex_f2Ex_L4":{
        "Name":"2-Click-Flare-Orbit (Ex-Curve, Left-Skewed at 1/4)",
        "CodeName":"tcfEx_L4",
    },
    "f2Log_f2Log_L4":{
        "Name":"2-Click-Flare-Orbit (Log-Curve, Left-Skewed at 1/4)",
        "CodeName":"tcfLog_L4",
    },
    
}

for name, data in extra_data.items():
    if "Name" in data:
        df.at[name, "Name"] = data["Name"]
    if "CodeName" in data:
        df.at[name, "CodeName"] = f'{data["CodeName"]}, {df.at[name, "CodeName"]}'
    if "Tutorial" in data:
        df.at[name, "Tutorial"] = data["Tutorial"]
        


# ### add tutorials

for name in df.index: # Babies
    if ("_" in name and re.match(r"b(?:Ex|Log)?_b(?:Ex|Log)?", name)) or re.match(r"b(?:Ex|Log)?$", name):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=rtqTmUVjsuY' target='_blank'>DJ Noumenon &#128279;</a>"
for name in df.index: # 1-Click Flares
    if ("_" in name and re.match(r"f1[DAS]?(?:Ex|Log)?_f1(?:Ex|Log)?", name)) or re.match(r"f1[DAS]?(?:Ex|Log)?$", name):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=P33Obuj0zAI' target='_blank'>DJ D-Styles & DJ Melo-D &#128279;</a>"
for name in df.index: # 2-Click Flares
    if ("_" in name and re.match(r"f2[DAS]?(?:Ex|Log)?_f2(?:Ex|Log)?", name)) or re.match(r"f2[DAS]?(?:Ex|Log)?$", name):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=1yqMmsQhnHU' target='_blank'>DJ D-Styles & DJ Babu &#128279;</a>"
for name in df.index: # transformers and pure transformer orbits
    if ("_" in name and re.match(r"tr\d[DAS]?(?:Ex|Log)?_tr\d[DAS]?(?:Ex|Log)?", name)) or re.match(r"tr\d[DAS]?(?:Ex|Log)?$", name):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=XdkNAePjM7o' target='_blank'>DJ Immortal &#128279;</a>"
for name in df.index: # tears and pure tear orbits
    if ("_" in name and re.match(r"t\d(?:Ex|Log)?_t\d(?:Ex|Log)?", name)) or re.match(r"t\d(?:Ex|Log)?$", name):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=WN8ity9B35U' target='_blank'>DJ Angelo &#128279;</a>"
for name in df.index: # Stabs
    if ("_" in name and re.match(r"b(?:Ex|Log)?_g(?:Ex|Log)?", name)):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=Fl-JlMxQlxc' target='_blank'>DJ Dirty Digits &#128279;</a>"
for name in df.index: # chirps
    if ("_" in name and re.match(r"b(?:Ex|Log)?_tr1(?:Ex|Log)?", name)):
        df.at[name, "Tutorial"] = "<a href='https://www.youtube.com/watch?v=pKe3OUKaK2k' target='_blank'>DJ Dirty Digits &#128279;</a>"



### add special scratches

special_scratches = [
    [
        "Scribble", 
        "scribble, sc",         
        1, 
        4, 
        0, 
        "Yes", 
        "b_b * 2 / 1", 
        "<a href='https://www.youtube.com/watch?v=rtqTmUVjsuY' target='_blank'>DJ Noumenon &#128279;</a>",
        999,
    ],
    [
        "Drills", 
        "drills, dr",             
        1, 
        8, 
        0, 
        "Yes", 
        "b_b * 4 / 1", 
        "",
        999,
    ],
    [
        "Swingflare", 
        "sf",                 
        1, 
        4, 
        3, 
        "Yes", 
        "(sl + c + ~c) / 1", 
        "<a href='https://www.youtube.com/watch?v=h3o5OTIy-kQ' target='_blank'>DJ Shiftee &#128279;</a>",
        999,
    ],
    [
        "1-Click-Chirpflare", 
        "chirpflare1, cf1",  
        1, 
        4, 
        2, 
        "Yes", 
        "(c / (1/3) + f1_f1 / (2/3)) / 2", 
        "<a href='https://www.youtube.com/watch?v=DUaY6gMONmA' target='_blank'>DJ Excess &#128279;</a>",
        999,
    ],
    [
        "2-Click-Chirpflare", 
        "chirpflare2, cf2",  
        2, 
        6, 
        4, 
        "Yes", 
        "c / (1/2) + f2_f2 / (3/2)", 
        "",
        999,
    ],
    [
        "Prizm", 
        "prizm, pr",               
        2, 
        6, 
        5, 
        "Yes", 
        "(f1 + ~tr1 / (1/2) + tr1 / (1/2) + ~tr2) / 2", 
        "<a href='https://www.youtube.com/watch?v=B32m9Jqqrpo' target='_blank'>Dj Fast-M &#128279;</a>",
        999,
    ],
    [
        "Slicecut", 
        "slicecut, slc",        
        1, 
        3, 
        2, 
        "No",  
        "sl / (2/3) + tr1 / (1/3)", 
        "",
        999,
    ],
    [
        "Boomerang", 
        "boomerang, boom", 
        2, 
        6, 
        4, 
        "Yes", 
        "slc + ~slc", 
        "<a href='https://www.youtube.com/watch?v=c2IrbYGs0eU' target='_blank'>DJ Dirty Digits &#128279;</a>",
        999,
    ],
    [
        "Autobahn", 
        "autobahn, ab",         
        3, 
        9, 
        7, 
        "Yes", 
        "sl // (1/3) / (2/3) + ct1 // (2/3) / (2/3) + (~b // (1/3) / (1/3) + ct1 // (2/3) / (2/3)).yshift(1/3) + ~ct1 / (2/3)", 
        "<a href='https://www.youtube.com/watch?v=nqzwiWkKV_s' target='_blank'>DJ Dirty Digits &#128279;</a>",
        999,
    ],
    [
        "Seesaw", 
        "seesaw, ss",             
        1, 
        4, 
        2, 
        "Yes", 
        "(b + ~b + g + ~b + b + ~g) / 1", 
        "<a href='https://www.youtube.com/watch?v=6ZHYnUdPw3g&t=141s' target='_blank'>TTM Academy &#128279;</a>",
        999,
    ],
    [
        "1-Click-Tazer", 
        "tazer1, ta1, lazer1, la1",             
        1, 
        3, 
        1, 
        "Yes", 
        "~bLog_f1Log_R3", 
        "<a href='https://www.youtube.com/watch?v=JRaUuXhw6Qk' target='_blank'>DJ ND  &#128279;</a>",
        999,
    ],
    [
        "2-Click-Tazer", 
        "tazer2, ta2, lazer2, la2",             
        1, 
        4,
        2, 
        "Yes", 
        "~bLog_f2Log_R4", 
        "<a href='https://www.youtube.com/watch?v=JRaUuXhw6Qk' target='_blank'>DJ ND  &#128279;</a>",
        999,
    ],
]

df2 = pd.DataFrame(
    data=special_scratches, index=[i[0] for i in special_scratches], columns=columns,
)

df = pd.concat([df, df2])


# most important

for indx, name in enumerate([
    "b_b",
    "Scribble",
    "Drills",
    "b_g",
    "b_tr1",
    "tr1_tr1",
    "tr1_b",
    "f1_f1",
    "f2_f2",
    "1-Click-Chirpflare",
    "2-Click-Chirpflare",
    "Swingflare",
    "Slicecut",
    "Boomerang",
    "Autobahn",
    "Prizm",
    "Seesaw",
    "1-Click-Tazer",
    "2-Click-Tazer",
    "b",
    "tr1",
    "tr2",
    "tr2D",
    "tr2A",
    "tr3",
    "tr3D",
    "tr3A",
    "tr3S",
    "tr4",
    "tr4D",
    "tr4A",
    "tr4S",
    "f1",
    "f1D",
    "f1A",
    "f2",
    "f2D",
    "f2A",
    "f2S",
    "f3",
    "f3D",
    "f3A",
    "f3S",
    "f4",
    "f4D",
    "f4A",
    "f4S",
    "t1",
    "t2",
    "t3",
    "t4",
    "ct1",
    "ct2",
    "ct3",
    "ct4",
]):
    df.at[name, "MostImportant"] =  indx + 1