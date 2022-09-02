#%%
from scratchbook import *
import re
import json
from pprint import pprint

# def makeLib(f, names):
#     table = []
#     for name in names:
#         formula = f(name) if not f == element else name
#         row = getInfo(makeScratch(formula))
#         row["Name(s)"] = name
#         row["Formula"] = formula
#         table.append(row)
#     return table

# def exportJSON(lib, filename):
#     print(f'Exporting "{filename}" lib with {len(lib)} rows')
#     with open(f'{filename}.json', 'w') as f:
#         json.dump(lib, f)

def makeLib(f, names):
    lib = {}
    for name in names:
        formula = f(name) if not f == element else name
        row = getInfo(makeScratch(formula))
        row["Name(s)"] = name
        row["Formula"] = formula
        lib[name] = row
    return lib

def exportJSON(lib, filename):
    lib = list(lib.values())
    print(f'Exporting "{filename}" lib with {len(lib)} rows')
    with open(f'{filename}.json', 'w') as f:
        json.dump(lib, f)


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
elements = makeLib(element, names)


### TEARS

tN = 3
names = [f"{base}t{n}{crv}" for n in range(2, tN + 1) 
        for base in ["", "i", "o", "d", "if", "of", "tr"]
        for crv in ["", "Ex", "Log"] ]
tears = makeLib(tear, names)


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
orbits = makeLib(orbit, names)


### CODEBOOK

codebook = {

    "t":"t2",
    "tear":"t2",
    "it":"it2",
    "itear":"it2",
    "ot":"ot2",
    "otear":"ot2",
    "ft":"ft2",
    "ftear":"ft2",
    "ift":"ift2",
    "iftear":"ift2",
    "oft":"oft2",
    "oftear":"oft2",
    "trt":"trt2",
    "trtear":"trt2",

    "babyorbit":"b_b",
    "bo":"b_b",
    
    "slice":"i_o",
    "s":"i_o",
     
    "chirp":"o_i",
    "c":"o_i",

    "diceorbit":"d_d",
    "do":"d_d",

    "st":"d_g",
    "stab":"d_g",
    
    "ocf":"f1_f1",
    "f1o":"f1_f1",
    "flare1orbit":"f1_f1",
    "cf1":"(c / (1/3) + ocf / (2/3)) / 2",

    "cocf":"cf1",
    "chirpflare1":"cf1",
    
    "tcf":"f2_f2",
    "f2o":"f2_f2",
    "flare2orbit":"f2_f2",
    "cf2":"c / (1/2) + tcf / (3/2)",

    "ctcf":"cf2",
    "chirpflare2":"cf2",

    "f3o":"f3_f3",
    "flare3orbit":"f3_f3",
    
    "ogflare":"of1_i_21",
    "ogf":"of1_i_21",
    "cogf":"(c/.5 + ogf/(3/4)) / 1",

    "chirpogflare":"cogf",
    "cogf_roll":"(cogf/1.25) * 4",
    "chirpogflare_roll":"cogf_roll",

    "rawogf":"of1_i",
    "rawogflare":"of1_i",

    "hp":"f1_f2",
    "hippo":"f1_f2",
    "hippopotamus":"f1_f2",    
    
    "hp_roll":"hp * 4",
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
    "drill":"dr",

    "uzi":"bo * 8 / 1 // 0.5",
    
    "mt":"st/.25 + (i + ~b + o + ~g)/.5//.5 + st/.25 + (i + ~b + o + ~g)/.5//.5 + st/.25 + gh/.25",
    "military":"mt",
    
    "k":"(c + c) /.5 + ocf / .5",
    "kermit":"k",
    
    "sf":"(s + do) / 1",
    "swingflare":"sw",
    
    "pr":"(oft + ~(s//1) + ~ift) / 1",
    "prizm":"pr",
    "pr_roll":"(pr / 1.5) * 4",
    "prizm_roll":"pr_roll",
    
    "boom":"(s + d/0.5//0.5 + ~s + ~d/0.5//0.5) / 2",
    "boomerang":"boom",
    "boom_roll":"(boom/(1.5)) * 2",
    "boomerang_roll":"boom_roll",
    "cboom":"c/.5 + (boom%4)/1.5",
    "chirpboom":"cboom",
    "chirpboomerang":"cboom",
    
    "ab":"s/(2/3)//(1/3) + i/(1/3)//(1/3) + (s/(2/3)//(1/3))**(1/3) + (trt//(2/3)/(2/3))**(1/3) + ~trt/(2/3)",
    "autobahn":"ab",

    "ss":"(s + g/0.5//0.5 + ~s + ~g/0.5//0.5) / 1",
    "seesaw":"ss",

    "stcr":"st/(1/3) + tr3/(1/2) + ~g/(1/6)",
    "stabcrab":"stcr",
    "stcrm":"stcr / (9/12) * 16",
    "stabcrabmarch":"stcrm",

    "slico1":"(h/(1/8))**(1/3) + ~s/(1/4)//(1/3) + (d/(1/8)//(1/3))**(1/3) + (s/(1/4)//(1/3))**(2/3) + (~ift/(1/4)//(1/3))**(1/3)",
    "slicecombo1":"slico1",
    "slico2":"slico1[:-2] + ~(d/(1/8)//(1/3))**(1/3) + ~s/(1/4)//(1/3) + (d/(1/8)//(1/3))**(1/3) + (s/(1/4)//(1/3))**(2/3) + ~(d/(1/8)//(1/6))**(3/6)",
    "slicecombo2":"slico2",

    "rl":"(c/.5 + ogf/(3/4)) * 2 + c/.5 + ogf",
    "royalline":"rl",

    "eg":"ocf + f1/.5 + ~f2/(3/4)",
    "enneagon":"eg",
    "eg_roll":"eg * 4",
    "enneagon_roll":"eg_roll",
    
    "hg":"c/.5 + ogf/(3/4) + c/.5 + of1_if1",
    "hendecagon":"hg",
    "hg_roll":"hg * 4",
    "hendecagon_roll":"hg_roll",
    
    "tt":"(~i_of2_13 + (gh/(1/4))**1) * 4",
    "turnaroundtransform":"tt",
    "turntrans":"tt",
    
    "int":"~b/.25 + bo/.5 + f1/.5 + ~b/.25 + bo/.5 + b/.5 + ~b/.25 + bo/.5 + f2/(3/4)",
    "internet":"int",
}


