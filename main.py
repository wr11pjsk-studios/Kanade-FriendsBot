import discord
import datetime

intents = discord.Intents.default()
intents.message_content = True  # Only needed if you want to read normal messages

bot = discord.Bot(intents=intents)

# ========== EMBEDDING COMMANDS ==========

@bot.slash_command(name="create_embed", description="Creates an embed with a title and text.")
async def create_embed(ctx: discord.ApplicationContext, title: str, text: str):
    embed = discord.Embed(description=text)
    embed.set_author(name=title)
    await ctx.respond(embed=embed)

@bot.slash_command(name="create_embed_url", description="Creates an embed with a title, text, and an image URL.")
async def create_embed_url(ctx: discord.ApplicationContext, title: str, text: str, link: str):
    embed = discord.Embed(description=text)
    embed.set_author(name=title)
    embed.set_image(url=link)
    await ctx.respond(embed=embed)

# ========== MODERATION COMMANDS ==========

@bot.slash_command(name="shush", description="Mutes the user and makes them shut the fuck up.")
async def shush(ctx: discord.ApplicationContext, member: discord.Member, until: int, reason: str):
    try:
        await member.timeout(datetime.timedelta(seconds=until), reason=reason)
        await ctx.respond(f"Successfully timed out {member.mention} for {until} seconds.")
    except Exception:
        if member.id == 787685020953083905:
            await ctx.respond("just because you created me doesn't mean you're omnipotent when I'm on a server, dumbass")
        else:
            await ctx.respond(f"no {member.mention}, you either failed the command or they're a mod.")

@bot.slash_command(name="tempban", description="Bans the user for a given amount of time.")
async def tempban(ctx: discord.ApplicationContext, member: discord.Member, until: int, reason: str):
    try:
        await member.ban(reason=reason)
        await ctx.respond(f"{member.mention} was banned for: {reason}.")
    except Exception:
        await ctx.respond("no.")

# ========== FUN COMMANDS ==========

@bot.slash_command(name="bonk", description="Bonks the pinged user.")
async def bonk(ctx: discord.ApplicationContext, bonked_member: discord.Member):
    try:
        bonked_name = bonked_member.nick or bonked_member.name
        ctx_name = ctx.author.nick or ctx.author.name

        bonk_embed = discord.Embed(description="akumarin is a straight guy")
        bonk_embed.set_author(name=f'{ctx_name} has bonked {bonked_name}')
        image_url = "https://c.tenor.com/yaEqa7kN91MAAAAd/tenor.gif"
        bonk_embed.set_image(url=image_url)

        await ctx.respond(embed=bonk_embed)
    except Exception:
        await ctx.respond("bro i couldn't bonk that guy, you're corny asf")

@bot.slash_command(name="cookfor", description="Cooks something for the pinged user.")
async def cookfor(ctx: discord.ApplicationContext, cooked_member: discord.Member):
    try:
        cooked_name = cooked_member.nick or cooked_member.name
        ctx_name = ctx.author.nick or ctx.author.name

        cook_embed = discord.Embed(description="a")
        cook_embed.set_author(name=f'{ctx_name} is cooking for {cooked_name}')
        image_url = "https://c.tenor.com/IGaUQ3yRuNAAAAAd/tenor.gif"
        cook_embed.set_image(url=image_url)

        await ctx.respond(embed=cook_embed)
    except Exception:
        await ctx.respond("I'm not your microwave bro 💀")

# ========== RUN THE BOT ==========

bot.run("token")
