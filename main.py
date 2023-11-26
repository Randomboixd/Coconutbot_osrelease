import discord
from discord.ext import tasks
import os
from itertools import cycle
import random
import json
import asyncio
import requests
import shutil
import hashlib
from cryptography.fernet import Fernet

if os.path.exists('./key.json'):
  Releasetype = "Production'nt"
else:
  Releasetype = "Production"

if Releasetype == "Production":
  version = "V-2.4"
else:
  version = "NIGHTLY"

def hashmii(data:str, mode:str="gln"):
  has = hashlib.sha256()
  data = data.encode()
  has.update(data)
  return has.hexdigest()

ReviewChanneld = 0 # Discord channel where Review messages are sent.
PollChanneld = 0 # Discord channel where poll messages are sent.

class Typedown: # Why...

    # Why did i make this.


  def compile(data):
    data = data.replace('<newline>', '\n')
    data = data.replace('<sus>', ':flushed:')
    data = data.replace('<nl>', '\n')
    data = data.replace('<newlinechar>', '\n')
    data = data.replace('<<instancetype>>', Releasetype)
    data = data.replace('<<ver>>', version)
    data = data.replace('<<glibberish>>', 'sdfhsjdhfshbfhsgfhsbfnjhsvfgvshbfsnfdakjhsdlsgfdhv')
    data = data.replace('<', '')
    data = data.replace('>', '')
    
    return data

clrs = cycle([0x8c0300, 0x548903, 0x018b12, 0x038089, 0x01388b, 0x27028a, 0x69018b, 0x8c005b, 0x8b0104]) # Used to be for a rainbow colors thing till i realized it was against tos so i ultimately removed it... except this variable.

def getdeckey(type:str="gln"):
  if type == "gln":
    if Releasetype != 'Production':
      with open('Encryption.json', 'r') as f:
        key = json.load(f)

      return key["deckey"].encode()
    else:
      key = os.getenv('Encryption_Key')
      return key.encode()
  if type == "ins":
    if Releasetype != 'Production':
      with open('Encryption.json', 'r') as f:
        key = json.load(f)

      return key["insdeckey"].encode()
    else:
      key = os.getenv('Insider_Encryption_Key')
      return key.encode()
  if type == "b":
    if Releasetype != 'Production':
      with open('Encryption.json', 'r') as f:
        key = json.load(f)
      return key["bmsgdeckey"].encode()
    else:
      key = os.getenv('Bulletin_Encryption_Key')
      return key.encode()


def enc(text:str, type:str="gln"): # Just an encryption function
  if type == "gln":
    key = getdeckey()
    ferne = Fernet(key)
    text = text.encode()
    encmsg = ferne.encrypt(text)
    return encmsg.decode()
  if type == "ins":
    key = getdeckey("ins")
    ferne = Fernet(key)
    text = text.encode()
    encmsg = ferne.encrypt(text)
    return encmsg.decode()
  if type == "b":
    key = getdeckey("b")
    ferne = Fernet(key)
    text = text.encode()
    encmsg = ferne.encrypt(text)
    return encmsg.decode()

def dec(enctext:str, type:str="gln"): # same for decryption.
  if type == "gln":
    key = getdeckey()
    ferne = Fernet(key)
    enctext = enctext
    msg = ferne.decrypt(enctext)
    return msg.decode()
  if type == "ins":
    key = getdeckey("ins")
    ferne = Fernet(key)
    enctext = enctext
    msg = ferne.decrypt(enctext)
    return msg.decode()
  if type == "b":
    key = getdeckey("b")
    ferne = Fernet(key)
    enctext = enctext
    msg = ferne.decrypt(enctext)
    return msg.decode()


def check_perms(type):
  if type == "adv":
    with open('./configuration/advancements.config') as f:
      ff = json.load(f)
    if ff["enabled"] == "True":
      return True
    else:
      return False

def Patch_for_DB(string:str): # lmao this won't help you with sql injection (yeah i wanted to use sqlite for this bot :skull: )
  newstr = string
  newstr = newstr.replace('DROP', '')
  newstr = newstr.replace(';', '')
  newstr = newstr.replace('SELECT', '')
  newstr = newstr.replace('FROM', '')
  newstr = newstr.replace('INSERT', '')
  newstr = newstr.replace('INTO',  '')
  newstr = newstr.replace('IN', '')
  newstr = newstr.replace(',', '')
  newstr = newstr.replace('TABLE', '')
  return newstr

Administrators = [] # Array of discord Ids... Put your id in here... will allow you to accept poll submissions.

Owner_name = "Your name here" # Used to be my name, buut let's say you operate this bot ok?

activity= discord.Activity(name=f"{str(version)}", type=discord.ActivityType.watching)

bot = discord.Bot(intents=discord.Intents.all() ,activity=activity)

fun = discord.SlashCommandGroup("fun", "99% of the commands here are 4 fun")

bulletinboard = discord.SlashCommandGroup("bulletinboard", "Revival of my old 'message board system'")

howto = discord.SlashCommandGroup("guide", "Your One step guide to everything coconutbot")

connectpass = discord.SlashCommandGroup("fancyannouncements", "Ngl They be fancy doe")

gln = discord.SlashCommandGroup("gamelabnetwork", "Integration With GLN")

settings = discord.SlashCommandGroup("settings", "Control CoconutBot to your liking!")

hints = discord.SlashCommandGroup("hints", "Get Hints on Secret Roles.")

insiders = discord.SlashCommandGroup("insider", "Under Developement Content!")

password = discord.SlashCommandGroup("keys", "Redeem your CoconutKeys!")


eco = discord.SlashCommandGroup("economy", "?")

vote_system = discord.SlashCommandGroup("polls", "Make your own polls!")


review = vote_system.create_subgroup(name="review", description="These are for admins only!")

games = discord.SlashCommandGroup("games", "Some Asynchronous games up your adshole")
christmas = discord.SlashCommandGroup("christmas", "A Gift For Christmas... From Coconutbot's Creator.")



glnidsettings = discord.SlashCommandGroup("gln_id_settings", "Configure Your Gamelab Network identificant!")

administrative = discord.SlashCommandGroup("administrative", "Warning! Make sure this is on ADMINS Only!")

GLNADDRESS = "https://< Your GLN Address here >" # Set this if you want GLN Support, follow guide to set up gln

GLNREGISTERADR = GLNADDRESS + "/gameservice/Webservice/Accountserver/RegisterServiceID/Account"
GLNGAMERIDREG = GLNADDRESS + "/gameservice/Webservice/Accountserver/RegisterServiceID/GamerID"

GLNDATAREQUESTURL = GLNADDRESS + "/gameservice/Webservice/Accountserver/GetTag"



class rickroll(discord.ui.View): 
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.blurple, emoji="😀") 
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # 😏




@fun.command(name='billnye', description="he the scienc guy (my fav command)")
async def billnye(ctx):
  ra = random.randint(0, 99999)
  if ra != 69420:
    await ctx.respond('https://www.youtube.com/watch?v=1mHDuMJHyJo') # pls don't sue me disney. i'll remove this if needed.
  else:
    embed=discord.Embed(title="You Unlocked a (not so) Secret Advancement!", description="Wait so Coconutbot has these? (NO)", color=0x06776b)
    embed.add_field(name="Im Pretty sure thats not bill nye.", value="Get the Magic number! (69420)", inline=False)
    embed.add_field(name="Reward", value="Your Time wasted.", inline=False)
    embed.add_field(name="There is no context. Your Ears are now blessed.",value=".", inline=False)
    embed.set_footer(text="You are a lucky man walking!")
    await ctx.send(embed=embed)
    await ctx.respond('https://www.youtube.com/watch?v=rEcOzjg7vBU')
    

@fun.command(name="geometrydash2", description="get info about 2.0")
async def gd2(ctx):
  await ctx.respond('.')
  await ctx.send("https://www.wikihow.com/Make-Sex-Better") # uhm.
  await asyncio.sleep(6)
  await ctx.channel.purge(limit=1)
  await ctx.send('THERE WAS A MISINPUT')
  await asyncio.sleep(0.4)
  await ctx.send('MISINPUT')
  await asyncio.sleep(0.4)
  await ctx.send('CALM DOWN!')
  await asyncio.sleep(0.4)
  await ctx.send('YOU CALM THE FK DOWN!')
  await asyncio.sleep(3)
  await ctx.send('IT WAS A MISINPUT')

