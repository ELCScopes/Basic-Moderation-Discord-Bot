#At the start we import the modules
import discord #We import discord to make connection with discord API
from discord.ext import commands #We import commands from discord.ext in order to define commands


client = commands.Bot(command_prefix='!') #You can always change the ! to any prefix you want


#Moderation Commands:


@client.command() #Ban command
async def ban(ctx, member : discord.Member, *, reason=None): #Reason = None because if there is no reason given it doesn't show an error
    await member.ban(reason=reason)
    await ctx.send(f"Banned {member.mention}")

#Kick command is pretty much same as the ban command but here is the code:

@client.command() #Kick command
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention}")


#Warn command is one of the easiest moderation commands you can do!

@client.command() #Warn command
async def warn(ctx, member : discord.Member, *, reason=None):
    await member.send(f"You have been warned in {ctx.guild.name} for : {reason}")
    await ctx.send(f"Warned {member.mention} for : {reason}")


client.run('bot_token') #Replace "bot_token" with your bot's token