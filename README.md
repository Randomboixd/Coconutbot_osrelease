# Coconutbot_osrelease (Open source release)

Around one year ago, i started making this bot for a discord server. After around 5 months of its lifespan i shut it down... and for rightful reasons...


### **THE CODE IS AWFUL!**


![house explosion gif. i hope it shows up]([https://tenor.com/bt0Bu.gif](https://media.tenor.com/eEs1jRy5UXgAAAAC/house-explosion.gif)


Soo this repository contains all the information to spin up a Coconutbot V2.4 instance (but why?)...

So let's get a few things off the hook before i'll explain stuff.

If you ever read the code for [gamelab](https://github.com/Randomboixd/gamelab) you can see, the code is almost as awful as that... Sooo **DO NOT EVEN THINK OF USING COCONUTBOT AS A MAIN BOT!**... well not without some patching atleast aka REWRITING THE WHOLE THING.

# Modifications from the original code

I removed some Discord IDs and stuff... For the bot to work correctly, you'll need to add yours in. I'll go in detail on that on this guide or readme thingy.

You'll also need to make modifications to get some stuff workin'... i'll include them in the guide.

# Setup

Coconutbot, is full of spaghetti!

Sooooooo... let me guide you through setting up the bot.

## 1.1 Dependencies

Noow depending on your environment, you'll need to install all packages in `requirements.txt`. I can't give a guide to all distros since [i use arch btw](https://www.youtube.com/watch?v=ifaoKZfQpdA)

but on windows, you can install these packages globally using `pip install -r requirements.txt`...

Buut if you are on linux... sorry buddy, you need to create a virtualenv...

because of this... thing.

![externally managed environment](/images/managed.png)

Thanks PEP668. very cool.

Im not gonna go over on how to create a virtualenv, so look that up...

Just install the stuff in requirements.txt and you're off to go!

## 1.2 Installing the base.

Grab the .py and put it into a folder, now let's create a few environment variables!

Note to create encryption keys, make sure you use the cryptography module.

here is how you can create one:
 ```py
from cryptography.fernet import Fernet

key = Fernet.generate_key().decode()
print(key)
```

Define these:

- `Encryption_Key` : encryption key as defined above
- `Insider_Encryption_Key` : another one for this.
- `Bulletin_Encryption_Key` : last one!
- `Discord_login` : a discord bot token.

and in `main.py` find variables "ReviewChanneld", "PollChanneld" ,"Owner_name" and "Administrators" and set em' to their correct values... i helped ya out with a comment :D


### Congrats! now the bot will start up... buut you won't do much with it yet...

## 1.3 Making directories and stuff

### Sprite images (Basically just... memes)

Create the directory `sprite_config` in the root of the bot and create a file in it called `nerd.json`... Add this inside it:

```json
{"max": 0}
```

Now create another directories in the root of the bot called `sprite_images`

That's it!

### Advancement progress

Create the following directory in the root of the bot: `adv_how_dd_we_g`.

### Settings

Create this directories in the root of the bot `ignore`.

### GLN

Currently, gln isnt ready to be open sourced... However you can prepare for it by creating the following directories: `gln` `gln_cold_storage`

# and you should be done!

... but why?