@fun.command(name="drink", description="its very evil")
async def drink(ctx):
  await ctx.respond('https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831')
  role = discord.utils.get(ctx.guild.roles, name="The Drink is Dangerous")
  user = ctx.author
  if role in user.roles:
    return
  else:
    embed=discord.Embed(title="You Unlocked a Secret Advancement!", description="Wait so Coconutbot has these?", color=0x06776b)
    embed.add_field(name="The Drink is Very Dangerous", value="Use the /fun drink Command. (This is an easteregg. For context go here: https://discord.com/channels/1044197813711544390/1044197814151954450/1046113775134191656)", inline=False)
    embed.add_field(name="Reward", value="The Drink is Dangerous role!", inline=False)
    embed.add_field(name="Original Inspiration for Easter Egg was @King Squirrel.", value="Backstory. (as much as i know) He was playing Red Dead Redemption 2 and found a glass of D  R  I  N  K. he Wanted to D   R   I   N   K but the game glitched him off instead.", inline=False)
    embed.set_footer(text="This is a system notification and thus cannot be unsubscribed from.")
    try:
      await user.add_roles(role)
      await ctx.author.send(embed=embed)
    except:
      pass

@fun.command(name="sprite_cranberry", description="Wanna Sprite Cranberry? (Also a Meme feature)")
async def sprite(ctx):
  await ctx.respond('Wanna Sprite Cranberry? (Bot Fetching a random meme!)')
  try:
    array = []
    for files in os.listdir('./sprite_images'):
      with open(f'./sprite_images/{str(files)}', 'r') as f:
        augh = json.load(f)
      array.append(augh["image"])
    with open(f'./sprite_config/nerd.json', "r") as f:
      aa = json.load(f)
    maximum = aa["max"]
    
    integer = random.randint(0, maximum)

    await ctx.send(array[integer])
    await ctx.send(f"This submission's Url is: (@{array[integer]}@) Please Report this to {Owner_name} if rule breaking is found!")
  except:
    await ctx.send('Bot Failed to fetch a meme :nerd:')

@fun.command(name="submit_cranberry", description="Submit your Cranberries. (jeez thats so out of context). Memes are allowed too!")
async def cransubmit(ctx, url: discord.Option(str, description="A link to your Image.")):
  await ctx.respond('Preforming Security Checks on your image! Hold Tight! This may take a while!')
  if "bypassdisco-rd.ggfilterforfucksake" in url:
    a = 1
  else:
    a = 2
  if "discord.gg" in url:
    await ctx.send('Your Submission Contains a Discord Invite Link! Submission Declined!')
    return
  if "http" in url:
    pass
  else:
    await ctx.send('Thats Not a valid link! Note It must either start with Http or Https !')
    return
  if ".gg" in url:
    if a != 1:
      await ctx.send('Your Submission is suspected as an Invite link! Dont use image hosts which use the .gg url!')
      return
  if "<" in url:
    await ctx.send('Your Submission was declined as it Contains one of the following symbols: < , > # & ')
    return
  if "," in url:
    await ctx.send('Your Submission was declined as it Contains one of the following symbols: < , > # & ')
    return
  if ">" in url:
    await ctx.send('Your Submission was declined as it Contains one of the following symbols: < , > # & ')
    return
  if "#" in url:
    await ctx.send('Your Submission was declined as it Contains one of the following symbols: < , > # & ')
    return
  if "&" in url:
    await ctx.send('Your Submission was declined as it Contains one of the following symbols: < , > # & ')
    return
  if "porn" in url:
    await ctx.send('Your Submission is suspected Porn. Declined!')
    return
  if "sex" in url:
    await ctx.send('Your Submission is suspected Porn. Declined!')
    return
  if a == 1:
    url = url.replace('bypass', '')
    url = url.replace('-', '')
    url = url.replace('filterforfucksake', '')
  await asyncio.sleep(10)
  await ctx.send('Hmm. Your Submission Survived the filters! Nice! Now Its time to record your Meme into the cool kids list!')
  with open(f'./sprite_images/{str(random.randint(0, 999999))}.json', 'x') as f:
    key = {
      "image": url
    }
    json.dump(key, f)
  with open('./sprite_config/nerd.json', 'r') as f:
    v = json.load(f)
  with open('./sprite_config/nerd.json', 'w') as f:
    data = {
      "max": int(v["max"]) + 1
    }
    json.dump(data, f)

@fun.command(name="has_bitches", description="Have bitches or dont. Its a life changeing question") # its Changing dumbass
async def bitches(ctx):
  a = random.randint(0,2)
  if a == 1:
    await ctx.respond(f"{str(ctx.author)} Has bitches")
  else:
    await ctx.respond(f"{str(ctx.author)} Does'nt Have bitches. Go outside!")

@fun.command(name="giveneitro", description="give someone neitro")
async def neitro(ctx, membr:discord.Member):
  if os.path.exists(f'./ignore/{str(membr.id)}.acc') != True:
    await ctx.respond(f'successfully sent sht to {str(membr.mention)}')
    try:
      await membr.send("Modmail: You successfully received neitro in our giveaway. (fake)")
      await membr.send("https://discord.gift/Udzwm3hrQECQBnEEFFCEwdSq")
    except:
      await ctx.respond(f'I cant send shit to {str(membr.mention)}"s discord dms. he locked his dms. :nerd: "')
  else:
    await ctx.respond('Doughnut distrub mode is turned on for that user.')

