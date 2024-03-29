### IMPORTS #################################################################
import re
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker

class MyLocator(matplotlib.ticker.AutoMinorLocator):
    def __init__(self, n=12):
        super().__init__(n=n)
        
matplotlib.ticker.AutoMinorLocator = MyLocator
slicetype = slice # to avoid name collision with "slice" scratch


### CURVES ###################################################################

def _L(x): # for holds
    return np.zeros(len(x))

def _N(x): # S up
    return (-np.cos(np.pi * x) + 1) / 2

def _NR(x): # S down
    return (np.cos(np.pi * x) + 1) / 2

def _Ex(x): # 4th quadrant of circle
    return 1 - np.sqrt(1 - (x ** 2))

def _ExR(x): # 1st quadrant of circle
    return np.sqrt(1 - ((x - 0) ** 2))

def _Log(x): # 2nd quadrant of circle
    return np.sqrt(1 - ((x - 1) ** 2))

def _LogR(x): # 3rd quadrant of circle
    return 1 - np.sqrt(1 - ((x - 1) ** 2))

finv = { # for "~" operator
    _N:_NR,
    _NR:_N,
    _Ex:_ExR,
    _ExR:_Ex,
    _Log:_LogR,
    _LogR:_Log,
    _L:_L,
}

fneg = { # for "-" operator
    _N:_NR,
    _NR:_N,
    _Ex:_LogR,
    _ExR:_Log,
    _Log:_ExR,
    _LogR:_Ex,
    _L:_L,
}

ocrvs = { # for orbit info
    _NR:[_N, _Ex, _Log],
    _N:[_NR, _ExR, _LogR],
    _ExR:[_Ex, _N, _Log],
    _Ex:[_ExR, _NR, _LogR],
    _LogR:[_Log, _N, _Ex],
    _Log:[_LogR, _NR, _ExR],
}

fowardcrvs = [_N, _Ex, _Log]


### INFO #####################################################################

def makeFclicks(n, dasq):
    if not dasq:
        return [i / (n+1) for i in range(1, n+1)]
    if dasq == "D":
        return [i / (n+2) for i in range(1, n+1)]
    if dasq == "A":
        return [(i+1) / (n+2) for i in range(1, n+1)]
    if dasq == "S":
        if n % 2 == 0:
            left =  [i / (n+2) for i in range(1, int(n/2)+1)]
            right = [(i+1) / (n+2) for i in range(int(n/2)+1, int(n/2)*2+1)]
            return  left + right
        else:
            left =  [i / (n+2)  for i in range(1, int(n/2)+1)]
            middle = [1/2]
            right = [(i+2) / (n+2) for i in range(int(n/2)+1, int(n/2)*2+1)]
            return  left + middle + right
    if dasq == "Q":
        return  [(i+1) / (n+3) for i in range(1, n+1)]
INFOKEYS = [
    ### Sounds
    "Sounds",
    ### Number of Elements
    "Elements",
    ### Number of Tears
    "Tears", 
    ### Number of Orbits
    "Orbits",
    ### Clicks
    "FO",
    "FC",
    "PO",
    "PC",
    ### Click patterns
    "D",
    "A",
    "S",
    "Q",
    ### Curves
    "Ex",
    "Log",
    
    ### Individual Elements
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
        ]  
