#%%
from scratchbook import *
# from library_of_scratches import *
from pprint import pprint

codebook = {
    "stab":"d + ~g",
    "tazer1":"~bLog_f1Log_12",
    "s":"i_o",
    "boom":"(s + d/0.5//0.5 + ~s + ~d/0.5//0.5) / 2",
}
formula = '~boom + tazer1 + f3_f6'
myscratch = makeScratch(
  formula,
  codebook
)
info = getInfo(myscratch)
# for k in ["Tears", "Orbits""]:
#   print(k, info[k])
pprint(info)
fig = Session(myscratch, fontsize=11, w_pad=2).fig
fig.show()
# %%
