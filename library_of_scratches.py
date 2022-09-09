#%%
from scratchbook import *
import re
import json
from pprint import pprint



### Preview

class Preview:
    
    def __init__(self, scratch, bars=2, linewidth=2, markersize=4, previewmode=False):
        bars = 1 
        beats = (bars * 4) 
        beatsfactor = beats / 8
        linewidth = linewidth / beatsfactor
        markersize = markersize / beatsfactor
        markeredgecolor="black"
        markerfacecolor="white"
        height = 1# / beatsfactor
        width = 1.5
        self.fig = plt.gcf()
        self.ax = plt.gca()
        self.ax.cla()
        self.fig.set_figheight(height)
        self.fig.set_figwidth(width)
        xshift = 0
        resolution = 500
        vinyl_track =[]
        fader_track = []
        for scalars, f, color, clicks  in scratch.slices:
            xscale, yscale, yshift = scalars
            x = np.linspace(0.0, 1.0, round(resolution * xscale))
            vinyl = np.vstack((
                x * xscale + xshift, 
                f(x) * yscale + yshift,
            ))
            vinyl_track.append([vinyl, color, linewidth])
            clicks = clicks * xscale + xshift
            fader = np.vstack((
                clicks, 
                np.array([np.interp(i, *vinyl) for i in clicks]),
            )).T
            fader_track.append([fader, markersize])
            xshift += scalars[0]
        for vinyl, color, linewidth in vinyl_track:
            self.ax.plot(*vinyl, color=color, linewidth=linewidth, 
                solid_capstyle='round')
        for fader, markersize in fader_track:
            for click in fader:
                self.ax.plot(*click, marker="o", markersize=markersize, 
                    markeredgecolor=markeredgecolor, markeredgewidth=.5, 
                    markerfacecolor=markerfacecolor)
        plt.axis("off")
        self.fig.patch.set_facecolor('#cccccc')
        self.fig.tight_layout()

### makeLib

def makeLib(f, names):
    lib = {}
    for name in names:
        formula = f(name) if not f == element else name
        row = getInfo(makeScratch(formula))
        row["Name(s)"] = name
        row["Formula"] = formula
        lib[name] = row
    return lib


### ELEMENTS

fN, trN = 3, 4
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


### CODEBOOK

