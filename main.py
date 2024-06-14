import asyncio
import os
import random
import sys
import logging
import tracemalloc
import requests
import json
import time
import discord
from discord import message
from discord import Client, Intents, Embed
from discord.ext import commands


#from keep_alive import keep_alive

#welcome to lore bot rewritten.
#the commands are added at the bottom, and some commands have changed names. for example, commands with a dash (-) in the name have been replaced with an underscore. why? because command names dont like dashes. 
#still a wip, not all commands are added, and some might not work. but the most used commands should still be working. most commands on the list were only used one time and never again, and some i cant even find by searching on discord. if you have any issues or commands that need to be added, like a missing lore card for example, ping me.
#updated command list will be coming soon.. maybe. i know its annoying but so is a lot of the format of the command names not being able to be used in an IDE. the way the old kajbot worked is commands would be stored in a .txt file, so basically any name could be given, AND MOST IMPORTANTLY, commands could be added without touching any code at all, just had to be stored on a text file. i am not doing that. if a command needs to be added so deperately, i will add it here, but chances are a command needing to be added is just an image being sent into chat, or favouriting a gif. not worthy of adding a command only for it to be used once. resources are limited here, remember.
#i sort of rambled. i hope you have a nice nostalgia trip



tracemalloc.start()  # this is stupid 

port = 465  # For SSL
cow = 0
poop = 0
intents = discord.Intents.all()
client = commands.Bot(command_prefix = "+", intents=intents)
pig = 0 #where are any of these used

sepoch = time.time()
current_time = time.ctime(sepoch)

# @client.event
# async def on_message(message):
#    if random.randint(1,5) == 1:
#        await message.add_reaction('👀')

@client.event
async def on_ready():
    global ok
    print(f'{client.user} has connected to Discord!')
    test = client.get_channel(801109953536196639)
    okthen = 0
    a = ""
    for i in range(26):
        ok = '0'  # to change status, change this variable
    await client.change_presence(activity=discord.Game(name='ok'))

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")

#@client.event 
#async def on_message(message):
#  if message.content.startswith("https://hullseals.space/"):
#    await ctx.send(f"**__The greatest website known to man is currently above this message__**")

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

x = 86400 #24 hours in seconds
f = 1
stopb = 0

@client.command()
async def gaga(ctx):  # kinda just th
    a = ""
    for i in range(8):
        b = chr(random.randint(33, 126))
        a = a + b
    await ctx.send(a)

@client.command(brief="send lots of messages")
async def mensajes(ctx, msg, num): #send lots of message
    u = int(num)
    for i in range(u):
      await ctx.send(msg)

@client.command()
async def roll(ctx, min: int, max: int):
    await ctx.send(random.randint(min, max))

@client.command()
async def dm(self, msg, member = None):
    if member is not None:
        channel = member.dm_channel
        if channel is None:
            channel = await member.create_dm()
        await channel.send(msg)


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


@client.command(name='restart')  # restarts the bot. for like adding commands
async def restart(ctx):
    await ctx.send("restarting...")
    restart_bot()


@client.command()  # ping command
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command()
async def bruh(ctx):
    await ctx.send(f"bruh")


@client.command(pass_context=True)
async def myid(ctx):
    await ctx.send("{} is your id".format(ctx.message.author.id))

# @client.command()
# async def tts(ctx):
#    await ctx.send(f"(&*^&*(%*&_@$()_#($)_(@#*_()$(_)(-09-09230-94-08_(&*()@$*#&*(&#$^*(@&#^$&*@#$^&*!@#$^&*^@#", tts=True)



@client.command()
async def alive(ctx):  # it just sends some russian or somethin, used for testing
    await ctx.send(f"я жив")


@client.command(brief='check if im alright')
async def respond(ctx):
    await ctx.send(f"im here")


@client.command(brief='sends you')
async def baba(ctx):  # says who sent the command
    await ctx.send(f"Author: {ctx.author}")



@client.command(brief='says what you tell it to')
async def say(ctx, message):
    await ctx.send(message)


