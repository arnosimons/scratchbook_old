#%%
from scratchbook import *
# from library_of_scratches import *
from pprint import pprint


#########################################################

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
        self.fig.patch.set_facecolor((0, 0, 0, 0.125))
        self.fig.tight_layout()



########################################################

codebook = {
    "stab":"d + ~g",
    "tazer1":"~bLog_f1Log_12",
    "s":"i_o",
    "boom":"(s + d/0.5//0.5 + ~s + ~d/0.5//0.5) / 2",
}
formula = 'ft2__tr2 + ft2__df1'
myscratch = makeScratch(
  formula,
  codebook
)
info = getInfo(myscratch)
# for k in ["Tears", "Orbits""]:
#   print(k, info[k])
# pprint(info)
fig = Preview(myscratch).fig
fig.show()
# %%