codebook = {

    "bo":"b_b",
    "babyorbit":"b_b",
    
    "s":"i_o",
    "slice":"i_o",
     
    "c":"o_i",
    "chirp":"o_i",

    "do":"d_d",
    "diceorbit":"d_d",

    "st":"d_g",
    "stab":"d_g",
    
    "f1o":"f1_f1",
    "flob1":"f1_f1",
    "flareorbit1":"f1_f1",

    "f2o":"f2_f2",
    "flob2":"f2_f2",
    "flareorbit2":"f2_f2",

    "f3o":"f3_f3",
    "flob3":"f3_f3",
    "flareorbit3":"f3_f3",

    "ogf":"of1_i_21",
    "ogflare":"of1_i_21",

    "cf1":"(c / (1/3) + flob1 / (2/3)) / 2",
    "chirpflare1":"cf1",
    
    "cf2":"c / (1/2) + flob2 / (3/2)",
    "chirpflare2":"cf2",

    "cf3":"(c/(2/5) + f3_f3/(8/5)) / 2",
    "chirpflare3":"cf3",

    "cogf":"(c/.5 + ogf/(3/4)) / 1",
    "chirpogflare":"cogf",
    
    "cogf_roll":"(cogf/1.25) * 4",
    "chirpogflare_roll":"cogf_roll",

    "rawogf":"of1_i",
    "rawogflare":"of1_i",

    "hp":"f1_f2_23",
    "hippo":"f1_f2_23",
    "hippopotamus":"f1_f2_23",    
    
    "hp_roll":"hp * 4",
    "hippo_roll":"hp_roll",
    "hippopotamus_roll":"hp_roll",
    
    "rawhp":"f1_f2",
    "rawhippo":"f1_f2",
    "rawhippopotamus":"f1_f2",

    "brbhp":"bo/.5 + f2/(3/4) + ~f1/.5 + h/.25",
    "brbhippopotamus":"brbhp",

    "ta1":"~iLog_of1Log_12",  
    "tazer1":"ta1",

    "ta2":"~iLog_of2Log_13",
    "tazer2":"ta2",

    "sc":"bo * 2 / 1",
    "scribble":"sc",

    "dr":"bo * 4 / 1 // 0.5",
    "drills":"dr",

    "uzi":"bo * 8 / 1 // 0.25",
    
    "mt":"st/.25 + (i + ~b + o + ~g)/.5//.5 + st/.25 + (i + ~b + o + ~g)/.5//.5 + st/.25 + gh/.25",
    "military":"mt",
    
    "k":"(c + c) /.5 + flob1 / .5",
    "kermit":"k",
    
    "sf":"(s + do) / 1",
    "swingflare":"sf",
    
    "pr":"(oft1 + ~(s//1) + ~ift1) / 1 // .75",
    "prizm":"pr",

    "pr_roll":"(pr / 1.5) * 2",
    "prizm_roll":"pr_roll",
    
    "boom":"(s + d/0.5//0.5 + ~s + ~d/0.5//0.5) / 2",
    "boomerang":"boom",

    "boom_roll":"(boom/(1.5)) * 2",
    "boomerang_roll":"boom_roll",

    "cboom":"c/.5 + (boom%4)/1.5",
    "chirpboom":"cboom",
    "chirpboomerang":"cboom",
    
    "ab":"s/(2/3)//(1/3) + i/(1/3)//(1/3) + (s/(2/3)//(1/3))**(1/3) + (trt1//(2/3)/(2/3))**(1/3) + ~trt1/(2/3)",
    "autobahn":"ab",

    "ss":"(s + g/0.5//0.5 + ~s + ~g/0.5//0.5) / 1",
    "seesaw":"ss",

    "stcr":"st/(1/3) + tr3/(1/2) + ~g/(1/6)",
    "stabcrab":"stcr",

    "stcr_roll":"stcr / (9/12) * 16",
    "stabcrab_roll":"stcr_roll",

    "slico1":"(h/(1/8))**(1/3) + ~s/(1/4)//(1/3) + (d/(1/8)//(1/3))**(1/3) + (s/(1/4)//(1/3))**(2/3) + (~ift1/(1/4)//(1/3))**(1/3)",
    "slicecombo1":"slico1",

    "slico2":"slico1[:-2] + ~(d/(1/8)//(1/3))**(1/3) + ~s/(1/4)//(1/3) + (d/(1/8)//(1/3))**(1/3) + (s/(1/4)//(1/3))**(2/3) + ~(d/(1/8)//(1/6))**(3/6)  + ~(s/(1/4)//(1/3))**(1/6) + (~i/(1/8)//(1/6))**(2/6)",
    "slicecombo2":"slico2",

    "rl":"(c/.5 + ogf/(3/4)) * 2 + c/.5 + ogf",
    "royalline":"rl",

    "eg":"flob1 + f1/.5 + ~f2/(3/4)",
    "enneagon":"eg",

    "eg_roll":"eg * 4",
    "enneagon_roll":"eg_roll",
    
    "hg":"c/.5 + ogf/(3/4) + c/.5 + of1_if1",
    "hendecagon":"hg",

    "hg_roll":"hg * 4",
    "hendecagon_roll":"hg_roll",
    
    "tt":"(~i_of2_13 + (gh/(1/4))**1) * 4",
    "turntrans":"tt",
    "turnaroundtransform":"tt",
    
    "internet":"~b/.25 + bo/.5 + f1/.5 + ~b/.25 + bo/.5 + b/.5 + ~b/.25 + bo/.5 + f2/(3/4)",
}


### COMBOS

COMBOS = {}
for k, v in codebook.items():
  if any(i in v for i in "+*~"):
    row = getInfo(makeScratch(v, codebook))
    row["Name(s)"] = k
    row["Formula"] = v
    COMBOS[k] = row


### UPDATE NAMES FOR ALL LIBS GIVEN CODEBOOK ENTRIES

for k, v in codebook.items():
    for lib in [ELEMENTS, TEARS, ORBITS, COMBOS]:
        if v in lib:
            lib[v]["Name(s)"] = f"{k}, " + lib[v]["Name(s)"]


### GENERIC TUTORIALS & SCRATCH SEARCHABILITY

