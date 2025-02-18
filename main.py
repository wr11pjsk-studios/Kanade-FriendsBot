import discord
from discord import app_commands
import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot("%", intents=intents)

@bot.event
async def on_ready():
    print("the bot is running lmaoooaooo")
    try:
        synced = await bot.tree.sync()
        print(f"i synced about {len(synced)} slash commands bro")
    except Exception as e:
       print(e) 

@bot.tree.command(name="hi")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} is a FEMBOY (stupid ahh slash commands)", ephemeral=False)

@bot.tree.command(name="embed create", category="Embedding")
async def create_embed(interaction: discord.Interaction, title: str, text: str):
    embed = discord.Embed(description=text)
    embed.set_author(name=title)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="embed create url", category="Embedding")
async def create_embed_url(interaction: discord.Interaction, title: str, text: str, link: str):
    embed = discord.Embed(description=text)
    embed.set_author(name=title)
    embed.set_image(url=link)
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="mute", category="Moderation")
async def shush(interaction: discord.Interaction, member: discord.Member, until: int, reason: str):
    try:
        await member.timeout(datetime.timedelta(seconds=until), reason=reason)
        await interaction.response.send_message(f"Successfully timed out user for {until} seconds.")
    except Exception:
        await interaction.response.send_message("no you dumbass, you either failed the command or they're a mod.")

@bot.tree.command(name="ban", category="Moderation")
async def tempban(interaction: discord.Interaction, member: discord.Member, until: int, reason: str):
    try:
        await member.ban()
        await interaction.response.send_message("{member} was banned for : {reason}.")
    except Exception:
        await interaction.response.send_message("no.")


@bot.tree.command(name="bonk", category="Fun")
async def bonk(interaction: discord.Interaction, bonked_member: discord.Member):
    try:
        bonk_embed = discord.Embed(description="akumarin is a straight guy")
        if bonked_member.nick:
            bonked_name = bonked_member.nick
        else:
            bonked_name = bonked_member.name

        if interaction.user.nickname:
            ctx_name = interaction.user.display_name
        else:
            ctx_name = interaction.user.name
        bonk_embed.set_author(name=f'{ctx_name} has bonked {bonked_name}')
        image_url="https://c.tenor.com/yaEqa7kN91MAAAAd/tenor.gif"
        bonk_embed.set_image(url=image_url)
        await interaction.response.send_message(embed=bonk_embed)
    except Exception:
        await interaction.response.send_message("bro i couldn't bonk that guy, you're corny asf")

@bot.tree.command(name="cook for",category="Fun")
async def cookfor(interaction: discord.Interaction, cooked_member: discord.Member):
    try:
        cook_embed = discord.Embed(description="damn taht's delicious")
        if cooked_member.nick:
            cooked_name = cooked_member.nick
        else:
            cooked_name = cooked_member.name

        if interaction.user.nickname:
            ctx_name = interaction.user.display_name
        else:
            ctx_name = interaction.user.name
        cook_embed.set_author(name=f'{ctx_name} is cooking for {cooked_name}')
        image_url="https://c.tenor.com/IGaUQ3yRuNAAAAAd/tenor.gif"
        cook_embed.set_image(url=image_url)
        await interaction.response.send_message(embed=cook_embed)
    except Exception:
        await interaction.response.send_message("I'm not your microwave bro 💀")


bot.run('Token.')
