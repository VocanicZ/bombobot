from discord import file
from mss.models import Monitor
import pyautogui as gui
import cv2 as cv
import time
import discord
import os
import numpy as np
from PIL import Image
from mss import mss
from src.crypto import get_crypto_price

token = "OTA1Mjc1OTA3NjI1ODUyOTM4.YYHt4w.aCjCfK34cAu9WhmTTlxTe-SumA0" 
client = discord.Client()
sct = mss()
monitor = sct.monitors[1]
width = monitor["width"]
height = monitor["height"]
mon = {'top': 0, 'left':width, 'width':width, 'height':height}

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
    sct_img = sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    cv.imwrite('C:/Users/ampna/Github/work/pro/bombobot/src/img/curscreen.png', img_bgr)
    await message.channel.send(file=discord.File('C:/Users/ampna/Github/work/pro/bombobot/src/img/curscreen.png'))
  elif message.content == "!curprice":
    await message.channel.send(get_crypto_price())

if __name__ == '__main__':
  client.run(token)