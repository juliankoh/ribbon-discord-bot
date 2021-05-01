import discord
from discord.ext import tasks
import os
from web3 import Web3
from dotenv import load_dotenv
from prometheus_api_client import PrometheusConnect

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
INFURA_KEY = os.getenv('INFURA_KEY')
VAULT_REFRESH_TIMER = os.getenv('VAULT_REFRESH_TIMER')

ADDRESS = "0x0FABaF48Bbf864a3947bdd0Ba9d764791a60467A"

w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{INFURA_KEY}"))

ABI = """[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_weth","type":"address"},{"internalType":"address","name":"_usdc","type":"address"},{"internalType":"address","name":"_swapContract","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldCap","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newCap","type":"uint256"},{"indexed":false,"internalType":"address","name":"manager","type":"address"}],"name":"CapSet","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"options","type":"address"},{"indexed":false,"internalType":"uint256","name":"withdrawAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"manager","type":"address"}],"name":"CloseShort","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"share","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"oldManager","type":"address"},{"indexed":false,"internalType":"address","name":"newManager","type":"address"}],"name":"ManagerChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"options","type":"address"},{"indexed":false,"internalType":"uint256","name":"depositAmount","type":"uint256"},{"indexed":false,"internalType":"address","name":"manager","type":"address"}],"name":"OpenShort","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"share","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"Withdraw","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"oldFee","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"newFee","type":"uint256"}],"name":"WithdrawalFeeSet","type":"event"},{"inputs":[],"name":"MINIMUM_SUPPLY","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"SWAP_CONTRACT","outputs":[{"internalType":"contract ISwap","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"USDC","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"accountVaultBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"adapter","outputs":[{"internalType":"contract IProtocolAdapter","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"asset","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"assetAmount","type":"uint256"}],"name":"assetAmountToShares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"assetBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"cap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentOption","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"currentOptionExpiry","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"delay","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"deposit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"depositETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"emergencyWithdrawFromShort","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"contract IRibbonFactory","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"feeRecipient","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_asset","type":"address"},{"internalType":"address","name":"_owner","type":"address"},{"internalType":"address","name":"_feeRecipient","type":"address"},{"internalType":"uint256","name":"_initCap","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"instantWithdrawalFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockedAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lockedRatio","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"maxWithdrawAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxWithdrawableShares","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextOption","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"nextOptionReadyAt","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"rollToNextOption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"components":[{"internalType":"bytes4","name":"kind","type":"bytes4"},{"internalType":"address","name":"wallet","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"id","type":"uint256"}],"internalType":"struct Types.Party","name":"signer","type":"tuple"},{"components":[{"internalType":"bytes4","name":"kind","type":"bytes4"},{"internalType":"address","name":"wallet","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"id","type":"uint256"}],"internalType":"struct Types.Party","name":"sender","type":"tuple"},{"components":[{"internalType":"bytes4","name":"kind","type":"bytes4"},{"internalType":"address","name":"wallet","type":"address"},{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"id","type":"uint256"}],"internalType":"struct Types.Party","name":"affiliate","type":"tuple"},{"components":[{"internalType":"address","name":"signatory","type":"address"},{"internalType":"address","name":"validator","type":"address"},{"internalType":"bytes1","name":"version","type":"bytes1"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"internalType":"struct Types.Signature","name":"signature","type":"tuple"}],"internalType":"struct Types.Order","name":"order","type":"tuple"}],"name":"sellOptions","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newCap","type":"uint256"}],"name":"setCap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newFeeRecipient","type":"address"}],"name":"setFeeRecipient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newManager","type":"address"}],"name":"setManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"underlying","type":"address"},{"internalType":"address","name":"strikeAsset","type":"address"},{"internalType":"address","name":"collateralAsset","type":"address"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint256","name":"strikePrice","type":"uint256"},{"internalType":"enum ProtocolAdapterTypes.OptionType","name":"optionType","type":"uint8"},{"internalType":"address","name":"paymentToken","type":"address"}],"internalType":"struct ProtocolAdapterTypes.OptionTerms","name":"optionTerms","type":"tuple"}],"name":"setNextOption","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"newWithdrawalFee","type":"uint256"}],"name":"setWithdrawalFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"share","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"share","type":"uint256"}],"name":"withdrawAmountWithShares","outputs":[{"internalType":"uint256","name":"amountAfterFee","type":"uint256"},{"internalType":"uint256","name":"feeAmount","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"share","type":"uint256"}],"name":"withdrawETH","outputs":[],"stateMutability":"nonpayable","type":"function"}]"""

client = discord.Client()

def get_vault_capacity():
    contract = w3.eth.contract(address=ADDRESS, abi=ABI)
    
    cap = contract.functions.cap().call()
    balance = contract.functions.totalBalance().call()
    
    capacity = (cap - balance) / 10**18
    # print(f"{capacity:.2f} eth")
    return f"{capacity:.2f} ETH Capacity"

def get_strike_percent():
    # connecting to prometheus
    prom = PrometheusConnect(url ="http://18.217.47.37:9090/", disable_ssl=True)

    # getting strike price
    strike_price = prom.custom_query(query="query_vaultShortPositions_strikePrice{job='rETH-THETA'} / 100000000")
    strike_price = float(strike_price[0]["value"][1])

    # getting eth price
    eth_price = prom.custom_query(query="crypto_currency{pair='ethusd', exchange='kraken'}")
    eth_price = float(eth_price[0]["value"][1])

    percent = ((strike_price / eth_price) - 1) * 100
    return f"{percent:.2f}% away from the Strike Price"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    refresh_capacity.start()

@tasks.loop(seconds=float(VAULT_REFRESH_TIMER))
async def refresh_capacity():
    capacity = get_vault_capacity()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=capacity))

@tasks.loop(seconds=float(VAULT_REFRESH_TIMER))
async def refresh_strike():
    strike_percent = get_strike_percent()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=strike_percent))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ethvault'):
        capacity = get_vault_capacity()
        await message.channel.send(capacity)

    if message.content.startswith('$ethstrike'):
        strike_percent = get_strike_percent()
        await message.channel.send(strike_percent)

    if message.content.startswith('$ngmi'):
        e = discord.Embed()
        e.set_image(url="https://cdn.discordapp.com/attachments/821798177501085727/831671217622089778/Screenshot_2021-04-14_at_00.24.20.png")
        msg = "<@!358623012657954816> is NGMI <:peepoRibbon:810321415722762241>"
        await message.channel.send(msg, embed=e)

    if message.content.startswith('$wen'):
        e = discord.Embed()
        e.set_image(url="https://media.discordapp.net/attachments/821798177501085727/832618375981039676/ribbonrug-picsay.jpg")
        msg = "No tokens, only rugs kek <:peepoRibbon:810321415722762241>"
        await message.channel.send(msg, embed=e)

    if message.content.startswith('$hat'):
        e = discord.Embed()
        e.set_image(url="https://i.pinimg.com/originals/7c/e9/3c/7ce93c4bbabb1d024366f549c62b2b0f.gif")
        msg = "idk man <:ribbonHat:829706651216248872>"
        await message.channel.send(msg, embed=e)

    if message.content.startswith('$help'):
        msg = "Ribbon bot commands:\n\n$vault - Tetha Vault available space\n$ngmi - someone is ngmi\n$wen - wen token?\n$hat - wen hat?"
        await message.channel.send(msg)

client.run(TOKEN)