@fun.command(name="suprise", description="nitro alert")
async def gibrealneitro(ctx):
  await ctx.respond('Click the button below!' ,view=rickroll())
  try:
    if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1') != True:
      open(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1', "x").close()
  except:
    pass

@fun.command(name="sendnuke", description="Send a nuke to someone's door! (for legal reasons. this is a joke)")
async def sendnuke(ctx, luckyperson: discord.Member):
  if os.path.exists(f'./ignore/{str(luckyperson.id)}.acc') != True:
    try:
      await ctx.respond('they got a neic mail!')
      await luckyperson.send('You got mail!')
      await asyncio.sleep(4)
      await luckyperson.send('What is it?')
      await asyncio.sleep(2)
      await luckyperson.send('TACTICAL NUKE INCOMING!')
      await asyncio.sleep(2)
      await luckyperson.send('https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831')
    except:
      await ctx.send(':nerd: THEY DISABLED DMS! :rofl: :rofl:')
  else:
    await ctx.respond('Do not Distrub is turned on for that person...')


@fun.command(name="sendkfc", description="Send KFC to someone's Door! They WILL like it!")
async def kfc(ctx, person: discord.Member):
  if os.path.exists(f'./ignore/{str(person.id)}.acc') != True:
    try:
      
      await person.send(f'Hey you! Yes YOU! {str(ctx.author)} Sent you some KFC!')
      await ctx.respond('They got some KFC!')
      await person.send('https://tenor.com/view/fried-chicken-crispy-gif-26189851')
      try:
        if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1') == True:
          if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2') != True:
            open(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2', 'x').close()
      except:
        pass
    except:
      await ctx.respond('They calmly refused. (Message was blocked by discord!) Possible Reasons: user has DMS turned off')
  else:
    await ctx.respond("I Was told Not to send fun stuff into this man's inbox. (Message blocked by CoconutBOT)")


@bulletinboard.command(name="read", description="Read a specific Message!")
async def readbulletin(ctx, bulletin: discord.Option(str)):
  #try:
    bulletin = bulletin.replace('/', "")
    with open(f'./bulletinmsg/{str(bulletin)}.msg') as f:
      ff = json.load(f)
    bname = ff["name"]
    bcontext = dec(ff["context"].encode(), 'b')
    bauthor = ff["author"]
    bimg = dec(ff["authorimg"].encode(), 'b')
    embed=discord.Embed(title=f"Message Posted by: {str(bauthor)}", color=0x1092a0)
    embed.set_thumbnail(url=bimg)
    embed.add_field(name=bname, value=bcontext, inline=True)
    embed.set_footer(text="BulletinBoard Integration Version 0.2")
    await ctx.respond("Done! I sent you a DM!")
    #try:
    await ctx.author.send("Here is your message!")
    await ctx.author.send(embed=embed)
    #except:
    #  await ctx.send("hmm it seems i can't send mail to your account! Please enable Direct Messages from members in this server's privacy settings please!")
  #except:
  #  await ctx.respond("That Post does not exist!")

@bulletinboard.command(name="write", description="Write a letter that anyone can read!")
async def writebulletin(ctx, messagename: discord.Option(str, description="So.. What should we call your message?"), message: discord.Option(str, description="What do you want your message to be? (SUPPORTS TYPEDOWN) leave something nice!"), msgimg:str="https://cdn.discordapp.com/attachments/1045369616911839302/1045397288891187230/luayer.png"):
  messagename = messagename.replace('/', "")
  message = Typedown.compile(message)
  message = str(enc(message, 'b'))
  msgimg = str(enc(msgimg, 'b'))
  try:
    with open(f'./bulletinmsg/{str(messagename)}.msg', 'r') as f:
      j = json.load(f)
    await ctx.respond('That Message Already Exists!')
  except:
    await ctx.respond('No Conflicts found! Writing time...')
    try:
      a = open(f'./bulletinmsg/{str(messagename)}.msg', 'x')
      a.write('{}')
      a.close()
    except:
      await ctx.send('Never mind! I found conflicts!')
      return 
    del a
    with open(f'./bulletinmsg/{str(messagename)}.msg', 'w') as f:
      
      data = {
      "name": messagename,
      "author": str(ctx.author),
      "authorimg": msgimg,
      "context": str(message),
      "uuid": enc(str(ctx.author.id), 'b')
      }
      json.dump(data, f, indent=4)
    await ctx.send('Successfully Registered Message! Also Sent you a dm with useful info!')
    await ctx.author.send(f'Hello! You Created a message right? Nice! Here are a few info about it. Its called {messagename}. Note its case sensitive.')
      
@bulletinboard.command(name="delete", description="The legends say. If you made it. You can delete it.")
async def bulletindelete(ctx, name: discord.Option(str, description="Name of the bulletin you wanna delete")):
  name = name.replace('/', "")
  with open(f'./bulletinmsg/{str(name)}.msg') as f:
    d = json.load(f)
  if dec(d["uuid"], 'b') == str(ctx.author.id):
    os.remove(f'./bulletinmsg/{str(name)}.msg')
    await ctx.send('Deleted File!')
    await ctx.author.send(f'You Have deleted {str(name)} of of Coconutbot Servers!')
  else:
    embed = discord.Embed(title="Critical Error", color=0xff0000)
    embed.add_field(name="Error!", value="You Don't Own the message!", inline=True)
    embed.add_field(name="But i did?", value=f"Contact {Owner_name} on discord for help!")
    await ctx.send(embed=embed)

@bulletinboard.command(name="list", description="Show Me ALL Existing Bulletins!")
async def bulletinlist(ctx):
  fullmessage = ""
  for message in os.listdir('./bulletinmsg/'):
    fullmessage = fullmessage + f"   {message}"
  fullmessage = fullmessage.replace('.msg', '')
  await ctx.respond(f'I got the following stuff: {fullmessage}')

@howto.command(name="typedown", description="Learn our new Markdown like system!")
async def typedwon(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="How to Typedown", description="What is Typedown?", color=0x06776b)
  embed.add_field(name="What?", value="Its a markup Language. Allowing you to express yourself a lil better. Such as Add newlines to your stuff... Yeah thats the main use.", inline=False)
  embed.add_field(name="Cool Where do i start?", value="You gotta find an input prompt. Input Prompts like Bulletinboard make support it. so that can be your test ground.", inline=False)
  embed.add_field(name="Whats the Syntax?", value="Its simple! Look Below to see the results of what i type! (1) <newline> or <nl> or <newlinechar> || (2) The nerdy stuff <<instancetype>> or <<ver>>", inline=False)
  embed.add_field(name="Output", value="(1) It will Result in a newline \n Like this! || (2) Production't or Production! NIGHTLY or the bot's version string..", inline=False)
  embed.add_field(name="Thats it!", value="You have Mastered Typedown.", inline=True)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="bulletinboard", description="How do i bulletinboard")
async def bbguide(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="How to BulletinBoard", description="So you wanna know how bulletin board works?", color=0x06776b)
  embed.add_field(name="What?", value="Bulletin Board is well. A bulletin board. You put messages and you read messages... Its like your school's little bulletin board.", inline=False)
  embed.add_field(name="Why?", value="Because why not? Its an optional feature. but you can also store meme links init.", inline=False)
  embed.add_field(name="Reading", value="Reading allows you to read. (yeez gotta stop with these stuff). Just use /bulletinboard read (and the name of the bulletin you wanna read)", inline=False)
  embed.add_field(name="Speaking of Reading. (Listing)", value="You wanna read. but you dont know what. You can use /bulletinboard list to list ALL bulletins registered. Simply get the name you want to read. and use /bulletinboard read to read it", inline=False)
  embed.add_field(name="Writing", value="Writing is important. Just /bulletinboard write (Name of the bulletin you wanna make) (Add your text) [optional( Your custom banner image)]. thats it. you made it.", inline=False)
  embed.add_field(name="Deleting", value="Deleting can ONLY be done if you made that message! just /bulletinboard delete (Name of the Message). After that. the bot does some checks and deletes your message! You'll also get a dm confirming what you done!", inline=True)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="gamelabnetwork", description="How to i use gamelab network?")
async def glnguide(ctx):
  if False != True:
    await ctx.respond('I have messaged you!')
    embed=discord.Embed(title="How to Gamelab Network", description="For indepth info about GLN. go to < this link has been removed due to... the domain not being owned by me anymore (_osrelease edit) >", color=0x06776b)
    embed.add_field(name="Registering", value="In order to use Commands starting with GLN You MUST get a gamelab Network account! Just use /GLN make or /GLN import <Account Key> (if you have an existing gln install) to get an account!", inline=False)
    embed.add_field(name="Playing", value="I Tried to adapt Most stuff gamelab network has to offer! but the bot explains EVERYTHING. so i dont need this topic rn.", inline=False)
    embed.add_field(name="Deleting Your GLN Account.", value="Gamelab Network allows you to just Throw away your account in an instant. Just type /GLN delete and you did it. (This WILL Erase your Coins!)", inline=False)
    embed.set_footer(text=f"Guide is written by {Owner_name}!")
    await ctx.author.send(embed=embed)
  else:
    await ctx.respond('Gamelab Network for Coconutbot Is still in development. i just decided to add this early.')

@howto.command(name="fun_stuff", description="how do i fun stuff?")
async def ffguide(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="How to fun", description="So you wanna have some fun? Coconutbot has that!", color=0x06776b)
  embed.add_field(name="Cool! What can i do?", value="... spam your ''Friends'' with useless dms! and some cool stuff.", inline=False)
  embed.add_field(name="You got me. So what now?", value="Just start typing /fun and you'll See all avalable commands!", inline=False)
  embed.add_field(name="Bot said he doesnt send messages to that person!", value="It depends. if the bot says it CANNOT because discord. then the user has DMS off. If it says it can't because of Do Not Disturb then they enabled DO NUT distrub on their bot profile.", inline=False)
  embed.add_field(name="I want that too! How do i?", value="Simply use /settings toggledms. If its off. it will turn it on. if its on. it will turn it off. (This prevents me from sending messages other than guides and bulletinposts to you!)", inline=False)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="cranberries", description="Cranberries are tasty. but what if we can taste them on discord?")
async def ccguide(ctx):
  await ctx.respond('I have messaged you!')
  embed=discord.Embed(title="Cranberries are tasty. and so are memes", description="Wanna cranberry was first made as a joke from King Squirrel on the server. Now it became our main meme distribution system... Lets Talk Cranberries.", color=0x06776b)
  embed.add_field(name="GIVE ME THE MEMES!", value="Great! Nice to see your appreciation for memes! Lets get right into it. You Can get a ''Cranberry'' By running /fun sprite_cranberry. Now Go and Enjoy Your Memes. Or Cranberries. Whatever.", inline=False)
  embed.add_field(name="Sharing is caring", value="So you wanna share your memes. (or cranberries) You can use the /fun submit_cranberry command alongside the url for your image, After a quick check it will register it to the berry system. What you don't have a link for your cranberry?", inline=False)
  embed.add_field(name="I Need some cranberrys right now.", value="you can find me at X City X Street XX in room 1 on pictochat! (please give me cranberries)", inline=False)
  embed.add_field(name="About our yummy api", value="You'll Be able to order Cranberrys free of charge for your app once i launch the api docs and well. the api. man if it would be this easy to get cranberries.", inline=False)
  embed.add_field(name="GIVE ME CRANBERRIES", value="I like how this got from just Sprite Cranberry to me literally being hungry lol (edit: i received cranberries)")
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@howto.command(name="advancements", description="Wait those exist?")
async def advguide(ctx):
  await ctx.respond('I have messaged you!')
  embed = discord.Embed(title="Super Secret Tiny Developer Extra Virus Funky Kong Included Advancements", description="Wait those exist?", color=0x06776b)
  embed.add_field(name="Why does VS-Code bug when i try to just write embeds?", value="No idea.", inline=False)
  embed.add_field(name="How do i obtain them?", value="Well if you didnt read the title... you can't but also you can. Its up to you to find 'em All! Its like pokemon. Gotta Catch 'em all! (firered version)", inline=False)
  embed.add_field(name="What do i do with them?", value="nothing.", inline=False)
  embed.set_footer(text=f"Guide is written by {Owner_name}!")
  try:
    await ctx.author.send(embed=embed)
  except:
    await ctx.send('It seems i cant message you... You may have to turn Direct Messages from Server Members on.')

