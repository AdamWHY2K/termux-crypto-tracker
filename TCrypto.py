#!/usr/bin/python3

from requests import get
from plotext import plot, title, figsize, xlabel, ylabel, nocolor, show, clear_plot
import json

def setValues():
    global combinedFiat, combinedFiatNet
    """
    Choose which coins to display here
    Use getInfo(name, identifier, coins, fiat, currency)
    name must be a string, should be the common abbrevation for the coin, such as BTC for bitcoin, ETH for ethereum, etc.
    identifer must be a string, must be compliant with coingecko's api - see full list here https://api.coingecko.com/api/v3/coins/list
    coins must be a number (float or int), should be the number of coins you hodl.
    fiat must be a number (float or int), should be how much you spent to gain the coins you have - can be zero.
    currency must be a string, must be compliant with coingecko's api - see full list here https://api.coingecko.com/api/v3/simple/supported_vs_currencies
    """
    #Note, I do not own these amounts of crypto. This information is for demonstrative purposes only.
    getInfo("BTC", "bitcoin", 0.123, 123.45, "gbp")
    getInfo("ETH", "ethereum", 1, 1111, "gbp")
    getInfo("BAT", "basic-attention-token", 123.456789, 0, "gbp")
    getInfo("XMR", "monero", 0.321, 30.21, "gbp")

    #Add any stable coins or unspent fiat you own here, convert to currency you've been using in this script.
    #I'm returning GBP values here, but I own USDC, so I convert my USDC holdings to GBP then add that to combinedFiat
    combinedFiat += 420.69
    #GBP value of my USDC
    combinedFiat += 42
    #Unspent fiat sat on an exchange

    print("Total Coin: " + format(combinedFiat, ".2f"))
    print("Total Net: " + format(combinedFiatNet, ".2f"))

    #Exit
    input("\nPress enter to exit.")



def createGraph(name, identifier, currency):
    url = get("https://api.coingecko.com/api/v3/coins/" + identifier + "/market_chart?vs_currency=" + currency + "&days=1").json()
    count = 0
    x = []
    y = []

    for i in url["prices"]:
        y.append(url["prices"][count][1])
        count += 1
        x.append(count)
        #Iterates through the results of the json api page.

    plot(x, y)
    title(name + " - 24 HOURS")
    #Joins user added name to title
    figsize(90,15)
    #Size of the graph, variable based on resolution
    xlabel("Number of entries")
    ylabel("Price")
    nocolor()
    show()
    clear_plot()
    #Must clear plot if calling multiple graphs at once.

def getInfo(name, identifier, coins, fiat, currency):
    global combinedFiat, combinedFiatNet
    createGraph(name, identifier, currency)
    coinData = get("https://api.coingecko.com/api/v3/simple/price?ids=" + identifier + "&vs_currencies=" + currency).json()
    print("\n" + name + ": " + str(coinData[identifier][currency]))
    coinLast = float(coinData[identifier][currency])
    myCoinFiat = coins * coinLast
    coinNet = myCoinFiat - fiat
    compareCoinUrl = get("https://api.coingecko.com/api/v3/coins/" + identifier + "/market_chart?vs_currency=" + currency + "&days=1").json()
    compareCoin = compareCoinUrl["prices"][0][1]
    percentageCoin = (coinLast - compareCoin) / compareCoin * 100
    totalCoinFiat = format(myCoinFiat, '.2f')
    totalCoinNet = format(coinNet, '.2f')
    totalCoinPercentage = format(percentageCoin, '.2f')+"%"
    print("My " + name + ": " + totalCoinFiat)
    if fiat != 0:
        print("Loss/Gain: " + totalCoinNet)
    print("24hr % Change: " + totalCoinPercentage)
    print(" ")
    combinedFiat += myCoinFiat
    combinedFiatNet += coinNet

combinedFiat = 0
combinedFiatNet = 0

print("""
_________________________________________________________________
     _       _              __        ___   ___   ______  _  __
    / \   __| | __ _ _ __ __\ \      / | | | \ \ / |___ \| |/ /
   / _ \ / _` |/ _` | '_ ` _ \ \ /\ / /| |_| |\ V /  __) | ' / 
  / ___ | (_| | (_| | | | | | \ V  V / |  _  | | |  / __/| . \ 
 /_/   \_\__,_|\__,_|_| |_| |_|\_/\_/  |_| |_| |_| |_____|_|\_\\

	                A Termux Crypto Tracker.
                      Github: github.com/AdamWHY2K
_________________________________________________________________""")

try:
    setValues()
except KeyError:
    print("Ensure the identifier you entered is compliant with coingecko's api - https://api.coingecko.com/api/v3/coins/list")
    print("Ensure the currency you entered is compliant with coingecko's api - https://api.coingecko.com/api/v3/simple/supported_vs_currencies")
