# termux-crypto-tracker
Author: AdamWHY2K

                                      Not expected, extremely appreciated:
* BTC: bc1qfgj4tk2a7hzyxmmrgx4mvumef5f6yfey737xsj    BCH: qzrqu0yecxka0p7sxr2g3fvpfcpg9x0awq3tf2m5ny   
                      <img src="https://user-images.githubusercontent.com/68286215/130465610-63a93f21-4c79-4de4-a1ee-2aeb6ed17a9a.png">                                                                    <img src="https://user-images.githubusercontent.com/68286215/130466304-f6b50ae3-2bf4-40df-bf6d-3adf95f2ec67.png">
* XMR: 47tW7pPZTW9LWxsB3KkWSgQgK9B5RH8yr9hPZ7jRofu8jTtPPxhpRVYjJvkK2EsYDsfpbMGBBQp5wNRrk4h6pPhG2rH1q8s
                                                  <img src="https://user-images.githubusercontent.com/68286215/130466563-1ad94060-fd62-4c87-ad3b-728858f8dcea.png">

## Description
* A simple python script to keep track of your crypto.
* Supports any crypto that coingecko's api supports (which is a lot) -- https://api.coingecko.com/api/v3/coins/list
* Shows losses/gains, 24 hour graph and percentage change.

Please note that I haven't tested this on any device other than my own. If you have issues feel free to open an [issue](https://github.com/AdamWHY2K/termux-crypto-tracker/issues/new) and I'll see what I can do.

https://user-images.githubusercontent.com/68286215/140621241-20d5ca13-e7e0-4f31-ad21-a2da15f1607f.mp4

# Requirements
* [Termux](https://github.com/termux/termux-app)
* [Termux-Widget](https://github.com/termux/termux-widget)
* [plotext v2.3.1](https://pypi.org/project/plotext/)

# Instructions
* Open termux and clone this repository using `git clone https://github.com/AdamWHY2K/termux-crypto-tracker`
* `cd termux-crypto-tracker`
* `pip3 install -r requirements.txt`
* `mv TCrypto.* ~/.shortcuts/`
* `nano ~/.shortcuts/TCrypto.py` and **read** the multiline comment, edit the values so they're accurate for you
* Go to your homescreen and add a Termux:Widget shortcut that launches **TCrypto.*sh***
