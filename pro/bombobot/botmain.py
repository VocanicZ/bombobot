import discord
from src.crypto import get_crypto_price
from src.imgbot import get_curscreen
from src.fl import *

token = "OTA1Mjc1OTA3NjI1ODUyOTM4.YYHt4w.aCjCfK34cAu9WhmTTlxTe-SumA0" 
client = discord.Client()

@client.event
async def on_ready():
  print("{0.user} connected".format(client))

@client.event
async def on_message(message):
  if message.author == client.user or message.channel.id != 905278361524391976:
    return
  elif message.content == "!command":
    command = '!command : list all command \n!curscreen : display bot current screen \n!curprice : current price on bsc'
    await message.channel.send("```"+command+"```")
  elif message.content == "!curscreen":
    set_img('curscreen', get_curscreen())
    await message.channel.send(file=discord.File(get_img_path('curscreen')))
  elif message.content == "!curprice":
    await message.channel.send(get_crypto_price())

if __name__ == '__main__':
  client.run(token)