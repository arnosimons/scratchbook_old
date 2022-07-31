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