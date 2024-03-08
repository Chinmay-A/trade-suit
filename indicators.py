def sma(window, series):
    
    if(window>len(series)):
        raise Exception("Window is longer than the available data")

    return (sum(series[-window:])/window)

def ema(window, k, series):

    if(window>len(series)):
        raise Exception("Window is longer than the available data")
    
    if(window==len(series)):
        return sma(window,series)
    

    x=ema(window,k,series[-1])
    return k*(series[-1]-x)+x

def bollinger_bands(window,series,devs):

    if(window>len(series)):
        raise Exception("Window is longer than the available data")
    
    import statistics

    middle=sma(window,series)
    stdev=statistics.stdev(series[-window:])
    
    return middle-devs*stdev,middle,middle+devs*stdev

def rsi(ltps, window):

    ltps_rel=ltps[-window:]
    #print(ltps_rel)

    dels=[(ltps_rel[i]-ltps_rel[i-1]) for i in range(len(ltps_rel)-1)]

    pos=[i if i>=0 else 0 for i in dels]
    #print(pos)
    neg=[i if i<0 else 0 for i in dels]
    #print(neg)

    return 100-(100/(1+(sum(pos)*len(neg)/(len(pos)*abs(sum(neg))))))

    
    