@settings.command(name="toggledms", description="I will happily refuse messages sent to you via coconutbot! (required stuff are not modified)")
async def disabledms(ctx):
  if os.path.exists(f'./ignore/{str(ctx.author.id)}.acc') == True:
    os.remove(f'./ignore/{str(ctx.author.id)}.acc')
    await ctx.respond('You have been deleted from the Do not disturb list!')
    await ctx.author.send('You removed yourself from the Do not disturb list! You will now receive other stuff')
  else:
    a = open(f'./ignore/{str(ctx.author.id)}.acc', 'x')
    a.close()
    await ctx.respond('You have been added to the chill zone! Wanna get out? run the command again!')
    await ctx.author.send('Do not distrub was turned on. However Important System messages like this will still be sent!')

@settings.command(name="remove_special_roles", description="Coconutbot can give you some secret roles. This tool can remove them!")
async def remove_special_roles(ctx):
  await ctx.respond('The proccess has been started! I will DM You when it finishes!')
  role = discord.utils.get(ctx.guild.roles, name="The Drink is Dangerous")
  user = ctx.author
  if role in user.roles:
    await user.remove_roles(role)

  role = discord.utils.get(ctx.guild.roles, name="How Did we get here?")
  user = ctx.author
  if role in user.roles:
    await user.remove_roles(role)
  await asyncio.sleep(20)
  try:

    await ctx.author.send('Notice: Your Request to remove your special roles have been completed! Thanks for Using CoconutBot - The Coconutbot Team')
  except:
    await ctx.send('I Cant send messages to you! But your Request Have been completed!')

  

@gln.command(name="make", description="First command to start your journey.")
async def makegln(ctx):
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
    await ctx.respond('Starting Account Generation. (Sent you some stuff via dms!)')
    await ctx.send('Set Up Your Username! Respond in 15 Seconds with a Username! Dont Respond if you wanna use your Discord Tag as your Username!')
    try:
      breh = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
      breh = breh.content
    except:
      await ctx.send('Time out! Using Your Discord Tag as your Username!')
      breh = str(ctx.author)[:-5]
    
    await ctx.send('Fingers Crossed...')
    aa = requests.get(GLNREGISTERADR)
    if aa.status_code != 200:
      await ctx.send('Damn it! It Failed! (Error: Connection is not 200!) good luck debugging :)')
    else:
      if aa.json()["Status"] == "Registered":
        b = open(f'./gln/{str(ctx.author.id)}.id', 'x')
        b.write('{}')
        b.close()
        with open(f'./gln/{str(ctx.author.id)}.id', 'w') as f:
          accenc = str(aa.json()["ServiceAccountID"])
          accenc = str((enc(accenc)))
          accpkg = {
            "Auth": accenc
          }
          json.dump(accpkg, f)
        aaa = requests.post(GLNGAMERIDREG, params={
          "gsid": aa.json()["ServiceAccountID"],
          "gid": breh,
          "cheats": True
        } )
        if aaa.status_code != 200:
          await ctx.send('Damn it! It Failed! (Error: Gamer Registration connection is NOT 200!) good luck debugging :)')
        else:
          if aaa.json()["Status"] == "Operation Success!":
            await ctx.send('You Have Successfully Registered a Gamelab Network ID! I sent Some Cool stuff about your account in your mailbox!')
            embed = discord.Embed(title="Success!", description="You Successfully Aqquired a Gamelab Network ID!", color=0x06776b)
            embed.add_field(name=f"Your Gamer Name (copy and pasted from your discord tag): {str(ctx.author)}", value=".", inline=False)
            embed.add_field(name=f"Your Authentication ID! (DONT SHARE!!!): {str(aa.json()['ServiceAccountID'])}", value=".", inline=False)
            embed.add_field(name="You Can now Gamelab Network Services with Coconutbot!", value=".", inline=False)
            embed.set_footer(text="From Coconut Bot Developer team and Gamelab Network development team (im alone so dont expect a large team lol)")
            await ctx.author.send(embed=embed)
  else:
    await ctx.respond('You already have a gamelab Network account!')

@gln.command(name="import", description="Already have a GLN ID? Import it!")
async def importgln(ctx, glnid: discord.Option(str, description="You can obtain this by opening up Account.Data with an editor")):
  if os.path.exists(f"./gln/{str(ctx.author.id)}.id") != True:
    await ctx.respond('Checking this ID With Gamelab Network! Hold on')
    reg = requests.post(GLNADDRESS + "/gameservice/Webservice/Accountserver/Exists", params={"gid":glnid})
    if reg.json()["Exist"] == "Yes":
      await ctx.send('Cool This ID Exists! Im Encrypting your ID and Linking it to THIS Discord Account!')
      d = str(glnid)
      d = enc(d)
      accpkg = {
        "Auth": d
      }
      with open(f"./gln/{str(ctx.author.id)}.id", 'w') as f:
        json.dump(accpkg, f, indent=4)
      await ctx.send('Done!')
    else:
      await ctx.send("Hmmm. Gamelab Network Cant find this ID... Did you enter it correctly? If you are coming from the Python Build. Check 'Account.Data' for the Token. Also Make sure you are NOT Using a custom server! Coconutbot Only communicates to Gamelab Network.")
      
  else:
    await ctx.respond('You Already have a gamelab network ID!')

