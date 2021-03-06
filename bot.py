import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import os
from datetime import *
import traceback

cp = '$'
bot = commands.Bot(command_prefix=cp)
bot.launch_time = datetime.utcnow()

print ('Bot is loading....')
print ('De command prefix die wordt gebruikt is ' + cp)
print ('Versie 1.3')

@bot.event
async def on_ready():
    await bot.edit_profile(username="GreyStripe")
    await bot.change_presence(game=discord.Game(name='Warrior Cats | Use {}help '.format(cp)))
    print('Bot is geladen als')
    print(bot.user.name)
    print(bot.user.id)

#Geeft de rol aan mensen die pas joinen
@bot.event
async def on_member_join(member):
	rollie8 = discord.utils.get(member.server.roles, name="New")
	await bot.add_roles(member, rollie8)
	
#Stuurt een bericht wanneer iemand de server verlaat
@bot.event
async def on_member_remove(member):
    server = member.server.get_channel(os.getenv("WELCOMECHANNEL"))
    fmt = ('{} left Warrior Cats RPG! ' .format(member))
    await bot.send_message(server, fmt.format(member, member.server))
	
#Bepaalt hoelang de bot online is
async def tutorial_uptime():
    await bot.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not bot.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
			
#de bot werkt hier als een soort chatbot
@bot.event
async def on_message(message):
    if message.content.lower().startswith('yeet'):
        await bot.send_message(message.channel, "Dabs on <@{}>".format(message.author.id))

    if message.content.lower().startswith('hi'):
        await bot.send_message(message.channel, "Hello, how are you doing <@{}>" .format(message.author.id))
		
    await bot.process_commands(message) #dit zorgt ervoor dat de andere commands nog werken
	
#wanneer iemand joint dan stuurt de bot een bericht
@bot.listen('on_member_join')
async def member_join_2(kakmens1):
    server = kakmens1.server.get_channel(os.getenv("WELCOMECHANNEL"))
    fmt = 'Welcome at {1.name}, {0.mention}, read the rules and enjoy the server!'
    await bot.send_message(server, fmt.format(kakmens1, kakmens1.server))
	
#Kick command
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
    """Kick a user"""
    await bot.kick(userName)
    embed=discord.Embed(title="Greystripe Modtools ", description=f"{userName} has been kicked \:white_check_mark: ", color=0xffff00)
    embed.set_footer(text="Powered by GreyStripe ©")
    await bot.say(embed=embed)
	
#ban command
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
    try:

        """Ban a user"""
        await bot.ban(userName)
        embed=discord.Embed(title="Greystripe Modtools ", description=f"\✅ {userName} has been banned.", color=0xffff00)
        embed.set_footer(text="Powered by GreyStripe ©")
        await bot.say(embed=embed)

    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")


@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number):
    try:
        mgs = [] #Empty list to put all the messages in the log
        number = int(number) #Converting the amount of messages to delete to an integer
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bot.delete_messages(mgs)
        await bot.say("** {} messages have been deleted:white_check_mark:**".format(number))
    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")

@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def massdelete(ctx, number):
    try:

        number = int(number) #Converting the amount of messages to delete to an integer
        counter = 0
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            if counter < number:
                await bot.delete_message(x)
                counter += 1
                await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even
    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")
			

@bot.command(name="8ball")
async def _ball():
     await bot.say(random.choice([":8ball: Without a doubt.", ":8ball: Yes definitely. ", ":8ball: Signs point to yes.", ":8ball: Outlook not so good.", ":8ball: Better not tell you now.", ":8ball: Don't count on it.", ":8ball: As I see it, Yes.", ":8ball: Never!"]))
	 
@bot.command(pass_context = True)
async def choose(ctx, choice1, choice2):
	await bot.say(random.choice([choice1, choice2]))
	
@bot.command(pass_context = True)
@commands.has_role("Staff")
async def mute(ctx, member: discord.Member, time, *, reason):
    try:
        time  = int(time)
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        channel = ctx.message.channel
        await bot.send_message(channel, "**:mute:| <@{}> You have been muted for:** {}\n**Reason:** {}\n**Admin/Mod:** <@{}>".format(member.id, time, reason, ctx.message.author.id))
        await asyncio.sleep("{}".format(time))
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")
	
@bot.command(pass_context = True)
@commands.has_role("Staff")
async def unmute(ctx, member: discord.Member):
    try:
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.remove_roles(member, role)
        await bot.say("{} is unmuted!" .format(member))
    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find:", color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    try:
        embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)
        await bot.say(embed=embed)
    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")
	
@bot.command(pass_context = True)
async def uptime(ctx):
    await bot.say("`I'm online for {0} hours and {1} minutes in the {2} Discord Server. `".format(hour, minutes, ctx.message.server))

@bot.command(pass_context = True)
async def info(ctx):
	embed=discord.Embed(title="Info about GreyStripe", description="All the information you want to know about the GreyStripe bot", color=0xffff00)
	embed.add_field(name="Creator", value="This discord bot was made by @Mohamed#7389", inline=False)
	embed.add_field(name="Programming language", value="Discord.py 0.16.12", inline=False)
	embed.add_field(name="Githubpage", value="https://github.com/Mohagames205/ThunderRPGbot", inline=False)
	embed.set_footer(text="Made by Mohamed")
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def verify(ctx):
    try:

        member = ctx.message.author
        verified_role = discord.utils.get(member.server.roles, name="Verified")
        await bot.add_roles(member, verified_role)

    except BaseException as error:
        traceback.print_exc()
        await bot.say(f"Something went wrong, please look into the logs <@239465856667615234>```py\n{error}```")

	
bot.loop.create_task(tutorial_uptime())	
bot.run(os.getenv('TOKEN'))