@client.command(brief='coin flip')
async def flip(ctx):
    cow = random.randint(1, 2)
    if cow == 1:
        await ctx.send(f"heads")
    else:
        await ctx.send(f"tails")


@client.command()
async def char(ctx):
    await ctx.send(chr(33))


@commands.has_permissions(administrator=True)
@client.command()
async def kick(ctx, member: discord.Member, *, why=None):
    await member.kick(reason=why)
    await ctx.send(f"{member} has been kicked by {ctx.author}")


@client.command()
async def image(ctx):
    c = "https://prnt.sc/"
    a = ""
    for i in range(2):
        b = chr(random.randint(97, 122))
        a = a + b
    for i in range(4):
        b = chr(random.randint(48, 57))
        a = a + b
    a = c + a
    await ctx.send(a)

@client.command()
async def chatisdead(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/834818089685483600/1117749097219239986/s7ZjTi1h.png?width=1078&height=794")

@client.command()
async def gravity(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/kF1GYE1Rw5_SRzoQM76ar4Gn_nG4f5qteSapbtl-w04/https/giant.gfycat.com/TightInbornIguana.mp4")

@client.command()
async def raxxla(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/596770377607282713/619323962572275722/sketch-1553703971235.png?width=1018&height=794")

@client.command()
async def newraxxla(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/499967027583123456/690283118732509224/sketch-1582379838094.png?width=1018&height=794")

@client.command()
async def quiet(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/IrIbYXBGCdbk0qi_-RTGtIT9K-_vXprrGSedW26XH4c/https/media.tenor.com/images/d7aac29bee701b6e6f94c52c2e607c35/tenor.gif?width=440&height=210")

@client.command()
async def training_pass(ctx):
  await ctx.send(f"Congratulations pup seal, you are now a verified seal. ")
  await ctx.send(f"`Once you have received the why so sealious role you will have access to more channels in the HSBC.`")
  await ctx.send(f"You will be able to seal")
  await ctx.send(f"`After 2 weeks you may start an optional advanced course.`")
  await ctx.send(f"You can sign up for training in other seal specialisations. ")
  await ctx.send(f"`You should create a Hull Seals account on our website so you can file paperwork and gain access to the IRC once we make the move.`")
  await ctx.send(f"You can also give yourself the active mechanic ```platform``` role in the Fleetcomm HQ discord server to receive pings when there is a case.")
  await ctx.send(f"`If you ever have a question feel free to ask any of the teachers, mods or admins.`")
  await ctx.send(f"That should be everything unless Unknown had forgotten to add something.")

@client.command()
async def castfist(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/thO_EBd1iOmhs92TiV5B0jTmyTXZhI54Nytts50L8mo/https/media.tenor.com/images/eff14acd47a18d4a3694bb949f43c6ce/tenor.gif?width=440&height=248")

@client.command()
async def website(ctx): 
  await ctx.send(f"https://hullseals.space/")
#in the commands sheet, there was 'weebsite' but there was also no record of that being used ever, so i assumed a typo?
#but i couldnt find 'website' being used either so i just assumed what it was and here we are

@client.command()
async def journal(ctx):
  await ctx.send(f"http://hullseals.space/journal")

@client.command()
async def hssop(ctx):
  await ctx.send(f"https://hullseals.space/knowledge/books/standard-operating-procedures")
@client.command()
async def natetyping(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/FapyigaKercKO-5aBxn2ZrxXggevhM3T8nT8qnfOuFk/https/media.tenor.com/images/31ca72c212e5045d3132dcf0cd87a6d2/tenor.gif?width=144&height=180")
@client.command()
async def nightmarefuel99(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/570667118023016459/666763501875888148/sketch-15790391270742.png?width=1334&height=794")
@client.command()
async def timetogo(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/nrvfNa_1fpp3HB8vavsjUcTTCRQ5pv65eqqVUrBZqjo/https/media.tenor.com/images/b4e9a3807b5aeea856c082e3741b0017/tenor.gif?width=440&height=246")
@client.command()
async def pure_evil(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/vHOHfDKBwXXtQYNpRQZTjuXaS1NtFOoNATqqiUP35aY/https/media.tenor.com/images/6494e2c611545bd3f3154224181c2e4a/tenor.gif?width=178&height=180")
@client.command()
async def marnin(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/Q41i8EYg9dCcwdpqMfrSW8xVBeyGINQUWCPSiFknSm8/%3Fitemid%3D15364121/https/media1.tenor.com/images/ba2c9d3f042f1417e00c280d10a64e16/tenor.gif?width=446&height=794")
@client.command()
async def toolewd(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/aCFlJe5cT7dafZ3F2cMpMR6J25UswvWnRaT5EpCSnJU/https/media.tenor.com/images/7927bd0e329a06db4766530784a51712/tenor.gif?width=440&height=246")
@client.command()
async def lewd(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/1MipS1qOwmKIqLVxsHkR-zVHk_hMDUWsa-Lz1fmjxYY/https/media.tenor.com/images/aea010c50a3aab16d3a5f47f027c6890/tenor.gif?width=440&height=246")
@client.command()
async def french(ctx):
  await ctx.send(f"***deleting** french* `1%`")
@client.command()
async def hshalpy(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/4adx28XT9LJy7f1CZCmMhap11qp6wXp-8X38Zaj9cUY/https/i.imgur.com/XlOhULd.mp4")

@client.command()
async def ualmostdidit(ctx):
  await ctx.send(f"wow you actually almost did it... I mean of course you almost did it you are almost the best... congrats 🎉🎉🎉")
@client.command()
async def stolen(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/558852116173684763/608763231749799950/stolen_meme.gif?width=440&height=440")
@client.command()
async def reeeeeeeeeeeeeeeeeee(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/7UTyc80Jy7-YP1DH5areiiVI7EgMld4tsG2t_1kuti8/https/media.tenor.com/images/eb51e8ca5c62d66e5c40249727f8ba3b/tenor.gif?width=440&height=338")
@client.command()
async def wd(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/558852116173684763/671848679673561098/hidefromthekillers.png?width=562&height=794")
@client.command()
async def strike(ctx):
  await ctx.send("that command is for autajja, not me, change ur prefix to `-`")
@client.command()
async def endworld(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/3KZHjD1jGtW2pNGDmfsY664YT0MFzFfd53Cpdndj2nM/https/media.tenor.com/images/5b637a38a860899944d3698673c18e63/tenor.gif?width=440&height=248")
@client.command()
async def canyshazard(ctx):
  await ctx.send(f"https://cdn.discordapp.com/emojis/646318939365703700.png?size=240")
@client.command()
async def masslore2(ctx):
  await ctx.send(f"https://cdn.discordapp.com/attachments/617832061524246548/617854557308846090/sketch-1567376992553.png https://cdn.discordapp.com/attachments/617832061524246548/617854557308846091/sketch-1567377685831.png https://cdn.discordapp.com/attachments/617832061524246548/617854557816619011/sketch-1567374960884.png https://cdn.discordapp.com/attachments/617832061524246548/617854558722457753/sketch-1567378284618.png https://cdn.discordapp.com/attachments/617832061524246548/617854559552798780/sketch-1567377938391.png https://cdn.discordapp.com/attachments/617832061524246548/617854561637498997/sketch-1567374857919.png https://cdn.discordapp.com/attachments/617832061524246548/617854562396536832/sketch-1567376861790.png https://cdn.discordapp.com/attachments/617832061524246548/617854562396536833/sketch-1567376948771.png https://cdn.discordapp.com/attachments/617832061524246548/617854575558524964/sketch-1567374515549.png https://cdn.discordapp.com/attachments/617832061524246548/617854576078487552/sketch-1567374627298.png https://cdn.discordapp.com/attachments/617832061524246548/617854559997657109/sketch-1567377366308.png https://cdn.discordapp.com/attachments/617832061524246548/617854558625988684/sketch-1567374749211.png")
@client.command()
async def clientinfo(ctx):
  await ctx.send("autajja did this one originally, but halpybot is probably more what youre looking for")
@client.command()
async def drink(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/499967027583123456/600477200524771329/sketch-1563235274327.png?width=794&height=794")
@client.command()
async def wtf(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/G1n_UabOMyoyvDwlpfkeOfOzGwzp9W-a37VzWWBTje8/https/media.tenor.com/images/ce4ae98b16871e8e78d692c43625d0ab/tenor.gif?width=440&height=330")
@client.command()
async def drebin(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854575558524964/sketch-1567374515549.png?width=596&height=794")
@client.command()
async def nate(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854576078487552/sketch-1567374627298.png?width=596&height=794")
@client.command()
async def maldor(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854561637498997/sketch-1567374857919.png?width=596&height=794")

@client.command()
async def akastus(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854559552798780/sketch-1567377938391.png?width=596&height=794")
@client.command()
async def inhooman(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854557308846091/sketch-1567377685831.png?width=596&height=794")
@client.command()
async def unknown(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/617832061524246548/617854558722457753/sketch-1567378284618.png?width=596&height=794")

@client.command()
async def boopthelostchapter(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/DVH6RHl2q1huU2ifa3rn0zrgR7YdzBZUWvCDH5bFcqU/https/media.tenor.com/images/933cf9f06926bfe7aa9fb2e68d255169/tenor.gif?width=440&height=246")
@client.command()
async def returnstare(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/558852116173684763/618605512413675571/20190903_132839.jpg?width=596&height=794")
@client.command()
async def incominghug(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/SHY-Kx6hlMokyzrDUcDyg0vuKGmVb8BO7mdpfvqULpc/https/media.tenor.com/images/9c24b14f074fcfe2d1fcfcd1b664d5fa/tenor.gif?width=214&height=180")
@client.command()
async def hshp(ctx):
  await ctx.send("The HS HP is the small carrier vessel sailed by Halfpenny to avoid him making eye contact with any others on the other ships. https://www.thevintagenews.com/wp-content/uploads/2016/04/The-first-picture-of-Draken-sailing-on-her-way-to-Iceland-N-60-050-E-003-101-Source-640x427.jpg")
@client.command()
async def nightmarefuel099(ctx):
  await ctx.send(f'https://media.discordapp.net/attachments/570667118023016459/666748029054877732/sketch-1579035500361.png?width=472&height=794')
@client.command()
async def lorebot(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/613149851211005953/613170872802344960/sketch-1566261516850.png?width=794&height=794")
@client.command()
async def hsha(ctx):
  await ctx.send(f"HS HA you really thought you could mess with us The HS Wonder's Defense Ship. https://cdn.discordapp.com/attachments/558862066341904384/575876645005557770/20190509_032637.jpg")
@client.command()
async def context_sure(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/558852116173684763/608072111818539048/image0.png?width=1656&height=306")
@client.command()
async def f_context(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/499967027583123456/608071838320295936/Screenshot_20190805-235953-01.jpeg?width=1878&height=236")
@client.command()
async def chatisdad(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/MVksNQVJP7Cu4urXhZ-o0QQKEVVFY2j9_mSU5tahT6E/https/media.tenor.com/images/ff97472b457bc54cc585a7e197f1e7ed/tenor.gif?width=440&height=338")
@client.command()
async def boop(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/592844231438106624/630393389782663190/ac7dc2d-1.gif?width=720&height=720")
@client.command()
async def boop2(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/rAcjlmwXvvzbL1aPer_x0bbS_1Sss6BXabsoXSVStl4/https/media.tenor.com/images/42a6d9f690041a87c3df6b969baaa2db/tenor.gif?width=440&height=436")
@client.command()
async def boop3(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/-RyWUYT9d-kpCQOCq0wTwYPMyZPx8LhAkKCuGX02ClQ/https/media.tenor.com/images/69719e74cda94ffcd316531c491ff7f0/tenor.gif?width=440&height=440")
@client.command()
async def boop4(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/Ige_Qq0iiZTM0CKwLTELR8eyLTV9J_v2YWusUzzDm34/https/media.tenor.com/images/835e8163c3a07a97b861cd7b76bd0bf0/tenor.gif?width=440&height=246")
@client.command()
async def boop5(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/K_zR4DYY-70X_WgmPmCwdKQfcsO7TLqX1DDGVY6ZrD0/https/media.tenor.com/images/8606dd8841fe08e2c3e2d939b7f54ba8/tenor.gif?width=440&height=240")
@client.command()
async def boop10(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/5SelnrxxkmUB4YxvoKiID-YbWb-IWRlE_8i961lf0vo/https/media.tenor.com/images/688339a8e6daa3b4a2345617b52e2e6b/tenor.gif?width=440&height=312")
@client.command()
async def aaaaaaaa(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/hOXV-lBI3SHbN0F-NFrdoZCr5tAIz9baF2WJDb9yLZU/https/i.imgur.com/CqeVTz9h.jpg?width=480&height=794")
@client.command()
async def rix_ping(ctx):
  await ctx.send("copy paste to ping Rix because he has been causing trouble `<@133299944248442880>`")
@client.command()
async def meghantrainor(ctx):
  await ctx.send("https://youtu.be/e_s83bdE2Zk")
@client.command()
async def getit(ctx):
  await ctx.send(f"https://media.tenor.co/videos/0a9cb30a9712154841ad66227fce84e0/mp4")
@client.command()
async def hswonder(ctx):
  await ctx.send(f"HS Wonder The Seals Command Ship Where All The Business Happens, Captained By Unknown https://cdn.discordapp.com/attachments/558862066341904384/575876489283895306/20190509_033839.jpg")
@client.command()
async def narwhal(ctx):
  await ctx.send(f"https://media.discordapp.net/attachments/570667118023016459/668887117111361606/narwhal.png?width=794&height=794")

@client.command()
async def annepressedf(ctx):
  await ctx.send(f"https://images-ext-2.discordapp.net/external/uu_oZ7XX8QZg2Vaq4PePmGI1BMocNT4D64C1AEy_Kxk/https/media.tenor.com/images/a5ca668d6a1b65c47a500ca0ef2faccf/tenor.gif?width=440&height=248")
@client.command()
async def chatrevive(ctx):
  await ctx.send(f"https://images-ext-1.discordapp.net/external/qefYydw12DJsCIlSWkv72oCj6mSfYwfspwX4CFIU5AE/https/media.tenor.com/images/1e62a3810c9178e844fdcb4fe7207234/tenor.gif?width=320&height=180")
@client.command()
async def go(ctx):
  await ctx.send(f"**Mentioned** seals please go ahead and **start** jumping towards the client. **All** other seals please **stand down.**")
@client.command()
async def night(ctx):
  await ctx.send("**Good night, Seal. Good work. Sleep well. I'll most likely repair you in the morning.**")
@client.command()
async def leaving(ctx):
  await ctx.send(f"https\://media.tenor.com/images/5239bd6c955f9bc3599085447b9c6cb7/tenor.gif")
@client.command()
async def sylpeace(ctx):
  await ctx.send(f"https\://tenor.com/view/emiru-cosplay-ahri-peace-cute-gif-16129981")
@client.command()
async def sealul8r(ctx):
  await ctx.send(f"https\://media.tenor.com/images/05a062a896f47808ac221bedeca04a56/tenor.gif")
@client.command()
async def snails(ctx):
  await ctx.send(f"https://cdn.discordapp.com/attachments/499967027583123456/603994494169251860/DSC_0006.JPG")
@client.command()
async def gibkfdrill(ctx):
  await ctx.send("Hey <@&635147239244824579> and <@&593518972817637386> the person using this command would like an impromptu drill")
@client.command()
async def sealloving(ctx):
  await ctx.send(f"https://media.tenor.com/images/cec933defd3ff8c1590c5a0bc380540c/tenor.gif")
@client.command()
async def cbmining(ctx):
  await ctx.send("``` Code Black mining navigation You will have no HUD, this will explain how to navigate the mining zone. Field navigation You can find the location of your ship and other things using the radar module only. Select the item you want on the left hand panel, then go towards it using your radar. Finding your mats Engage your cargo scoop, and then proceed towards the location of the chunk as shown above. Rise your ship above the chunk slightly once in visual, then further go with a speed of less then 40. ```")
@client.command()
async def nagihazard(ctx):
  await ctx.send("<\:nagihazard\:646319015597441034>")
  #idk
@client.command()
async def clear(ctx):
  await ctx.send("**Official Hull Seals Case Report Form** *(not for training drills)* https\://hullseals.space/paperwork/")
@client.command()
async def canys(ctx):
  await ctx.send(f"https://cdn.discordapp.com/attachments/617832061524246548/672465676023234599/sketch-1580398700384.png")
@client.command()
async def fu(ctx):
  await ctx.send(f'https://media1.tenor.com/images/b20d3ddbcab55d73772e111d96fdc5f6/tenor.gif?itemid\=12960855')
@client.command()
async def anne(ctx):
  await ctx.send(f"https://media.tenor.com/images/eff14acd47a18d4a3694bb949f43c6ce/tenor.gif")
@client.command()
async def coffee(ctx):
  await ctx.send(f"https://media.tenor.com/images/368f4a609bcf69d32ee49e2d925dd469/tenor.gif")

@client.command()
async def fabseal(ctx):
  await ctx.send(f"https://media.tenor.com/images/a96326a7b68043cba19481fb963f3c22/tenor.gif")
@client.command()
async def udidit(ctx):
  await ctx.send("**wow you actually did it... I mean of course you did it you are the best... congrats 🎉🎉🎉**")
@client.command()
async def rixxshower(ctx):
  await ctx.send(f"https://cdn.discordapp.com/attachments/365904573493411850/667123021445857328/unknown.png")
@client.command()
async def beer(ctx):
  await ctx.send(f"https://media.tenor.com/images/2098804f7059249052b7cc1d74ddc816/tenor.gif")
@client.command()
async def noodletyping(ctx):
  await ctx.send(f"https://i.imgur.com/o72WhBX.jpg")
@client.command()
async def creator(ctx):
  await ctx.send("unknown made the original, mika ported to replit. so yeah unknown made it. thank u unknown for the text file <3")
@client.command()
async def hsbask(ctx):
  await ctx.send("HS Bask The Seal Navy's Flagship That Accomodates All The Seals. https://cdn.discordapp.com/attachments/558862066341904384/575876268583551007/20190509_032245.jpg")
@client.command()
async def archer(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/617854559552798780/sketch-1567377938391.png")
@client.command()
async def howls(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/617854562396536833/sketch-1567376948771.png")
@client.command()
async def hack(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/617854557816619011/sketch-1567374960884.png")
@client.command()
async def halfpenny(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/617854562396536832/sketch-1567376861790.png")
@client.command()
async def keni(ctx):
  await ctx.send(f"https://cdn.discordapp.com/attachments/617832061524246548/621102769604001792/sketch-1567381602718.png")
@client.command()
async def skyrose(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/684055240731000937/sketch-1583161645943.png")
@client.command()
async def phelankaaa(ctx):
  await ctx.send("https://m.imgur.com/a/7vRCFNM")

@client.command()
async def bacon(ctx):
  await ctx.send("https://www.youtube.com/watch?v\=Wd2qRSzCj84")
@client.command()
async def stare2_electricboogaloo(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/558852116173684763/618605512413675571/20190903_132839.jpg")

@client.command()
async def nagi(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/684058561629782042/sketch-1583162665367.png")
@client.command()
async def modemus(ctx):
  await ctx.send("https://media.tenor.com/images/f435b2b155227283892107934545a3c4/tenor.gif")
@client.command()
async def nemisis(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/617854557308846090/sketch-1567376992553.png")
@client.command()
async def sylvia(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/617832061524246548/684055241192374312/sketch-1583161482584.png")
#keep_alive()
key = "MTA0OTQwMzkyMTU1MjEzNDIxNQ.G2NF7V.oH2UpE6VIZ4a_HS1gx1J31be9_d1zR8HzA3mzw"
client.run(key)