@glnidsettings.command(name="whoami", description="Tells you who you are on Gamelab Network!", guild_ids=[1044197813711544390])
async def glnwhoami(ctx):
  if os.path.exists(f"./gln/{str(ctx.author.id)}.id") != True:
    await ctx.respond('You are NOT Registered on Gamelab Network! Please do so by running /gamelabnetwork make!')
    if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2') == True:
      if os.path.exists(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1') == True:
        role = discord.utils.get(ctx.guild.roles, name="How Did we get here?")
        if role in ctx.author.roles:
          os.remove(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1')
          os.remove(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2')
        else:
          embed = discord.Embed(title="Secret Advancement Unlocked", description="wait so coconutbot has these?", color=0x06776b)
          embed.add_field(name="How did we get here?", value="Woah you actually got this! I though i hid it really hard!", inline=False)
          embed.add_field(name="Reward", value=f"How did we get here? Role. and a thank you from {Owner_name}")
          await ctx.author.add_roles(role)
          embed.set_footer(text="This is a system notification and thus cannot be unsubscribed from.")
          await ctx.author.send(embed=embed)
          os.remove(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog1')
          os.remove(f'./adv_how_dd_we_g/{str(ctx.author.id)}.prog2')
        

  else:
    with open(f'./gln/{str(ctx.author.id)}.id', 'r') as f:
      ff = json.load(f)
      if 'g' in str(ff["Auth"]):
        auth = str(ff["Auth"]).encode()
        authdec = int(dec(auth))
      else:
        await ctx.respond('Account Encryption Problem. This account is not ENCRYPTED (or your account hash does not start with g)! To Continue using GLN Please Run /gamelabnetwork encrypt_mii. \n Why did i do this? For sake of security. \n Does GLN encrypt data? not yet. but it will \n Does GLN Desktop encrypt stuff? No. as its 1 person only. Unlike discord where the bot is shared around.')
        return
    
    jj = requests.post(GLNDATAREQUESTURL, params={
      "gsid": authdec
    })
    if jj.status_code == 200:
      await ctx.respond(f'You are: {jj.json()["Profile"]}. You Have {str(jj.json()["Coins"])} Coins!')
    else:
      await ctx.respond('Unable To Connect to Gamelab Network!')

@glnidsettings.command(name="deleteid", description="Delete your Gamelab Network ID!")
async def glndelete(ctx, confirmation: discord.Option(str, description="Make sure this is 'Confirm' Else the proccess Will Fail!")):
  if confirmation == "9":
    embed = discord.Embed(title="Secret Advancement Unlocked!", description="wait so coconutbot has these? (YES I SAID IT FOR THE 3RD TIME)", color=0x06776b)
    embed.add_field(name="Mighty Number 9", value="At first this wasnt intended to be a refrence to Mighty No 9. but it was ALL over in my head so. THIS ISNT A MIGHTY NO 9 REFRENCE!", inline=False)
    embed.add_field(name="Reward", value="A Copy of Wii Play. Here it is: https://www.youtube.com/watch?v=Kh3ZdSjnqgw", inline=False)
    embed.set_footer(text="This is a message that you should go shower")
    await ctx.author.send(embed=embed)
    await ctx.respond(':flushed:')
  if confirmation == "Confirm":
    if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
      await ctx.respond('You Dont have a gamelab network ID! There is nothing to delete. Looking on how to disable Do not disturb? use /settings toggledms!')
    else:
      
      await ctx.respond('Starting Account Deletion!')

      await ctx.send('Do You Really Want to Delete your ID? (Respond with Yes)')
      try:
        c1 = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=4)
      except:
        c1 = ""
      if c1.content == "Yes":
        await ctx.send("Really? (Respond with Yeah)")
        try:
          c2 = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=4)
        except:
          c2 = ""
        if c2.content == "Yeah":
          await ctx.send('You got it!')
        else:
          await ctx.send('Account Deletion Canceled.')
          return
      else:
        await ctx.send('Account Deletion Canceled')
        return

      with open(f'./gln/{str(ctx.author.id)}.id') as f:
        bb = json.load(f)
        auth = str(bb["Auth"]).encode()
        authenc = int(dec(auth))
      g = requests.post(GLNADDRESS + "/gameservice/Webservice/Accountserver/DeleteServiceID", params={
        "gsid": authenc
      })
      os.remove(f'./gln/{str(ctx.author.id)}.id')
      await ctx.send('Account Deleted!')
  else:
    await ctx.respond('Safety Backoff: Please in the Confirmation parameter Write "Confirm".')

@gln.command(name="free_coins", description="Wait a ??? amount of sec and get ??? Coins for your GLN Account!")
async def glncoins(ctx):
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
    await ctx.respond("You Don't Own a Gamelab Network ID! Please Read the manual by running /guide gamelabnetwork!")
  else:
    await ctx.respond("Contacting Server! https://tenor.com/view/connecting-connect4-connect-four-connect-loading-gif-11142406")
    g = requests.get(GLNADDRESS + "/gameservice/Webservice/Gameserver/Freecoins")
    jayson = g.json()
    Coinstoget = jayson["Coins"]
    UnderWhatTime = jayson["Time"]
    await asyncio.sleep(10)
    await ctx.send(f"You'll Receive {str(Coinstoget)} In {str(UnderWhatTime)} Seconds!")
    await asyncio.sleep(UnderWhatTime)
    with open(f'./gln/{str(ctx.author.id)}.id') as f:
      ff = json.load(f)
      Auth = str(ff["Auth"]).encode()
      Authdec = dec(Auth)
    g = requests.post(GLNADDRESS + '/gameservice/Webservice/Gameserver/Claim', params={"gsid": Authdec, "amount": Coinstoget})
    await ctx.send('Done! You got your Coins added to your account!')

@glnidsettings.command(name="cold_storage", description="Move/Remove your account from the cold storage!")
async def cold_storage(ctx):
  await ctx.respond("Checking for valid accounts!")
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') == True:
    if os.path.exists(f'./gln_cold_storage/{str(ctx.author.id)}.id') != True:
      await ctx.send('Preparing Your Account to be moven to Cold Storage! Warning: If you create a new account after being moved to cold storage one has to be sacrificed!')
      shutil.move(f'./gln/{str(ctx.author.id)}.id', f'./gln_cold_storage/')
      await asyncio.sleep(4)
      await ctx.send('Operation Successful!')

      
    else:
      await ctx.send('You Have One account In Both Live And Cold Storage! One has to be sacrificed. Please Delete the Account with gln commands!')
      return
  else:
    if os.path.exists(f"./gln_cold_storage/{str(ctx.author.id)}.id") == True:
      await ctx.send('Preparing to move Your Account into Live Environment!!')
      shutil.move(f'./gln_cold_storage/{str(ctx.author.id)}.id', f'./gln/')
      await asyncio.sleep(4)
      await ctx.send('Operation Successful!')
    else:
      await ctx.send('There was no Gamelab Network Account Found In live And Cold Storage!')
      return

@glnidsettings.command(name="to_desktop", description="A Guide/way to import your Discord GLN Account to Gln Desktop!")
async def todesktop(ctx):
  await ctx.respond('Searching for an account!')
  await asyncio.sleep(4)
  if os.path.exists(f"./gln/{str(ctx.author.id)}.id") != True:
    await ctx.send("I Can't Find a Gamelab Network Identificator with this discord account!")
  else:
    await ctx.send('Found 1 Account!')
    with open(f'./gln/{str(ctx.author.id)}.id') as f:
      f = json.load(f)
    ke = f["Auth"]
    ke = int(dec(ke))
    await asyncio.sleep(2)
    await ctx.send('Sending A Test DM to Test if i can Communicate with you!')
    try:
      await ctx.author.send('.')
    except:
      await ctx.send("Due to Secret Information being shared.. I Must Talk with you with DMS. But i cant! Please check that you have Direct Messages Enabled for this server! im sorry dude")
      return
    await ctx.send('I was able to send you a message thru the api! Great lets go talk in DMS!')
    await asyncio.sleep(4)
    await ctx.author.send("Hey there. Nice to see someone sending you dms arent we? Anyway.")
    await asyncio.sleep(5)
    await ctx.author.send("1. Get The Latest Client From https://rndwebsite.ddns.net/projects/GamelabNetwork")
    await asyncio.sleep(5)
    await ctx.author.send("2. Once Connected Hit I to start Importing a GLN Account from discord!")
    await asyncio.sleep(5)
    await ctx.author.send(f"3. When Asked for Your Unique Gamelab Network Enter the Following: {str(ke)}")
    await asyncio.sleep(5)
    await ctx.author.send("4. Enjoy! (or dont. we dont judge you)")
    

@gln.command(name="guess_the_number", description="Guess the number! Its a Random Scenario Every time!", guild_ids=[1044197813711544390])
async def glnguess(ctx):
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
    await ctx.respond('You dont have a Gamelab Network Account! Please make one with /gamelabnetwork Make!')
    return
  await ctx.respond('Contacting Server! (Connection Is Secure)')
  await ctx.send('https://tenor.com/view/connecting-connect4-connect-four-connect-loading-gif-11142406')
  with open(f'./gln/{str(ctx.author.id)}.id') as f:
    ff = json.load(f)
    Auth = ff["Auth"]
    Auth = str(Auth).encode()
    AuthDec = dec(Auth)
  
  rq = requests.get(GLNADDRESS + "/gameservice/Webservice/Gameserver/GTM")

  bw = int(rq.json()["Between"])
  andd = int(rq.json()["And"])
  
  
  await asyncio.sleep(10)
  await ctx.send(f'Please Enter the number you think is the number (between {str(bw)} and {str(andd)})')
  try:
    msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=15)
  except asyncio.TimeoutError:
    await ctx.send('You have Reached your Timelimit! (15 sec)')
    return
  except:
    await ctx.send('idk something happened')
    return
  
  try:
    mesg = int(msg.content)
  except:
    await ctx.send('Your Message Isnt a number!')
    return
  Reward_Win = random.randint(80, 190)
  Reward_Lose = random.randint(20, 50)

  Num = random.randint(bw, andd)

  if mesg == Num:
    await ctx.send(f'You Win! Reward: {str(Reward_Win)} Coins.')
    await ctx.send(f'Sending to server!')
    
    requests.post(GLNADDRESS + "/gameservice/Webservice/Gameserver/Claim", params={"gsid": int(AuthDec), "amount": Reward_Win})
  else:
    await ctx.send(f'Not Quite. You Got {str(Reward_Lose)} Coins.')
    await ctx.send("Sending to server!")
    requests.post(GLNADDRESS + "/gameservice/Webservice/Gameserver/Claim", params={"gsid": int(AuthDec), "amount": Reward_Lose})

@gln.command(name='sauce_detector', description='Are you Sauce?!')
async def sauce_detector(ctx):
  await ctx.respond('Backend Development in process!')
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
    await ctx.send("You'll Need a Gamelab Network Account for dis one!")
  else:
    # gameservice/Webservice/Gameserver/sauce1
    await ctx.respond('Contacting Server! (Connection Is Secure)')
    await ctx.send('https://tenor.com/view/connecting-connect4-connect-four-connect-loading-gif-11142406')
    with open(f'./gln/{str(ctx.author.id)}.id') as f:
      ff = json.load(f)
      Auth = ff["Auth"]
      Auth = str(Auth).encode()
      AuthDec = dec(Auth)
    bruh = requests.get(GLNADDRESS + "/gameservice/Webservice/Gameserver/sauce1")
    await asyncio.sleep(5)
    person1 = bruh.json()["person1"]
    person2 = bruh.json()["person2"]
    per1dec = bruh.json()["person1desc"]
    per2dec = bruh.json()["person2desc"]
    sauce = bruh.json()["sauce"]
    await ctx.send(f"{person1}: {per1dec}")
    await ctx.send(f"{person2}: {per2dec}")
    await ctx.send('Who is sauce?')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if guess.content == person1:
      if sauce == 1:
        await ctx.send('You got it! He is the sauce!')
      else:
        await ctx.send('you murdered us all.')
        return
    elif guess.content == person2:
      if sauce == 2:
        await ctx.send('You got him!')
      else:
        await ctx.send('you murdered us all.')
        return
    else:
      await ctx.send('You murdered us all. ITS NOT EVEN A NAME LISTED!')
      return
    


@glnidsettings.command(name="encrypt_mii", description="Convert a Unencrypted Account to an encrypted one! (not required for new accounts)")
async def encryptmii(ctx):
  if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
    await ctx.respond('You dont have a Gamelab Network ID. Nothing To Encrypt!')
    return
  else:
    with open(f'./gln/{str(ctx.author.id)}.id') as f:
      augh = json.load(f)
      if 'g' in str(augh["Auth"]):
        await ctx.respond('Your Account Is Already Encrypted. Accounts After 2022 Dec 4 Are automatically Encrypted By default!')
        return
      
    await ctx.respond("Hello! Recently Coconutbot's Auth code For GLN Has changed to use Encryption instead. EncryptMii Will Detect and Encrypt Your Account!")
    await asyncio.sleep(6)
    await ctx.send('Your Account is now being encrypted by Encrypt Mii!')
    with open(f'./gln/{str(ctx.author.id)}.id', 'w') as ff:
      encd = str(augh["Auth"])
      encd = enc(encd)
      accpkg = {
        "Auth": encd
      }
      json.dump(accpkg, ff, indent=4)
    await asyncio.sleep(5)
    await ctx.send('Your Account has been encrypted by EncryptMii!')


@hints.command(name="the_drink_is_dangerous", description="Stuck? I'll Help! Just Run and I'll Give you a tip!")
async def hintdrink(ctx):
  hints = ["There is a command in the fun category...", "You Can't Live without it!", "Its Connected with Red Dead Redemption 2!", "There is a squirrel on that tree!"]
  await ctx.respond('https://www.youtube.com/watch?v=hDpsnFnovUQ')
  await ctx.send('Your Hint will be sent in 10 seconds!')
  await asyncio.sleep(10)
  await ctx.send(hints[random.randint(0, 3)])

@hints.command(name="how_did_we_get_here", description="Stuck? I'll Help!")
async def hinthow(ctx):
  hints = ["Its a Combination of 3 Specific Commands!", "I think you should have your Gamelab Network account disconnected from your account for this...", "Rick Gives You A Kfc Then Checks your Gamelab Network account details!", "You Probably gonna hate the first step...", "You Should have Dms on for that!"]
  await ctx.respond('https://www.youtube.com/watch?v=hDpsnFnovUQ')
  await ctx.send('Your Hint will be sent in 10 seconds!')
  await asyncio.sleep(10)
  await ctx.send(hints[random.randint(0, 4)])

@hints.command(name="mightyno9", description="Do you guys have Wii play? OH DON'T EVEN GET ME STARTED!")
async def hint9(ctx):
  hints = ["Its in the MOST Unexpected Place you'll search in.", "You must delete something", "Its related to a dead game.. and 9"]
  await ctx.respond('https://www.youtube.com/watch?v=hDpsnFnovUQ')
  await ctx.send('Your Hint will be send in 10 seconds!')
  await asyncio.sleep(10)
  await ctx.send(hints[random.randint(0, 2)])

@connectpass.command(name="helloworld", description="Hello World!")
async def cchellow(ctx):
  embed = discord.Embed(title="Post Made by: (Your username Here)", color=0xd15705)
  embed.add_field(name="Your Announcement Title", value="More Info about Announcement", inline=False)
  embed.add_field(name="----More Info----", value="Small Little Text")
  embed.set_footer(text="This is a system message!")
  await ctx.send(embed=embed)

@connectpass.command(name="builder", description="Build an announcement!")
async def ccbuilder(ctx, announcement_title: discord.Option(str, description="Your Announcement's Title"), what_happened: discord.Option(str, description="A Small Desc of the change."), changes_indepth: discord.Option(str, description="What Happened. In depth.")):
  await ctx.respond('Starting Building Of JSON! Hold on!')
  jayson = {
    "ann_title": announcement_title,
    "ann_wh": what_happened,
    "ann_changes_depth": changes_indepth,
    "author": str(ctx.author)
  }
  await ctx.send('Compiling to file! This WILL Replace the other announcement!')
  with open('./ann/ann.json', 'w') as f:
    json.dump(jayson, f, indent=4)
    await ctx.send('Successfully Compiled into file!')
  await ctx.send('You can now preview your announcement before sending! just run /fancyannouncements preview')

@connectpass.command(name="preview", description="Preview the ann.json file!")
async def ccpreviewer(ctx):
  await ctx.respond('Interpreting File! Hold on!')
  with open('./ann/ann.json', 'r') as f:
    ff = json.load(f)
  ann_title = ff["ann_title"]
  ann_wh = ff["ann_wh"]
  ann_changes_depth = ff["ann_changes_depth"]
  ann_author = ff["author"]
  embed = discord.Embed(title=f"Post Made by: {ann_author}", color=0xd15705)
  embed.add_field(name=ann_title, value=ann_wh, inline=False)
  embed.add_field(name="What Changed.", value=ann_changes_depth, inline=False)
  embed.set_footer(text="This is a system message!")
  await ctx.send(embed=embed)

@insiders.command(name="join_or_leave", description="Make yourself an Insider!")
async def insreg(ctx):
  await ctx.respond("Welcome To Coconutbot Insiders! Report bugs, get programming sht,test commands early!, and more!")
  await ctx.send('DEBUG: Hashing Profile ID! One sec Please!')
  pid = hashmii(str(ctx.author.id))
  if os.path.exists(f'./insiders/people/{str(pid)}.insider') != True:
    await ctx.send('It Seems you are not a part of insiders yet! Adding your account to the insiders list!')
    with open(f'./insiders/people/{str(pid)}.insider', 'x') as f:
      ar = {
        "Insider_Name": str(ctx.author),
        "Insider_Rep": 0,
        "Insider_ID": str(enc(str(ctx.author.id), "ins"))
      }
      json.dump(ar, f, indent=4)
    await asyncio.sleep(5)
    await ctx.send('Welcome to insiders! You Now have access to commands in the insiders section! Thanks for contributing! btw i sent you a message telling what you can do.')
    embed = discord.Embed(title="Welcome to insiders!!!", description="Welcome! no no! Take a seat!", color=0x0152d8)
    embed.add_field(name="Your Job", value=f"Sometimes me ({Owner_name}) make bugs... Your job is if you can. report them. If you do you will get something called Insider Rep. The more you have the more C O O L you are!", inline=False)
    embed.add_field(name="Newsletter", value="By becoming an insider you also got access to Insider Newsletters! You can read them if you want to.", inline=False)
    embed.add_field(name="Insider Commands.", value="New Commands will be Insider Exclusive commands! You can test them... and once its out. You'll Get a DM saying Thanks for your contribution!")
    embed.set_footer(text="This is a confirmation that you subscribed to Coconutbot insider! You can unsubscribe by running the same command again!")
    try:
      await ctx.author.send(embed=embed)
    except:
      await ctx.send('I Cant send messages to you!')
  else:
    await ctx.send('It Seems You are a part of insiders... Unsubscribing...')
    os.remove(f"./insiders/people/{str(pid)}.insider")
    await ctx.send('Thanks for using Insiders...')
  
@insiders.command(name="insider_profile", description="Check your Insider Profile!")
async def insprof(ctx):
  
  pid = hashmii(str(ctx.author.id))
  if os.path.exists(f'./insiders/people/{str(pid)}.insider') != True:
    await ctx.respond('You are not an insider! You can become one btw by running /insider join_or_leave!')
  else:
    await ctx.respond("Gathering information!")
    with open(f'./insiders/people/{str(pid)}.insider', 'r') as f:
      ff = json.load(f)
    Rep = ff["Insider_Rep"]
    Name = ff["Insider_Name"]
    memem = random.randint(0, 8)
    meme = ["Airhorn Solutions!", "Empowering your mom!", "Does people read these?", "Cool Kid Alert!", "Amiiiiiiiiiiiiiiibo settings", "click the bugs!", "0 rep = cool", "s6x", ":nerd:"]
    embed = discord.Embed(title=f'Insider Profile of {str(ctx.author)}!', description=meme[memem], color=0x0152d8)
    embed.add_field(name=f"Insider Name: {str(Name)}", value=".",)
    embed.add_field(name=f"Reputation (REP): {str(Rep)}", value=".")
    embed.set_footer(text="This is a user triggered event!")
    await ctx.send(embed=embed)

@fun.command(name="news", description="Latest News: Everything is AWFUL")
async def news_insider(ctx):
  #if os.path.exists(f'./insiders/people/{str(ctx.author.id)}.insider') == True:
  if False == True:
    await ctx.respond('This Command is Limited to Insiders only for now! Either become an insider or Wait till this releases!')
  else:
    # Comment the Following lines to disable REP Giving!
    #with open(f'./insiders/people/{str(ctx.author.id)}.insider', 'r') as f:
    #  fff = json.load(f)
    #with open(f'./insiders/people/{str(ctx.author.id)}.insider', 'w') as f:
    #  json.dump({
    #    "Insider_Name": str(ctx.author),
    #    "Insider_Rep": fff["Insider_Rep"] + 1
    #  }, f, indent=4)
    # You can stop commenting from here
    with open(f'news.json') as f:
      ff = json.load(f)

    embed = discord.Embed(title=f'News', description="What Happened on Coconutbot recently", color=0xd15705)
    embed.add_field(name="News", value=f'{str(ff["news"])}')
    embed.set_footer(text="This is a user triggered event!")
    await ctx.respond(embed=embed)

@insiders.command(name="push")
async def push(ctx):
  await ctx.respond('This used to be a Insider Notification Push Command. Its going to be removed in 2.2 so.')
  await ctx.send('https://www.youtube.com/watch?v=-nHYpZLV_Tg')

@administrative.command(name="redeem_password", description="A password Item like system. Inspiration from Pokemon Mystery Dungeon games!")
async def passrm(ctx, passwordd: discord.Option(str, description="The Password You are trying to redeem.")):
  if os.path.exists(f'./insiders/people/{str(ctx.author.id)}.insider') != True:
    await ctx.respond('The Password System is under Development! Please Become an INSIDER To redeem commands!')
    return
  else:
    if os.path.exists(f'./keys/{str(passwordd)}.key'):
      await ctx.respond('Checking key!')
      await asyncio.sleep(5)
      with open(f'./keys/{str(passwordd)}.key', 'r') as f:
        f = json.load(f)
      keytype = f["type"]
      if keytype == "REP":
        repam = f["Rep_Amount"]
        pid = hashmii(str(ctx.author.id))
        if os.path.exists(f'./insiders/people/{str(pid)}.insider'):
          with open(f'./insiders/people/{str(pid)}.insider', 'r') as fff:
            a = json.load(fff)
          with open(f'./insiders/people/{str(pid)}.insider', 'w') as ff:
            json.dump({
              "Insider_Name": str(ctx.author),
              "Insider_Rep": a["Insider_Rep"] + int(repam),
              "Insider_ID": a["Insider_ID"]
            }, ff, indent=4)
          embed = discord.Embed(title="Password Redeemed!", description="That was a nice person!", color=0x00ff4c)
          embed.add_field(name="Rewards", value=f"You got {str(repam)} Insider REP!", inline=True)
          embed.set_footer(text="This is an insider Only command!")
          await ctx.send(embed=embed)
          os.remove(f'./keys/{str(passwordd)}.key')
        else:
          embed = discord.Embed(title="Unable to redeem password!", description="God damn!", color=0xff0000)
          embed.add_field(name="Error", value=f"This is an insider gift!", inline=True)
          embed.set_footer(text="Not again!")
          await ctx.send(embed=embed)
      if keytype == "GLN_COIN":
        can = f["GLN_Coins"]
        if os.path.exists(f'./gln/{str(ctx.author.id)}.id') != True:
          embed = discord.Embed(title="Unable to redeem password!", description="God damn!", color=0xff0000)
          embed.add_field(name="Error", value=f"This is a Gamelab Network Coin Gift. And you either have your account in cold storage. or dont have a GLN account at all!", inline=True)
          embed.set_footer(text="Not again!")
          await ctx.send(embed=embed)
        else:
          with open(f'./gln/{str(ctx.author.id)}.id') as gln:
            gln = json.load(gln)
          
          requests.post(GLNADDRESS + "/gameservice/Webservice/Gameserver/Claim", params={"gsid": gln["Auth"], "amount": int(can)})

          embed = discord.Embed(title="Password Redeemed!", description="That was a nice person!", color=0x00ff4c)
          embed.add_field(name="Rewards", value=f"You got {str(can)} Gamelab Network Coins!", inline=True)
          embed.set_footer(text="This is an insider Only command!")
          await ctx.send(embed=embed)
          os.remove(f'./keys/{str(passwordd)}.key')
    else:
      await ctx.respond('Checking key!')
      await asyncio.sleep(5)
      embed = discord.Embed(title="Unable to redeem password!", description="God damn!", color=0xff0000)
      embed.add_field(name="Error", value=f"This Isn't A Valid Gift password! Did you Misspell it? Try Copy and pasting it. Or contact {Owner_name}", inline=True)
      embed.set_footer(text="Not again!")
      await ctx.send(embed=embed)

@administrative.command(name="enctest")
async def enctest(ctx, text : discord.Option(str)):
  
  await ctx.respond(f'Your Normal Message: {text}')
  msgenc = enc(text)
  await ctx.send(f'Encrypted Message: {msgenc}')

@administrative.command(name="dectest")
async def dectest(ctx, enctext : discord.Option(str)):
  key = getdeckey()
  enctext = enctext.encode()
  await ctx.respond(f'Encrypted Message: {enctext}')
  msgdec = dec(enctext)
  await ctx.send(f'Decrypted Message: {msgdec}')

@administrative.command(name="hashtest")
async def hashtest(ctx, hashd: discord.Option(str)):
  await ctx.respond(hashmii(hashd))

@eco.command(name="ohio", description="(DANGEROUS) Adventure Ohio! (Die=Savegame Reset)")
async def ohio(ctx):
  await ctx.respond('Fetching Scenarios. if there are a lot the bot may fail to respond!')
  scen = []
  scencount = 0
  for x in os.listdir('./ohio/scenarios'):
    
    scencount = scencount + 1
    scen.append(x)
    
  scencount = scencount - 1
  #await ctx.send(f'Fixed Scencount: {str(scencount)}')
  new3dsxl = random.randint(0, scencount)
  theultimatechoice = scen[new3dsxl]
  with open(f'./ohio/scenarios/{str(theultimatechoice)}') as f:
    f = json.load(f)
  
  typesfuck = f["type"]
  if typesfuck == "good":
    await ctx.send(f'You met: {f["name"]}')
    await ctx.send(f'{f["description"]}')
    await ctx.send(f["png"])
  elif typesfuck == "eh":
    await ctx.send(f'You met: {f["name"]}')
    await ctx.send(f'{f["description"]}')
    await ctx.send(f["png"])
  elif typesfuck == "death":
    await ctx.send(f'You met: {f["name"]}')
    await ctx.send(f'{f["description"]}')
    await ctx.send(f["png"])

  await ctx.send('Finished Sortin!')



@administrative.command(name="test")
async def st(ctx):
  await ctx.respond("Please Enter something!")
  guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
  await ctx.send(guess.content)

@administrative.command(name="keytest")
async def keytest(ctx):
  await ctx.respond('Listening For Keys.')
  boop = ["shit"]
  waa = 1
  iterablearray = []
  for ah in boop:
    msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    
    if msg.content == "q":
      await ctx.channel.purge(limit=1)
      await ctx.send('Stopped Listening For keys!')
      
      break
    
    elif msg.content == "a":
      waa = waa + 1
      await ctx.channel.purge(limit=1)
      try:
        await ctx.send(iterablearray[waa])
      except:
        await ctx.send('out of range')
      

    elif msg.content == "d":
      waa = waa - 1
      await ctx.channel.purge(limit=1)
      try:
        await ctx.send(iterablearray[waa])
      except:
        await ctx.send('out of range')
    elif msg.content == "mk":
      something = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
      iterablearray.append(something.content)
      
    boop.append("Crap")
    
    await asyncio.sleep(0.5)
    
  return

@administrative.command(name="keytestbruh")
async def keytestbruh(ctx):
  await ctx.respond('Listening For Keys.')
  boop = ["shit"]
  waa = 1
  iterablearray = []
  tmsg = 0
  augh = await ctx.author.send("Im Editable!")
  for ah in boop:
    try:
      msg = await bot.wait_for('message', check=lambda message: message.author == ctx.author, timeout=1)
      tmsg = tmsg + 1
      mesg = msg.content
    except:
      mesg = "None"
    
    
    await augh.edit(f"Total Messages Sent: {str(tmsg)}")
    

    if mesg == "q":
      await ctx.send('Stopped Listening!')
      return
    boop.append("Crap")
    
    await asyncio.sleep(0.5)
    
  return

@administrative.command(name="words3", description="The First ASynchronous game.")
async def words3(ctx):
  await ctx.respond('nope')
  return

@vote_system.command(name="make", description="Make your own poll! (Will be reviewed by mod team)")
async def votemk(
  ctx,
  polltitle: discord.Option(str, description="This is the actual question! Make sure its pretty!"),
  poll_choice1 : discord.Option(str, description="The first choice. Something like 'I agree!' will do it"),
  poll_choice2 : discord.Option(str, description="The second choice. Something like 'I disagree' will do it"),
  poll_none : discord.Option(bool, description="If set to True the 'None' Option will appear. (Defaults to True)", default=True),
  poll_emoji1 : discord.Option(str, description="A Discord emoji for the first choice! (Defaults to Thumbsup)", default="👍"),
  poll_emoji2 : discord.Option(str, description="A Discord emoji for the second choice! (Defaults to thumbsdown)", default="👎")

):
  await ctx.respond('Checking stuff')
  lool = await ctx.send('Probing Emojis!')
  try:
    await lool.add_reaction(poll_emoji1)
  except:
    await ctx.send("poll_emoji1 is not a valid discord emoticon!\nEither you are using a custom emoji i dont have access to\nOr you entered standard text!")
    return
  try:
    await lool.add_reaction(poll_emoji2)
  except:
    await ctx.send("poll_eEmoji2 is not a valid discord emoticon!\nEither you are using a custom emoji i dont have access to\nOr you entered standard text!")
    return
  await ctx.send('Emoticons work! Nice')
  await ctx.send('Generating a Poll ID! (This will be used by admins to review and publish your poll!)')
  Poll_ID = random.randint(0, 9999999999999999999999999999999999)
  bolstring = str(poll_none)
  polltitle = Typedown.compile(polltitle)
  Poll_Structure = {
    "title": polltitle,
    "choice1": poll_choice1,
    "choice2": poll_choice2,
    "emoji1": poll_emoji1,
    "emoji2": poll_emoji2,
    "none": bolstring,
    "author": str(ctx.author),
    "author_id": str(ctx.author.id)
  }
  await ctx.send('Encrypting Important Information!')
  Poll_Structure_Encrypted = {
    "title": enc(polltitle),
    "choice1": enc(poll_choice1),
    "choice2": enc(poll_choice2),
    "emoji1": poll_emoji1,
    "emoji2": poll_emoji2,
    "none": bolstring,
    "author": enc(str(ctx.author)),
    "author_id": enc(str(ctx.author.id))
  }
  b = open(f'./poll_submissions/{str(Poll_ID)}.p', 'x')
  b.write('{}')
  b.close()
  del b
  with open(f'./poll_submissions/{str(Poll_ID)}.p', "w") as f:
    json.dump(Poll_Structure_Encrypted, f, indent=4)
  
  
  Creator = str(ctx.author)
  Question = polltitle
  
  embed=discord.Embed(title="A Wild poll has appeared!", color=0x520303)
  embed.set_author(name="Coconutbot Polls")
  embed.add_field(name=f"Creator: {Creator}!", value=f"{Question}", inline=True)
  if poll_none == False:
    embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}", inline=False)
  else:
    embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}, |🚫| - None", inline=False)
  embed.set_footer(text="These polls are reviewed by a moderation team before they are out.")

  if ctx.author.id != 0:
    
    ReviewChannel = bot.get_channel(ReviewChanneld)
    await ReviewChannel.send(f'Submission ID: {str(Poll_ID)}')
    await ReviewChannel.send(embed=embed)
  else:
    await ctx.send(f'Hey {Owner_name}! Would you like to bypass queue? Respond with: Sure m8')
    guess = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if guess.content == "Sure m8":
      pollcnl = bot.get_channel(PollChanneld)
      bah = await pollcnl.send(embed=embed)
      await bah.add_reaction(poll_emoji1)
      await bah.add_reaction(poll_emoji2)
      if poll_none != False:
        await bah.add_reaction('🚫')
      os.remove(f"./poll_submissions/{str(Poll_ID)}.p")
    else:
      ReviewChannel = bot.get_channel(ReviewChanneld)
      await ReviewChannel.send(f'Submission ID: {str(Poll_ID)}')
      await ReviewChannel.send(embed=embed)



