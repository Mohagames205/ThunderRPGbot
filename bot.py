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

    if author_level == 0 and author_xp >= 10:
        set_level(user_id, 1)
        await bot.send_message(message.channel, "You leveled up to 1")

    if author_level == 1 and author_xp >= 100:
        set_level(user_id, 2)
        await bot.send_message(message.channel, "You leveled up to level 2")
		
    if author_level == 2 and author_xp >= 200:
        set_level(user_id, 3)
        await bot.send_message(message.channel, "You leveled up to level 3")
    if author_level == 3 and author_xp >= 300:
        set_level(user_id, 4)
        await bot.send_message(message.channel, "You leveled up to level 4")
	if author_level == 4 and author_xp >= 400:
        set_level(user_id, 5)
        await bot.send_message(message.channel, "You leveled up to level 5")
	if author_level == 5 and author_xp >= 500:
        set_level(user_id, 6)
        await bot.send_message(message.channel, "You leveled up to level 6")
	if author_level == 6 and author_xp >= 600:
        set_level(user_id, 7)
        await bot.send_message(message.channel, "You leveled up to level 7")
	if author_level == 7 and author_xp >= 700:
        set_level(user_id, 8)
        await bot.send_message(message.channel, "You leveled up to level 8")
	if author_level == 8 and author_xp >= 850:
        set_level(user_id, 9)
        await bot.send_message(message.channel, "You leveled up to level 9")
	if author_level == 9 and author_xp >= 1000:
        set_level(user_id, 10)
        await bot.send_message(message.channel, "You leveled up to level 10")
	if author_level == 10 and author_xp >= 1150:
        set_level(user_id, 11)
        await bot.send_message(message.channel, "You leveled up to level 11")
	if author_level == 11 and author_xp >= 1300:
        set_level(user_id, 12)
        await bot.send_message(message.channel, "You leveled up to level 12")
	if author_level == 12 and author_xp >= 1500:
        set_level(user_id, 13)
        await bot.send_message(message.channel, "You leveled up to level 13")
	if author_level == 13 and author_xp >= 1800:
        set_level(user_id, 14)
        await bot.send_message(message.channel, "You leveled up to level 14")
	if author_level == 14 and author_xp >= 1900:
        set_level(user_id, 15)
        await bot.send_message(message.channel, "You leveled up to level 15")
	if author_level == 15 and author_xp >= 2500:
        set_level(user_id, 16)
        await bot.send_message(message.channel, "You leveled up to level 16")
	if author_level == 17 and author_xp >= 3000:
        set_level(user_id, 18)
        await bot.send_message(message.channel, "You leveled up to level 17")
	if author_level == 18 and author_xp >= 3600:
        set_level(user_id, 19)
        await bot.send_message(message.channel, "You leveled up to level 18")
	if author_level == 19 and author_xp >= 4000:
        set_level(user_id, 20)
        await bot.send_message(message.channel, "You leveled up to level 19")
        #lvl_role = None
        #for role in message.server.roles:
            #if role.name == "level 4":
                #lvl_role = role

        await bot.add_roles(message.author, lvl_role)

    if message.content.lower().startswith('.xp'):
        await bot.send_message(message.channel, "You have `{}` points!".format(get_xp(message.author.id)))

    if message.content.lower().startswith('.lvl'):
        level = get_level(user_id)
        await bot.send_message(message.channel, "You leveled up to level: {}".format(level))

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

	
bot.run('NDYwNzc4MzUyODgyNDgzMjAx.DhJtfg.Fhwjv5j7EL-qYd_LC9Tb7w59jck')
