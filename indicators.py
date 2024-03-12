def sma(series,window):
    
    if(window>len(series)):
        raise Exception("Window is longer than the available data")

    return (sum(series[-window:])/window)

def ema(window, k, series):

    if(window>len(series)):
        raise Exception("Window is longer than the available data")
    
    if(window==len(series)):
        return sma(series,window)
    

    x=ema(window,k,series[:-1])
    return k*(series[-1]-x)+x

def bollinger_bands(window,series,devs):

    if(window>len(series)):
        raise Exception("Window is longer than the available data")
    
    import statistics

    middle=sma(series,window)
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

def calculate_rsi(close_prices, window):
    delta = [close_prices[i] - close_prices[i - 1] for i in range(1, len(close_prices))]
    gains = [delta[i] if delta[i] > 0 else 0 for i in range(len(delta))]
    losses = [abs(delta[i]) if delta[i] < 0 else 0 for i in range(len(delta))]
    
    avg_gain = sum(gains[:window]) / window
    avg_loss = sum(losses[:window]) / window
    
    if avg_loss == 0:
        return 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

def vwap(close,vols,window):

    numerator=0
    sum_vol=0
    n=len(close)

    for i in range(window):
        numerator+=close[n-i-1]*vols[n-i-1]
        sum_vol+=vols[n-i-1]
    
    return numerator/sum_vol

    
    