@review.command(name="approve", description="Approve a poll! you'll need a submission id!")
async def voteaprove(
  ctx,
  submission_id : discord.Option(str, description="You know where to find these!")
):
  submission_id = int(submission_id)
  if ctx.author.id in Administrators:
    await ctx.respond('Submission Approved!')
    await ctx.send('https://tenor.com/view/memes-approved-gif-18220485')
    with open(f"./poll_submissions/{str(submission_id)}.p") as f:
      f = json.load(f)
    author_id = int(dec(f["author_id"]))
    op = bot.get_user(author_id)
    try:
      await op.send('Hey! Your Poll Submission has been Approved!')
      await op.send('https://tenor.com/view/memes-approved-gif-18220485')
    except:
      pass
    pollchnl = bot.get_channel(PollChanneld)
    Creator = str(dec(f["author"]))
    Question = str(dec(f["title"]))
    poll_none = str(f["none"])
    poll_emoji1 = f["emoji1"]
    poll_emoji2 = f["emoji2"]
    poll_choice1 = str(dec(f["choice1"]))
    poll_choice2 = str(dec(f["choice2"]))
    
    os.remove(f"./poll_submissions/{str(submission_id)}.p")
    embed=discord.Embed(title="A Wild poll has appeared!", color=0x520303)
    embed.set_author(name="Coconutbot Polls")
    embed.add_field(name=f"Creator: {Creator}!", value=f"{Question}", inline=True)
    if poll_none == "False":
      embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}", inline=False)
    else:
      embed.add_field(name="Options:", value=f"|{poll_emoji1}| - {poll_choice1}, |{poll_emoji2}| - {poll_choice2}, |🚫| - None", inline=False)
    embed.set_footer(text="These polls are reviewed by a moderation team before they are out.")
    ohnoes = await pollchnl.send(embed=embed)
    await ohnoes.add_reaction(poll_emoji1)
    await ohnoes.add_reaction(poll_emoji2)
    if poll_none != "False":
      await ohnoes.add_reaction("🚫")

  else:
    await ctx.respond("You are not an administrator!")

