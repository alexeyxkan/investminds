import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data


def a_divide_b_and_c(a, b, c, name, label1, label2, filename):
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    (a / b).plot(x="Date", y="Close", ax=ax1, legend=False, color="g")
    c.plot(x="Date", y="Close", ax=ax2, legend=False, color="b")

    ax1.set_xlabel(name)
    ax1.set_ylabel(label1, color='g')
    ax2.set_ylabel(label2, color='b')

    fig.savefig(filename)
    plt.close()
    
    return fig


def correlation_xfl_spx_to_us10yt():
    a_divide_b_and_c(pd.DataFrame(data.get_xfl())["Close"],
                     pd.DataFrame(data.get_spx())["Close"],
                     data.get_us10yt()["Close"],
                     'Корреляция отношения Финансового сектора к S&P 500 и ставки по 10-летним tresuries',
                     'XFL/S&P_500', 'United States 10-Year Bond Yield',
                     'images/correlation_xfl_spx_to_us10yt.png')
    
    
def correlation_copper_gold_to_us10yt():
    a_divide_b_and_c(pd.DataFrame(data.get_copper())["Close"], 
                     pd.DataFrame(data.get_gold())["Close"],
                     data.get_us10yt()["Close"],
                     'Корреляция отношения меди к золоту и стаки по 10-летним tresuries',
                     'Медь/Золото',
                     'United States 10-Year Bond Yield',
                     'images/correlation_copper_gold_to_us10yt.png')