def getInfo(scratch):
    # initialize dic
    info = {k:0 for k in INFOKEYS}
    lastel = None
    lastcrv = None
    # lastfclicks = None
    lastscale = None
    lastyshift = None
    lastabsheight = None
    lasticlick = None
    lastoclick = None
    decplaces, margin = 5, 0.00002
    # fill dic with data
    for indx, s in enumerate(scratch.slices):
        scale = s[0]
        crv = s[1]
        crvcol = s[2]
        clicks = s[3]
        iclick = 1 if 0 in clicks else 0 
        oclick = 1 if 1 in clicks else 0
        fclicks_list = [i for i in clicks if not i in [0, 1]]
        fclicks = len(fclicks_list)
        height = round(scale[1], decplaces)
        yshift = round(scale[2], decplaces)
        absheight = height + yshift
        nohold = crv != _L
        reverse = True if nohold and lastcrv and (lastcrv in ocrvs[crv]) else False
        forward = True if crv in fowardcrvs else False
        isorbit = nohold and reverse and scale[1:] == lastscale[1:] and iclick==lastoclick and oclick==lasticlick
        istear = nohold and not reverse and lastabsheight and (
            (forward and lastabsheight - yshift < margin) 
            or (not forward and lastyshift - absheight < margin))
        info["Elements"] += 1
        if istear:
            info["Tears"] += 1
        if isorbit:
            info["Orbits"] += 1
            if (lastcrv == _N and crv == _NR) or (lastcrv == _NR and crv == _N):
                info["S-Curved"] += 1
            elif (lastcrv == _Log and crv == _LogR) or (lastcrv == _LogR and crv == _Log):
                info["Tazers"] += 1
            elif (lastcrv == _ExR and crv == _Log) or (lastcrv == _Log and crv == _ExR):
                info["Phantazms"] += 1
            elif (lastcrv == _Ex and crv == _ExR) or (lastcrv == _ExR and crv == _Ex):
                info["Ex-Tazers"] += 1
            elif (lastcrv == _Ex and crv == _LogR) or (lastcrv == _LogR and crv == _Ex):
                info["Ex-Phantazms"] += 1
        info["FO"] += iclick + fclicks
        info["FC"] += oclick + fclicks
        info["PO"] += int(bool(not iclick))
        info["PC"] += int(bool(not oclick))
        for style in "DASQ":
            if (fclicks_list not in [[], [0], [1/2], [1]] 
            and fclicks_list == makeFclicks(fclicks, style) 
            and not info[style]):
                info[style] = 1
        if crv in [_Ex, _ExR] and not info["Ex"]:
            info["Ex"] = 1
        elif crv in [_Log, _LogR] and not info["Log"]:
            info["Log"] = 1
        # Holds, Ghosts and Babies first. Only the latter makes Sounds
        if not any([fclicks, iclick, oclick]): 
            if crv == _L:
                if crvcol == "k":
                    info["Holds"] += 1
                    lastel = "Holds"
                elif crvcol == "w":
                    info["G-Holds"] += 1
                    lastel = "G-Holds"
            elif crvcol == "w":
                info["Ghosts"] += 1
                if lastel == "Dices" and isorbit:
                    info["Stabs"] += 1
                lastel = "Ghosts"
            elif crvcol == "k":
                info["Sounds"] += 1
                info["Babies"] += 1
                if lastel == "Babies" and isorbit:
                    info["Baby-Orbits"] += 1
                lastel = "Babies"  
        # All other scratches now. They all make Sounds
        else:
            info["Sounds"] += (1 + fclicks)
            if iclick and not any([oclick, fclicks]): # In
                info["Ins"] += 1
                if lastel == "Outs" and isorbit:
                    info["Chirps"] += 1
                elif lastel == "oFlares":  # OGF
                    info["OG-Flares"] += 1
                lastel = "Ins"
            elif oclick and not any([iclick, fclicks]): # Out
                info["Outs"] += 1
                if lastel == "Ins" and  isorbit:
                    info["Slices"] += 1
                lastel = "Outs"
            elif all([iclick, oclick]) and not fclicks: # Dice
                info["Dices"] += 1
                if lastel == "Ghosts" and isorbit:
                    info["Off-Stabs"] += 1
                elif lastel == "Dices" and isorbit:
                    info["Dice-Orbits"] += 1
                lastel = "Dices"
            elif fclicks and not any([iclick, oclick]): # Flare
                info["Flares"] += 1
                if lastel == "Flares" and isorbit:
                    info["Flare-Orbits"] += 1
                    # if lastfclicks == fclicks == 1:  # 1C-Flobs
                    #     info["1C-Flobs"] += 1
                    # elif lastfclicks == fclicks == 2: # 2C-Flobs
                    #     info["2C-Flobs"] += 1
                    # elif lastfclicks == fclicks == 3: # 3C-Flobs
                    #     info["3C-Flobs"] += 1
                    # elif lastfclicks == 1 and fclicks == 2: # Hippo
                    #     info["Hippos"] += 1
                lastel = "Flares"
            elif all([fclicks, iclick]) and not oclick: # iFlare
                info["iFlares"] += 1
                lastel = "iFlares"
            elif all([fclicks, oclick]) and not iclick: # # oFlare
                info["oFlares"] += 1
                lastel = "oFlares"
            elif all([fclicks, iclick, oclick]): # Transformer
                info["Transformers"] += 1
                lastel = "Transformers"
        lastcrv = crv
        # lastfclicks = fclicks
        lastscale = scale
        lastyshift = yshift
        lastabsheight = absheight
        lasticlick = iclick
        lastoclick = oclick
    return info


