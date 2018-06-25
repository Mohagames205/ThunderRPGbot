import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import os
from datetime import *
import os.path

cp = '&'
bot = commands.Bot(command_prefix=cp)
bot.launch_time = datetime.utcnow()
gamble_msg_stuff = {}

print ('Bot is aan het laden...')
print ('De command prefix die wordt gebruikt is ' + cp)
print ('Versie 1.3')

@bot.event
async def on_ready():
    await bot.edit_profile(username="GreyStripe")
    await bot.change_presence(game=discord.Game(name="BETA | Level system".format(cp)))
    print('Bot is geladen als')
    print(bot.user.name)
    print(bot.user.id)
	


@bot.event
async def on_message(message):
    user_id = message.author.id

    author_level = get_level(user_id)
    author_xp = get_xp(user_id)
	
	
	iets = (author.level)*300
	
	if author_xp >= iets:
		set_level(user_id, (author_level)+1)
		await bot.send_message(message.channel, "You leveled up to level {}" .format(author_level))
		
        #lvl_role = None
        #for role in message.server.roles:
            #if role.name == "level 4":
                #lvl_role = role

        await bot.add_roles(message.author, lvl_role)

    if message.content.lower().startswith('.xp'):
        await bot.send_message(message.channel, "You have `{}` points!".format(get_xp(message.author.id)))

    if message.content.lower().startswith('.lvl'):
        level = get_level(user_id)
        await bot.send_message(message.channel, "You are level: {}".format(level))

    user_add_xp(message.author.id, 2)


def user_add_xp(user_id: int, xp: int):
    if os.path.isfile("users.json"):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id]['xp'] += xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
        except KeyError:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            users[user_id] = {}
            users[user_id]['xp'] = xp
            with open('users.json', 'w') as fp:
                json.dump(users, fp, sort_keys=True, indent=4)
    else:
        users = {user_id: {}}
        users[user_id]['xp'] = xp
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_xp(user_id: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        return users[user_id]['xp']
    else:
        return 0


def set_level(user_id: int, level: int):
    if os.path.isfile('users.json'):
        with open('users.json', 'r') as fp:
            users = json.load(fp)
        users[user_id]["level"] = level
        with open('users.json', 'w') as fp:
            json.dump(users, fp, sort_keys=True, indent=4)


def get_level(user_id: int):
    if os.path.isfile('users.json'):
        try:
            with open('users.json', 'r') as fp:
                users = json.load(fp)
            return users[user_id]['level']
        except KeyError:
            return 0

	
bot.run('hidden')
