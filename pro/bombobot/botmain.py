import discord
from discord.ext import commands
from src.crypto import get_crypto_price
from src.imgbot import *
from src.fl import *
from datetime import datetime

token = "bruh"
client = commands.Bot(command_prefix='.')#discord.Client()

@client.event
async def on_ready():
  print("{0.user} connected".format(client))

@client.event
async def on_message(message):
  def curscreen():
    set_img('curscreen', get_curscreen())
  if message.author == client.user or message.channel.id != 905278361524391976:
    return
  curscreen()
  await message.delete()
  count = 0
  command = 'menu : goto main menu \nbalance : current balance on screen \nheros : display all heros \nmap : open map menu \nworkall : force every heros to work \nrestall : force every heros to rest \nback : return to main menu \nclose : close pop-up \njoin our sheet -> https://docs.google.com/spreadsheets/d/1UqdWBjrXFToku7G1YfuEgTZM2PN3be-ilmuoYgUnYQA/edit?usp=sharing'
  if message.content == "menu":
    while not get_loc('heros_button') and count < 10:
      if get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      elif get_loc('back_button'):
        click_img('back_button',delay=1,x=800,y=100)
      else:
        sleep(1)
      count+=1
  elif message.content == "balance":
    while not get_loc('refbalance2') and count < 10:
      if get_loc('refbalance'):
        click_img('refbalance',delay=2)
      elif get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      else:
        sleep(1)
      count+=1
  elif message.content == "back":
    click_img('back_button',delay=1,x=800,y=100)
  elif message.content == "close":
    click_img('close_button',delay=1,x=200,y=100)
  elif message.content == "heros":
    while not get_loc('refheros') and count < 10:
      if get_loc('heros_button'):
        click_img('heros_button',delay=1,y=500)
      elif get_loc('back_button'):
        click_img('back_button',delay=1,x=800,y=100)
      elif get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      else:
        sleep(1)
      count+=1
  elif message.content == "map":
    while not get_loc('back_button') and count < 10:
      if get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      elif get_loc('refmap'):
        click_img('refmap',delay=1,x=100)
      else:
        sleep(1)
      count+=1
  elif message.content == "workall":
    while not get_loc('refheros') and count < 10:
      if get_loc('heros_button'):
        click_img('heros_button',delay=1,y=500)
      elif get_loc('back_button'):
        click_img('back_button',delay=1,x=800,y=100)
      elif get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      else:
        sleep(1)
      count+=1
    if get_loc('refheros'):
      loc = (4000,1320)
      for _ in range(5):
        click(loc)
        sleep(2)
  elif message.content == 'restall':
    while not get_loc('refheros') and count < 10:
      if get_loc('heros_button'):
        click_img('heros_button',delay=1,y=500)
      elif get_loc('back_button'):
        click_img('back_button',delay=1,x=800,y=100)
      elif get_loc('close_button'):
        click_img('close_button',delay=1,x=200,y=100)
      else:
        sleep(1)
      count+=1
    if get_loc('refheros'):
      loc = (4125, 500)
      for _ in range(5):
        click(loc)
        sleep(2)
  curscreen()
  await message.channel.purge(limit=3)
  now = datetime.now()
  await message.channel.send('```current bcoin price on bsc : '+get_crypto_price()+'\nlast update : '+now.strftime("%d/%m/%Y %H:%M:%S")+'```')
  await message.channel.send(file=discord.File(get_img_path('curscreen')))
  await message.channel.send("```"+command+"```")

if __name__ == '__main__':
  client.run(token)