### SCRATCH ##################################################################

class Scratch:
    
    def __init__(self, slices):
        self.slices = slices
        # self.info = getInfo(self)        
        self.length = sum(i[0][0] for i in slices)
        self.height = max(i[0][1] + i[0][2] for i in self.slices)
            
    def __truediv__(self, n): # length
        return Scratch([
            [[
                i[0][0] / self.length * n, # xscale
                i[0][1], # yscale
                i[0][2], # yshift
            ]] + i[1:] 
            for i in self.slices
        ])
    
    def __floordiv__(self, n): # yscale
        return Scratch([
            [[
                i[0][0], # xscale
                i[0][1] / self.height * n, # yscale
                i[0][2] / self.height * n, # yshift
            ]] + i[1:] 
            for i in self.slices
        ])
    
    def __pow__(self, n): # yshift
        return Scratch([
            [[
                i[0][0], # xscale
                i[0][1], # yscale
                i[0][2] + n, # yshift
            ]] + i[1:] 
            for i in self.slices
        ])
    
    def __getitem__(self, so):
        if isinstance(so, slicetype):
            slices = self.slices[so]
        elif isinstance(so, int):
            slices = [self.slices[so]]
        else:
            message = f'Indexing must be of the form "[n]" or "[n:m]", where n and m are integers. See the Operator section for help.'
            raise TypeError(message)
        return Scratch(slices)
    
    def __add__(self, other):
        if not isinstance(other, Scratch):
            message = "A scratch can only be added to another scratch"
            raise TypeError(message)
        return Scratch(self.slices + other.slices)
    
    def __mul__(self, n):
        if not isinstance(n, int) or (isinstance(n, int) and n < 1):
            message = "A scratch can only be multiplied by an integer > 0"
            raise ValueError(message)
        scratch = self
        for i in range(n-1):
            scratch += self
        return scratch
    
    def __mod__(self, n): # phase shift the scratch
        if not isinstance(n, int) or (
            isinstance(n, int) and n > len(self.slices)):
            message = "Phase shifting requires an integer smaller or equal to the number of slices. Here:" + str(len(self.slices))
            raise ValueError(message)
        return self[n:] + self[:n]
    
    def __invert__(self): # invert on y-axis
        maxy = max(i[0][1] + i[0][2] for i in self.slices)
        yshift = min(i[0][2] for i in self.slices)
        return Scratch([
            [[i[0][0], i[0][1], yshift + (maxy - (i[0][1] + i[0][2]))], 
            finv[i[1]], i[2], i[3]] for i in self.slices])
    
    def __neg__(self): # invert on x-axis
        return Scratch([
            [i[0], fneg[i[1]], i[2], np.flip([1 - i for i in i[3]])] 
            for i in self.slices][::-1])
    
### SESSION ##################################################################