@review.command(name="disapprove", description="Disapprove a poll!")
async def votedisaprove(
  ctx,
  submission_id : discord.Option(str, description="You know where to get this from")
):
  submission_id = int(submission_id)
  if ctx.author.id in Administrators:
    await ctx.respond("Submission Disapproved!")
    await ctx.send("https://tenor.com/view/knuckles-meme-meme-approved-sonic-stamp-gif-17417455")
    with open(f"./poll_submissions/{str(submission_id)}.p") as f:
      f = json.load(f)
    author_id = int(dec(f["author_id"]))
    op = bot.get_user(author_id)
    await op.send("Hey! Your Poll submission didnt go through... im sorry for ya buddy.")
    await op.send("https://tenor.com/view/knuckles-meme-meme-approved-sonic-stamp-gif-17417455")
    os.remove(f"./poll_submissions/{str(submission_id)}.p")
  else:
    bruh = await ctx.respond("You are not an administrator! I mean i kind of have OCD\nYou mean O :b: CD \nhttps://ih1.redbubble.net/image.3497596780.2775/st,small,507x507-pad,600x600,f8f8f8.jpg")
    

@tasks.loop(seconds=300)
async def clrfls():
  for f in os.listdir('./adv_how_dd_we_g/'):
    os.remove(f"./adv_how_dd_we_g/{str(f)}")
  
