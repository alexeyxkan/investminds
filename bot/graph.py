import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data


def correlation_xfl_spx_to_us10yt():
    plt.style.use('seaborn-whitegrid')
    data1 = pd.DataFrame(data.get_xfl())["Close"] / pd.DataFrame(data.get_spx())["Close"]
    data2 = data.get_us10yt()["Close"]
    
    plt.style.use('seaborn-whitegrid')
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    data1.plot(x="Date", y="Close", ax=ax1, legend=False, color="g")
    data2.plot(x="Date", y="Close", ax=ax2, legend=False, color="b")

    ax1.set_xlabel('Корреляция отношения Финансового сектора к S&P 500 и ставки по 10-летним tresuries')
    ax1.set_ylabel('XFL/S&P_500', color='g')
    ax2.set_ylabel('United States 10-Year Bond Yield', color='b')

    fig.savefig('images/correlation_xfl_spx_to_us10yt.png')
    plt.close()