class Session:
    
    def __init__(self, scratch, bars=2, linewidth=4, markersize=8, 
                 fontsize=12, pad=0, h_pad=0, w_pad=0, rect=None):
        if scratch.length / 4 <= round(scratch.length / 4):
            required_len = round(scratch.length / 4)
        else:
            required_len = round(scratch.length / 4) + 1        
        bars = required_len if required_len >= 2 else 2
        beats = (bars * 4) 
        beatsfactor = beats / 8
        linewidth = linewidth / beatsfactor
        markersize = markersize / beatsfactor
        fontsize = fontsize / beatsfactor
        markeredgecolor="black"
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
        xticks_labels = [
            f"{i+1}" if not i % 4 == 0 
            else f"({i+1})" for i in range(len(xticks))][:-1] + [1]
        self.ax.set_xlim(
            [-(height * marginscalar), beats + (height * marginscalar)])
        self.ax.set_ylim(
            [-(height * marginscalar), 1 + (height * marginscalar)])
        self.ax.set_xlabel('Counts (in quarter notes)', fontsize=fontsize)
        self.ax.set_xticks(xticks, xticks_labels, fontsize=fontsize)
        self.ax.grid(which='major', color='#2e2d2d', linewidth=0.8)
        self.ax.grid(which='minor', color='#787878', linestyle=':', 
                     linewidth=0.5)
        self.ax.xaxis.set_major_locator(plt.MaxNLocator(10 * beatsfactor))
        self.ax.minorticks_on() 
        self.ax.set_ylabel('Sample', fontsize=fontsize)
        self.ax.set_yticks([0.0, 1.0], ['Start (0)','End (1)'], 
                           fontsize=fontsize)
        for i in range(beats):
            if i % 4 == 0:
                self.ax.axvline(x=i, color='black', 
                                label='axvline - % of full height')
            if not i % 2 == 0:
                self.ax.axvspan(i, 1 + i, facecolor='#e6e6e6', alpha=0.5, 
                                ymin=1 - marginscalar * 1.5, 
                                ymax=marginscalar * 1.5)
            else:
                self.ax.axvspan(i, 1 + i, facecolor='#cccccc', alpha=0.5, 
                                ymin=1 - marginscalar * 1.5, 
                                ymax=marginscalar * 1.5)    
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
        self.fig.tight_layout(pad=pad, h_pad=h_pad, w_pad=w_pad, rect=rect)
        
### ELEMENTS #################################################################

def fcl(n, dasq):
    if not dasq:
        return [f'{i}/{n+1}' for i in range(1, n+1)]
    if dasq == "D":
        return [f'{i}/{n+2}' for i in range(1, n+1)]
    if dasq == "A":
        return [f'{i+1}/{n+2}' for i in range(1, n+1)]
    if dasq == "S":
        if n % 2 == 0:
            left =  [f'{i}/{n+2}' for i in range(1, int(n/2)+1)]
            right = [f'{i+1}/{n+2}' for i in range(int(n/2)+1, int(n/2)*2+1)]
            return  left + right
        else:
            left =  [f'{i}/{n+2}' for i in range(1, int(n/2)+1)]
            middle = ["1/2"]
            right = [f'{i+2}/{n+2}' for i in range(int(n/2)+1, int(n/2)*2+1)]
            return  left + middle + right
    if dasq == "Q":
        return  [f'{i+1}/{n+3}' for i in range(1, n+1)]
    
def element(name):
    _h = "(?P<h>h(?:old)?)"
    _gh = "(?P<gh>g(?:host)?h(?:old)?)"
    _g = "(?P<g>g(?:host)?)"
    _b = "(?P<b>b(?:aby)?)"
    _i = "(?P<i>i(?:n)?)"
    _o = "(?P<o>o(?:ut)?)"
    _d = "(?P<d>d(?:ice)?)"
    _f = "(?P<f>f(?:lare)?\d)"
    _if = "(?P<if>if(?:lare)?\d)"
    _of = "(?P<of>of(?:lare)?\d)"
    _df = "(?P<df>df(?:lare)?\d)" # allow as well...?
    _tr = "(?P<tr>tr(?:ansformer)?\d)"
    _D = "(?P<D>D)"
    _A = "(?P<A>A)"
    _S = "(?P<S>S)"
    _Q = "(?P<Q>Q)"
    _Ex = "(?P<Ex>Ex)"
    _Log = "(?P<Log>Log)"
    ELS = re.compile(fr"(?:{_h}|{_gh})$|(?:{_g}|{_b}|{_i}|{_o}|{_d}|(?:{_f}|{_if}|{_of}|{_df}|{_tr})(?:{_D}|{_A}|{_S}|{_Q})?)(?:{_Ex}|{_Log})?$")
    m = ELS.match(name)
    # if not m or name.startswith("df"):
    if not m:
        raise ValueError(f'unintelligible name: "{name}"')
    dic = m.groupdict()
    dic = {k:True if v else False for k,v in dic.items()}
    l, h, ys = 1, 1, 0 # default
    crv, crvc = "N", "k" # default
    cl = [] # default
    if dic["h"]:
        crv = "L"
    elif dic["gh"]:
        crv = "L"
        crvc = "w"
    elif dic["g"]:
        crvc = "w"
    else:
        if dic["Log"]:
            crv = "Log"
        elif dic["Ex"]:
            crv = "Ex"
        if dic["i"] or dic["d"] or dic["if"] or dic["tr"] or dic["df"]:
            cl.append("0")
        m = re.match(r"(?:[iod]?f(?:lare)?(?P<fN>\d)|tr(?:ansformer)?(?P<trN>\d))(?P<DASQ>[DASQ])?", name)
        if m:
            md = m.groupdict()
            n = int(md["fN"]) if md["fN"] else int(md["trN"]) - 1
            cl += fcl(int(n), md['DASQ'])
        if dic["o"] or dic["d"] or dic["of"] or dic["tr"] or dic["df"]:
            cl.append("1")
        cl = f'[{", ".join(cl)}]'
    scratch = f"Scratch([[[1,1,0], _{crv}, '{crvc}', np.array({cl})]])"
    return scratch
        