### COMBOS

combos = {}
for k, v in codebook.items():
  if any(i in v for i in "+*~"):
    row = getInfo(makeScratch(v, codebook))
    row["Name(s)"] = k
    row["Formula"] = v
    combos[k] = row


### UPDATE NAMES FOR ALL LIBS GIVEN CODEBOOK ENTRIES

for k, v in codebook.items():
    for lib in [elements, tears, orbits, combos]:
        if v in lib:
            lib[v]["Name(s)"] = f"{k}, " + lib[v]["Name(s)"]


### GENERIC TUTORIALS

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
        elif baseNk == "odt2_i":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=V1owPZNNMPI", "credit":"DJ Throdown"} # OG Flare
        elif basek == "d_g":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=Fl-JlMxQlxc", "credit":"DJ Dirty Digits"} # Stabs
        elif basek == "o_i": 
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=pKe3OUKaK2k", "credit":"DJ Dirty Digits"} # Chirps
        elif basek == "t" or basek == "t_t":
            v["Tutorial"] = {"url":"https://www.youtube.com/watch?v=WN8ity9B35U", "credit":"DJ Angelo"} # Faderless Tears

for lib in [elements, tears, orbits]:
    addTutorials(lib)


### SPECIFIC TUTORIALS
combos["sc"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rtqTmUVjsuY", 
      "credit":"DJ Noumenon"}
combos["dr"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rtqTmUVjsuY", 
      "credit":"DJ Noumenon"}
combos["uzi"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=YjtVcQ39QrU", 
      "credit":"DJ Phillee Blunt"}
combos["ta1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=kuVk_wyNAg", 
      "credit":"DJ Rafik"}
combos["ta2"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=JRaUuXhw6Qk", 
      "credit":"DJ ND"}
combos["mt"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=GpT1Y1aMlWw", 
      "credit":"DJ Trife"}
combos["k"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=rQnMymtQ9sg", 
      "credit":"DJ Raedawn"}
combos["sf"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=h3o5OTIy", 
      "credit":"DJ Shiftee"}
combos["cf1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DUaY6gMONmA", 
      "credit":"DJ Excess"}
combos["pr"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B32m9Jqqrpo", 
      "credit":"DJ Fast-M"}
combos["pr_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B32m9Jqqrpo", 
      "credit":"DJ Fast-M"}
combos["boom"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=c2IrbYGs0eU", 
      "credit":"DJ Dirty Digits"}
combos["boom_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=c2IrbYGs0eU", 
      "credit":"DJ Dirty Digits"}
combos["ab"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=nqzwiWkKV_s", 
      "credit":"DJ Dirty Digits"}
combos["ss"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=6ZHYnUdPw3g", 
      "credit":"DJ DJ Raedawn"}
combos["slico1"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B_iOaAguNuo", 
      "credit":"DJ Short-E"}
combos["slico2"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=B_iOaAguNuo", 
      "credit":"DJ Short-E"}
combos["rl"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=iMHKliaY7BU", 
      "credit":"DJ chile"}
combos["eg"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=fPOTkGvLtL0", 
      "credit":"DJ chile"}
combos["eg_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=fPOTkGvLtL0", 
      "credit":"DJ chile"}
combos["hg"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=OVZxorYLHj8", 
      "credit":"DJ chile"}
combos["hg_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=OVZxorYLHj8", 
      "credit":"DJ chile"}
combos["cogf"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DPC6LJar6DY", 
      "credit":"DJ chile"}
combos["cogf_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=DPC6LJar6DY", 
      "credit":"DJ chile"}
combos["tt"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=7I8ezdTaq88", 
      "credit":"DJ chile"}
combos["hp_roll"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=wmiTMz8XViE", 
      "credit":"DJ chile"}
combos["cboom"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=5mB80n1sZmo", 
      "credit":"DJ chile"}
combos["int"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=_mxSbVy6y8Y", 
      "credit":"DJ chile"}
combos["brbhp"]["Tutorial"] = {
      "url":"https://www.youtube.com/watch?v=REVf6rnZPBc", 
      "credit":"DJ chile"}


### EXPORT JSONS

exportJSON(elements, "elements")
exportJSON(tears, "tears")
exportJSON(orbits, "orbits")
exportJSON(combos, "combos")




# myscratch = makeScratch(
#   "stab + i + (f2Ex//1)**.2 + ~(f2Log//1)**.2 + tazer1 + tazer2 + tcf", 
#   codebook
# )
# info = getInfo(myscratch)
# fig = Session(myscratch, fontsize=11, w_pad=2).fig
# fig.show()

# %%