def base(name):
    return re.sub(r"Log|Ex|[DASQ\d]", "", name)

def baseN(name):
    return re.sub(r"Log|Ex|[DASQ]", "", name)

def addTutorials(lib):
    for k, v in lib.items():
        baseNk = "_".join([baseN(name) for name in k.split("_")[:2]])
        basek = "_".join([base(name) for name in k.split("_")[:2]])
        if baseNk in ["b_b", "b"]:
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=rtqTmUVjsuY", "credit":"DJ Noumenon"} # Babies
        elif baseNk in ["f1_f1", "f1"]:
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=irNJitl6xpc", "credit":"DJ Rafik"} # 1-Click Flares
        elif baseNk in ["f2_f2", "f2"]: 
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=x-GqD3eH36g", "credit":"DJ Rafik"} # 2-Click Flares
        elif baseNk in ["f3_f3", "f3"]: 
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=x-GqD3eH36g", "credit":"DJ Rafik"} # 3-Click Flares
        elif basek in ["tr_tr", "tr"]:
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=XdkNAePjM7o", "credit":"DJ Immortal"} # Transformers
        elif baseNk == "of1_i_21":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=V1owPZNNMPI", "credit":"DJ Throdown"} # OG Flare
        elif basek == "d_g":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=Fl-JlMxQlxc", "credit":"DJ Dirty Digits"} # Stabs
        elif basek == "o_i": 
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=pKe3OUKaK2k", "credit":"DJ Dirty Digits"} # Chirps
        elif basek == "t" or basek == "t_t":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=WN8ity9B35U", "credit":"DJ Angelo"} # Faderless Tears

for lib in [ELEMENTS, TEARS, ORBITS, COMBOS]:
    addTutorials(lib)
    for k, v in lib.items():
        v["Search"] = ""
        for scratch in [ # copy/paste from scratchbook.INFOKEYS
            "Babies", # b
            "Ins", # i
            "Outs", # o
            "Dices", # d
            "Flares", # f
            "iFlares", # if
            "oFlares", # of
            "Transformers", # tr
            "Ghosts", # g
            "Holds", # h
            "G-Holds", # gh
            ### Individual Orbits
            "Chirps", # c
            "Slices", # s
            "Stabs", # st
            "Flare-Orbits", # f_f
            # "1C-Flobs", # _1cfo
            # "2C-Flobs", # _2cfo
            # "3C-Flobs", # _3cfo
            # "Hippos", # hp
            "OG-Flares", # ogf
            "Baby-Orbits", # bo
            "Dice-Orbits", # do
            "Off-Stabs", # ost
            ### Orbit types
            "S-Curved",
            "Tazers",
            "Phantazms",
            "Ex-Tazers",
            "Ex-Phantazms",
        ]:
            if v[scratch]:
                if scratch == "Babies":
                    scratch = "Babies Baby"
                v["Search"] += f" {scratch}"


### SPECIFIC TUTORIALS

COMBOS["sc"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rtqTmUVjsuY", 
      "credit":"DJ Noumenon"}
COMBOS["dr"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rtqTmUVjsuY", 
      "credit":"DJ Noumenon"}
COMBOS["uzi"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=YjtVcQ39QrU", 
      "credit":"DJ Phillee Blunt"}
COMBOS["ta1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=kuVk_wyNAg", 
      "credit":"DJ Rafik"}
COMBOS["ta2"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=JRaUuXhw6Qk", 
      "credit":"DJ ND"}
COMBOS["mt"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=GpT1Y1aMlWw", 
      "credit":"DJ Trife"}
COMBOS["k"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rQnMymtQ9sg", 
      "credit":"DJ Raedawn"}
COMBOS["sf"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=h3o5OTIy", 
      "credit":"DJ Shiftee"}
COMBOS["cf1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DUaY6gMONmA", 
      "credit":"DJ Excess"}
COMBOS["pr"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B32m9Jqqrpo", 
      "credit":"DJ Fast-M"}
COMBOS["pr_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B32m9Jqqrpo", 
      "credit":"DJ Fast-M"}
COMBOS["boom"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=c2IrbYGs0eU", 
      "credit":"DJ Dirty Digits"}