### TEARS ####################################################################

def tearParts(steps, el):
    if int(steps) <= 1:
        raise ValueError("Steps must be an int > 1")
    return [
        f"({el}/(1/{steps})//(1/{steps})){f'**({i}/{steps})' if not i==0 else ''}" 
        for i in range(steps)]

def tear(name):
    _t = "(?P<t>((?P<ft>f)|(?P<trt>tr))?t(?:ear)?(?P<tN>\d))"
    _i = "(?P<i>i)"
    _o = "(?P<o>o)"
    _d = "(?P<d>d)"
    _iod = f"(?:{_i}|{_o}|{_d})"
    _crv = "(?P<crv>Ex|Log)"
    TRS = re.compile(fr"{_iod}?{_t}{_crv}?(?:__(?P<el>(?:d?f(?:lare)?\d|tr(?:ansformer)?\d)[DASQ]?))?$")
    m = TRS.match(name)
    if not m or name.startswith("otr") or name.startswith("itr"):
        raise ValueError(f'unintelligible name: "{name}"')
    dic = m.groupdict()
    if dic["el"]:
        dic["el"] = f'{dic["el"]}{dic["crv"] or ""}'
    else:
        if dic["trt"]:
            dic["el"] = f'd{dic["crv"] or ""}' 
        else:
            dic["el"] = f'b{dic["crv"] or ""}'    
    # parts = tearParts(int(dic['tN']), dic['el']) # <--- tN means N slices (like sounds in transformers)
    parts = tearParts(int(dic['tN']) + 1, dic['el']) # <--- tN means N + 1 slices (like sounds in flares)
    # handle clicks between tear parts
    if dic["ft"] or dic["trt"]:
        if dic["el"].startswith("b"):
            parts[0] = parts[0].replace("b", "o")
            parts[-1] = parts[-1].replace("b", "i")
        elif dic["el"].startswith("f"):
            parts[0] = parts[0].replace("f", "of")
            parts[-1] = parts[-1].replace("f", "if")
        for i in range(1, len(parts)-1):
            if dic["el"].startswith("b"):
                parts[i] = parts[i].replace("b", "d")
            elif dic["el"].startswith("f"):
                parts[i] = parts[i].replace(
                    f'f{dic["el"][1]}', f'tr{int(dic["el"][1]) + 1}')          
    # handle iod clicks
    elements = [re.sub(r"[-+*/%~\[\]\(\).:]|\b\d*\b", " ", i).strip() 
        for i in parts]
    if (dic["i"] or dic["d"] or dic["trt"]) and not any(
        dic["el"].startswith(i) for i in ["i","d","tr"]):
        if elements[0].startswith("b"):
            parts[0] = parts[0].replace("b", "i")
        elif elements[0].startswith("of"):
            parts[0] = parts[0].replace(
                f'of{dic["el"][1]}', f'tr{int(dic["el"][1]) + 1}')
        elif elements[0].startswith("o"):
            parts[0] = parts[0].replace("o", "d").replace("Ldg", "Log")            
        elif elements[0].startswith("f"):
            parts[0] = parts[0].replace("f", "if")
    if (dic["o"] or dic["d"] or dic["trt"]) and not any(
        dic["el"].startswith(i) for i in ["o","d","tr"]):
        if elements[-1].startswith("b"):
            parts[-1] = parts[-1].replace("b", "o")
        elif elements[-1].startswith("if"):
            parts[-1] = parts[-1].replace(
                f'if{dic["el"][1]}', f'tr{int(dic["el"][1]) + 1}')
        elif elements[-1].startswith("i"):
            parts[-1] = parts[-1].replace("i", "d")            
        elif elements[-1].startswith("f"):
            parts[-1] = parts[-1].replace("f", "of")
    # wrap up
    elements = [re.sub(r"[-+*/%~\[\]\(\).:]|\b\d*\b", " ", i).strip() 
        for i in parts]
    element_dics = [element(el)[1] for el in elements]
    formula = " + ".join(parts)
    return formula
        
