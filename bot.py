import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import os
import datetime

cp = '&'
bot = commands.Bot(command_prefix=cp)
bot.launch_time = datetime.utcnow()

print ('Bot is aan het laden...')
print ('De command prefix die wordt gebruikt is ' + cp)
print ('Versie 1.3')

@bot.event
async def on_ready():
    await bot.edit_profile(username="GreyStripe")
    await bot.change_presence(game=discord.Game(name='Use {}help | Warrior Cats'.format(cp)))
    print('Bot is geladen als')
    print(bot.user.name)
    print(bot.user.id)
	

@bot.event
async def on_member_join(member):
	rollie8 = discord.utils.get(member.server.roles, name="New")
	await bot.add_roles(member, rollie8)
	


@bot.event
async def on_member_remove(member):
    server = member.server.get_channel("434077834684792832")
    fmt = ('{} left Warrior Cats RPG!' .format(member))
    await bot.send_message(server, fmt.format(member, member.server))
	
	
@bot.listen('on_member_join')
async def member_join_2(kakmens1):
    server = kakmens1.server.get_channel("434077834684792832")
    fmt = 'Welcome at the {1.name} Discord server, {0.mention}, read the rules and enjoy the server!'
    await bot.send_message(server, fmt.format(kakmens1, kakmens1.server))
	
	
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User, *, reason):
    """Kick a user"""
    await bot.kick(userName)
    await bot.say("*** :white_check_mark:  The user {} has been kicked***" .format(userName))
	
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User, * ,reason):
    """Ban a user"""
    await bot.ban(userName)
    await bot.say("*** :white_check_mark: The user {} had been banned***" .format(userName))


@bot.command(pass_context = True)
async def purge(ctx, number):
	mgs = [] #Empty list to put all the messages in the log
	number = int(number) #Converting the amount of messages to delete to an integer
	async for x in bot.logs_from(ctx.message.channel, limit = number):
		mgs.append(x)
	await bot.delete_messages(mgs)
	await bot.say("** {} messages have been deleted:white_check_mark:**".format(number))

@bot.command(pass_context = True)
async def massdelete(ctx, number):
    number = int(number) #Converting the amount of messages to delete to an integer
    counter = 0
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        if counter < number:
            await bot.delete_message(x)
            counter += 1
            await asyncio.sleep(1.2) #1.2 second timer so the deleting process can be even
			

@bot.command(name="8ball")
async def _ball():
     await bot.say(random.choice([":8ball: Without a doubt.", ":8ball: Yes definitely. ", ":8ball: Signs point to yes.", ":8ball: Outlook not so good.", ":8ball: Better not tell you now.", ":8ball: Don't count on it.", ":8ball: As I see it, Yes.", ":8ball: Never!"]))
	 
@bot.command(pass_context = True)
async def choose(ctx, choice1, choice2):
	await bot.say(random.choice([choice1, choice2]))
	
@bot.command(pass_context = True)
@commands.has_role("Staff")
async def mute(ctx, member: discord.Member, time, *, reason):
    time  = int(time)
    role = discord.utils.get(member.server.roles, name='Muted')
    await bot.add_roles(member, role)
    channel = ctx.message.channel
    await bot.send_message(channel, "**:mute:| <@{}> You have been muted for:** {}\n**Reason:** {}\n**Admin/Mod:** <@{}>".format(member.id, time, reason, ctx.message.author.id))
    await asyncio.sleep("{}".format(time))
    role = discord.utils.get(member.server.roles, name='Muted')
    await bot.remove_roles(member, role)
@bot.command(pass_context = True)
@commands.has_role("Staff")
async def unmute(ctx, member: discord.Member):
	role = discord.utils.get(member.server.roles, name='Muted')
	await bot.remove_roles(member, role)
	await bot.say("{} is unmuted!" .format(member))
		
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
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find:", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await bot.say(f"{days}d, {hours}h, {minutes}m, {seconds}s")
	
bot.run('hidden')