COMBOS["boom_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=c2IrbYGs0eU", 
      "credit":"DJ Dirty Digits"}
COMBOS["ab"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=nqzwiWkKV_s", 
      "credit":"DJ Dirty Digits"}
COMBOS["ss"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=6ZHYnUdPw3g", 
      "credit":"DJ DJ Raedawn"}
COMBOS["slico1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B_iOaAguNuo", 
      "credit":"DJ Short-E"}
COMBOS["slico2"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B_iOaAguNuo", 
      "credit":"DJ Short-E"}
COMBOS["rl"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=iMHKliaY7BU", 
      "credit":"DJ chile"}
COMBOS["eg"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=fPOTkGvLtL0", 
      "credit":"DJ chile"}
COMBOS["eg_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=fPOTkGvLtL0", 
      "credit":"DJ chile"}
COMBOS["hg"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=OVZxorYLHj8", 
      "credit":"DJ chile"}
COMBOS["hg_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=OVZxorYLHj8", 
      "credit":"DJ chile"}
COMBOS["cogf"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DPC6LJar6DY", 
      "credit":"DJ chile"}
COMBOS["cogf_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DPC6LJar6DY", 
      "credit":"DJ chile"}
COMBOS["tt"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=7I8ezdTaq88", 
      "credit":"DJ chile"}
COMBOS["hp_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=wmiTMz8XViE", 
      "credit":"DJ chile"}
COMBOS["cboom"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=5mB80n1sZmo", 
      "credit":"DJ chile"}
COMBOS["internet"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=_mxSbVy6y8Y", 
      "credit":"DJ chile"}
COMBOS["brbhp"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=REVf6rnZPBc", 
      "credit":"DJ chile"}


### CORE

CORE = {
    k:dict(v)
    for k, v in COMBOS.items()
}

CORE.update({
    k:dict(v)
    for k, v in ORBITS.items()
    if k in [
        "b_b", # baby-orbit
        "d_g", # stabs
        "d_d", # dice-orbit
        "i_o", # slice
        "o_i", # chirp
        "f1_f1", # flob1
        "f2_f2", # flob2
        "f3_f3", # 3 click flare
        "f1_f2_23", # hippo
        "f1_f2", # rawhippo
        "of1_i", # rawogf
        "of1_i_21", # ogflare
    ]
})


### EXPORT JSONS

libraries = [
    [CORE, "CORE"],
    [ELEMENTS, "ELEMENTS"],
    [TEARS, "TEARS"],
    [ORBITS, "ORBITS"],
    [COMBOS, "COMBOS"],
]
for lib, libname in libraries:
    for k, v in lib.items():
        myscratch = makeScratch(v["Formula"], codebook)
        fig = Preview(myscratch).fig
        fig.savefig(f"previews/{k}.png", format="png")
        v["Preview"] = f"""<img class='center' src='{k}.png'>"""
        v["Tutorial"] = f"""<a href='{v["Tutorial"]["url"]}' target='_blank'>{v["Tutorial"]["credit"]} &#128279;</a>""" if "Tutorial" in v else ""
        for l, ln in libraries:
            v[ln] = 1 if k in l else 0

    # lib = list(lib.values())
    d = {"data":list(lib.values())}
    print(f'Exporting "{libname}" lib with {len(lib)} rows')
    with open(f'test/{libname}.json', 'w') as f:
        json.dump(d, f)

with open(f'test/codebook.json', 'w') as f:
    json.dump(codebook, f)


### COLUMS HTML

print()
print("HTML Columns")
print("*" * 80)
INFOKEYS = ["Name(s)", "Tutorial"] + INFOKEYS + ["Formula", "Search"] + [i[1] for i in libraries]
for indx, col in enumerate(INFOKEYS):
    print("{data:" + f'"{col}", title: "{col}"' + "}," + f" // {indx}")


### TESTS #####################
print()
print("TESTS")
print("*" * 80)
pprint(ELEMENTS["b"])


# myscratch = makeScratch(
#   "stab + i + (f2Ex//1)**.2 + ~(f2Log//1)**.2 + tazer1 + tazer2 + flob2", 
#   codebook
# )
# info = getInfo(myscratch)
# fig = Session(myscratch, fontsize=11, w_pad=2).fig
# fig.show()

# %%
