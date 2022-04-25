import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_connect():
  print("机器人已上线！")

@bot.command()
async def F(ctx,*,arg):
  if(ctx.author.voice):
    channel = ctx.author.voice.channel
    name = channel.name
    Invite = await channel.create_invite(max_age=3600)
    embed = discord.Embed()
    link = "["+name+"]("+str(Invite)+")"
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.title = arg
    embed.description = "点击加入⇨"+link
    embed.color = discord.Color.green()
    embed.set_footer(text="指令介绍 │ 比如!F Flex铂金4q1 ", icon_url="https://cdn.discordapp.com/attachments/903080100256428102/925036986031570944/logo_Lobby_Gold.png")
    
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed()
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.description = "请加入语音频道后再使用该指令！"
    embed.color = discord.Color.red()
    embed.set_footer(text="指令介绍 │ 比如!F Flex铂金4q1", 
    icon_url="https://cdn.discordapp.com/attachments/903080100256428102/925036986031570944/logo_Lobby_Gold.png")
    await ctx.send(embed=embed)

@bot.command()
async def f(ctx,*,arg):
  if(ctx.author.voice):
    channel = ctx.author.voice.channel
    name = channel.name
    Invite = await channel.create_invite(max_age=3600)
    embed = discord.Embed()
    link = "["+name+"]("+str(Invite)+")"
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.title = arg
    embed.description = "点击加入⇨"+link
    embed.color = discord.Color.green()
    embed.set_footer(text="指令介绍 │ 比如!F Flex铂金4q1 ", icon_url="https://cdn.discordapp.com/attachments/903080100256428102/925036986031570944/logo_Lobby_Gold.png")
    
    await ctx.send(embed=embed)
  else:
    embed = discord.Embed()
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.description = "请加入语音频道后再使用该指令！"
    embed.color = discord.Color.red()
    embed.set_footer(text="指令介绍 │ 比如!F Flex铂金4q1", 
    icon_url="https://cdn.discordapp.com/attachments/903080100256428102/925036986031570944/logo_Lobby_Gold.png")
    await ctx.send(embed=embed)

bot.run('OTI0MzI3MzMwMjAwMDU5OTY1.Ycc86A.fH9SIOUDa7G3s8FABLvEjmx-hgY')
