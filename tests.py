#%%
from scratchbook import *
from library_of_scratches import *
from pprint import pprint

codebook = {
    "stab":"d + ~g",
    "tazer1":"~bLog_f1Log_12",
}
# myscratch = makeScratch(
#   "stab + i + (f2Ex//1)**.2 + ~(f2Log//1)**.2 + tazer1" )
# info = getInfo(myscratch)
# fig = Session(myscratch, fontsize=11, w_pad=2).fig
# # fig.show()
# # pprint(info)
# assert info["#Sounds"] == 11
# assert info["Orbit"] == 4
# assert info["Ex-Phantazm"] == 1
# assert info["Tazer"] == 1

print(len(ELEMENTS), "ELEMENTS")
# pprint(ELEMENTS[45])

print(len(TEARS), "TEARS")
# pprint(TEARS[23])

print(len(ORBITS), "ORBITS")
pprint(ORBITS[34:])
# %%
