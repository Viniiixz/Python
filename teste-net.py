import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

#tese
def internet():
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    s = speedtest.Speedtest()
    dataatual = datatime.now().strftime('%d/%m/%Y')
    horatual = datatime.now().strftime('%H:%M')
    velocidade = s.download(threads=None)*(10**-6)
    df.loc[len(df)] = [dataatual, horatual, velocidade]
    df.to_excel('dados.xlsx', sheet_name='base', index=False)
    Timer(1000, internet).start()


internet()
