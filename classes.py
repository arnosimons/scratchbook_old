import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker
class MyLocator(matplotlib.ticker.AutoMinorLocator):
    def __init__(self, n=12):
        super().__init__(n=n)
matplotlib.ticker.AutoMinorLocator = MyLocator
slicetype = slice

class Scratch:
    
    def __init__(self, slices, length=None, yscale=1, yshift=0):
        length = length or sum(i[0][0] for i in slices)
        self.slices = [[np.array([
            i[0][0] / sum(i[0][0] for i in slices) * length, # xscale
            i[0][1] * yscale, # yscale
            i[0][2] * yscale + yshift, # yshift
        ])] + i[1:] for i in slices]
    
    def __getitem__(self, so):
        if isinstance(so, slicetype):
            slices = self.slices[so]
        elif isinstance(so, int):
            slices = [self.slices[so]]
        else:
            raise TypeError("Indexing requires slice or int, not", type(so))
        return Scratch(slices, length=sum(i[0][0] for i in slices))
    
    def __add__(self, other):
        if not isinstance(other, Scratch):
            message = "A scratch can only be added to another scratch"
            pyscript.write("session-output", message)
            raise ValueError(message)
        return Scratch(self.slices + other.slices)
    
    def __mul__(self, n):
        if not isinstance(n, int) or (isinstance(n, int) and n < 1):
            message = "A scratch can only be multiplied by an integer > 0"
            pyscript.write("session-output", message)
            raise ValueError(message)
        scratch = self
        for i in range(n-1):
            scratch += self
        return scratch
    
    def __truediv__(self, length):
        return Scratch(self.slices, length=length)
    
    def __floordiv__(self, yscale):
        return Scratch(self.slices, yscale=yscale)
    
    def __invert__(self):
        maxheight = max(i[0][1] + i[0][2] for i in self.slices)
        yshift = min(i[0][2] for i in self.slices)
        return Scratch([[[i[0][0], i[0][1], yshift + (maxheight - (i[0][1] + i[0][2]))], finv[i[1]], i[2], i[3]] for i in self.slices])
    
    def __neg__(self):
        return Scratch([[i[0], fneg[i[1]], i[2], np.flip([1 - i for i in i[3]])] for i in self.slices][::-1])
    
    def __mod__(self, n):
        if not isinstance(n, int) or (isinstance(n, int) and n > len(self.slices)):
            message = "Phase shifting requires an integer smaller or equal to the number of slices. Here:" + str(len(self.slices))
            pyscript.write("session-output", message)
            raise ValueError(message)
        return self[n:] + self[:n]
    
    def yshift(self, n):
        return Scratch([[[i[0][0], i[0][1], i[0][2] + n], i[1], i[2], i[3]] for i in self.slices])
    
class Session:
    
    def __init__(self, scratch, bars=2, linewidth=5, markersize=10, fontsize=12):
        beats = (bars * 4) if bars else x
        beatsfactor = beats / 8
        linewidth = linewidth
        markersize = markersize
        markeredgecolor="black", 
        markerfacecolor="white"
        height = 2 / beatsfactor
        width = 15
        marginscalar = 0.05
        self.fig = plt.gcf()
        self.ax = plt.gca()
        self.ax.cla()
        self.fig.set_figheight(height)
        self.fig.set_figwidth(width)
        xticks = np.linspace(0, beats, beats + 1)
        xticks_labels = [i+1 for i in range(len(xticks))][:-1] + [1]
        self.ax.set_xlim([-(height * marginscalar), beats + (height * marginscalar)])
        self.ax.set_ylim([-(height * marginscalar), 1 + (height * marginscalar)])
        self.ax.set_xlabel('Count', fontsize=fontsize)
        self.ax.set_xticks(xticks, xticks_labels, fontsize=fontsize)
        self.ax.grid(which='major', color='#2e2d2d', linewidth=0.8)
        self.ax.grid(which='minor', color='#787878', linestyle=':', linewidth=0.5)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(10 * beatsfactor))
        self.ax.minorticks_on() 
        self.ax.set_ylabel('Sample', fontsize=fontsize)
        self.ax.set_yticks([0.0, 1.0], ['Start (0)','End (1)'], fontsize=fontsize)
        for i in range(beats):
            if not i % 2 == 0:
                self.ax.axvspan(i, 1 + i, facecolor='#e6e6e6', alpha=0.5, ymin=1 - marginscalar * 1.5, ymax=marginscalar * 1.5)
            else:
                self.ax.axvspan(i, 1 + i, facecolor='#cccccc', alpha=0.5, ymin=1 - marginscalar * 1.5, ymax=marginscalar * 1.5)    
        xshift = 0
        resolution = 500
        for scalars, f, color, clicks  in scratch.slices:
            xscale, yscale, yshift = scalars
            x = np.linspace(0.0, 1.0, round(resolution * xscale))
            vinyl = np.vstack((
                x * xscale + xshift, 
                f(x) * yscale + yshift,
            ))
            clicks = clicks * xscale + xshift
            fader = np.vstack((
                clicks, 
                np.array([np.interp(i, *vinyl) for i in clicks]),
            )).T
            self.ax.plot(*vinyl, color=color, linewidth=linewidth, solid_capstyle='round')
            for click in fader:
                self.ax.plot(*click, marker="o", markersize=markersize, markeredgecolor="black", markerfacecolor="white")
            xshift += scalars[0]