@bot.event
async def on_application_command_error(context, exception):
    
    await context.respond(f'Unhandled Exception occured!\nWhat happened?\nCoconutbot dealt with a undocumented error. think of this as a crash.\n The Crash log. Report this to {Owner_name}! : ||{str(exception)}||')
    



bot.add_application_command(bulletinboard) # You might wanna remove this, if you don't want people using this to bypass words.
bot.add_application_command(fun)
bot.add_application_command(howto)
#bot.add_application_command(gln) # Only use if you have a GLN Server set up... else... its not worth uncommenting this.
bot.add_application_command(settings)
bot.add_application_command(hints)
# bot.add_application_command(connectpass) # Just write announcements by hand. better imo.
# bot.add_application_command(insiders) # Doesn't work...
# bot.add_application_command(password) # Also unfinished.
# bot.add_application_command(eco) # Unfinished... :(
bot.add_application_command(vote_system)
# bot.add_application_command(glnidsettings) # Only use if you have a GLN Server set up... else... its not worth uncommenting this.
# bot.add_application_command(games) # Unfinished... Uncomment if you want to see that.
# bot.add_application_command(administrative) # You might wanna... not uncomment this. It reveals a lot of features i did while making this thang.
bot.add_application_command(christmas)

try:
  if Releasetype == "Production":
    bot.run(os.getenv('Discord_login'))
  else:
    with open('key.json', 'r') as f:
      b = json.load(f)

    key = b["login"]
    bot.run(key)
    #definerun()
except:
  print("ur bot failed leel")
  #os.system('kill 1')
  quit() # This was replaced with quit aaaas... yeah you'd have to kill 1 on replit if your bot ever reached ratelimits.