### ORBITS ###################################################################

# _s = "gbiodftrxDASQEL"
_s = "(?:h(?:old)?|g(?:host)?h(?:old)?|g(?:host)?|b(?:aby)?|i(?:n)?|o(?:ut)?|d(?:ice)?|(?:[iod]?f(?:lare)?\d|tr(?:ansformer)?\d)[DASQ]?|(?:[iod]f?|tr)t(?:ear)?\d(?:Ex|Log)?(?:__(?:(?:d?f(?:lare)?\d|tr(?:ansformer)?\d)[DASQ]?))?)"
_c = "(?:Ex|Log)"
_tEl = "(?:__(?:[bd]|(?:f\d|tr\d)[DASQ]?))"

ORB = re.compile(
    # fr"(?P<L>[{_s}][{_s}\d]*?{_tEl}?)_(?P<R>[{_s}][{_s}\d]*{_tEl}?)(?:_(?P<S>\d\d))?$")
    # fr"(?P<L>[\w\d]*?{_tEl}?)_(?P<R>[\w\d]*?{_tEl}?)(?:_(?P<S>\d\d))?$")
    fr"(?P<L>{_s}{_c}?{_tEl}?)_(?P<R>{_s}{_c}?{_tEl}?)(?:_(?P<S>\d\d))?$")

def orbit(name):
    m = ORB.match(name)
    if not m:
        raise ValueError(f'unintelligible name: "{name}"')
    dic = m.groupdict()
    if dic['S']:
        num1, num2 = dic['S'][0], dic['S'][1]
        den = int(num1) + int(num2)
        formula = f"({dic['L']}/({num1}/{den}) + ~{dic['R']}/({num2}/{den})) / 1{' // 0.5' if not any(i.startswith(j) for i in [dic['L'], dic['R']] for j in ['f', 'if', 'of', 'tr']) else ''}"
    else:
        formula = f"({dic['L']} + ~{dic['R']}) / 1{' // 0.5' if not any(i.startswith(j) for i in [dic['L'], dic['R']] for j in ['f', 'if', 'of', 'tr']) else ''}"
    return formula

### MAKE SCRATCH #############################################################

codebook = {} # Dummy to avoid error messages in html...

def new(formula, codebook=codebook):
    formula = re.sub(r"[-+*/%~\[\]\(\).:]|\b\d*\b", " ", formula)
    for name in set(formula.split()):
        try:
            exec(name)
        except NameError:
            try:
                exec(element(name))
                yield name
            except:
                yield name
                try:
                    for name in new(tear(name), codebook):
                        yield name
                except:
                    try:
                        for name in new(orbit(name), codebook):
                            yield name
                    except:
                        for name in new(codebook[name], codebook):
                            yield name

SLICE = re.compile(r"\bslice\b")            
IN = re.compile(r"\bin\b")
IN_ = re.compile(r"\bin_(?=\w)")
_IN = re.compile(r"(?<=\w)_in\b")        

def makeScratch(formula, codebook=codebook):
    formula = SLICE.sub("s", formula)
    formula = IN.sub("i", formula)
    formula = IN_.sub("i_", formula)
    formula = _IN.sub("_i", formula)
    just_defined = set()
    for n in list(new(formula, codebook))[::-1]:
        if n in just_defined:
            continue
        try:
            exec(f"{n} = {element(n)}")
            just_defined.add(n)
        except:
            try:
                exec(f"{n} = {tear(n)}")
                just_defined.add(n)
            except:
                try:
                    exec(f"{n} = {orbit(n)}")
                    just_defined.add(n)
                except:
                    exec(f"{n} = {codebook[n]}")
                    just_defined.add(n)
    return eval(formula)