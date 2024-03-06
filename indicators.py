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

    import statistics

    middle=sma(window,series)
    stdev=statistics.stdev(series[-window:])
    
    return middle-devs*stdev,middle,middle+stdev