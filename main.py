import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@client.event
async def on_ready():
    print(f'The "{client.user}" Bot is ready to use.')

###################################################### Welcome ######################################################
@client.event
async def on_member_join(member):
    channel = client.get_channel(ID_CHANNEL)
    embed = discord.Embed(
        title="👋 Welcome!",
        description=f"Hello {member.mention}, I hope you have fun on my server!",
        color=0x850dbd
    )
    embed.add_field(name="👮 Avoid Punishments", value="Read our #rules", inline=False)
    embed.set_author(name=member.name, icon_url=member.avatar.url)
    embed.set_thumbnail(url=member.avatar.url)
    embed.set_image(url="IMAGE")
    embed.set_footer(text=f"ID: {member.id}")
    await channel.send(embed=embed)

    role = discord.utils.get(member.guild.roles, id=ID_ROLE)
    if role:
        await member.add_roles(role)

###################################################### Clear ######################################################
@client.command()
async def clear(ctx, amount: int = 5):
    if ctx.author.guild_permissions.manage_messages:
        try:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{amount} messages have been deleted!', delete_after=5)
        except discord.Forbidden:
            await ctx.send("❌ I do not have permission to delete messages in this channel.")
    else:
        await ctx.send("❌ You do not have permission to use this command.")

##################################################### Commands #####################################################
@client.command()
async def list_commands(ctx):
    embed = discord.Embed(title="⚙️ List of Commands", color=discord.Color.red())
    embed.add_field(name="-> !info", value="More info about commands", inline=False)
    embed.add_field(name="-> !clear", value="Delete messages.", inline=False)
    embed.add_field(name="-> !say", value="Make the bot say something.", inline=False)
    embed.add_field(name="-> !suggest", value="Add a suggestion", inline=False)
    embed.set_footer(text="Created by: .swible")
    await ctx.send(embed=embed)

###################################################### Help ######################################################
@client.command()
async def info(ctx):
    embed = discord.Embed(title="❓ Info", color=discord.Color.blue())
    embed.add_field(name="🤗 Entries System", value="", inline=False)
    embed.add_field(name="🗑 Clear messages", value="", inline=False)
    embed.add_field(name="🎮 Commands", value="", inline=False)
    embed.add_field(name="🧻 Add Roles", value="", inline=False)
    embed.add_field(name="🔰 Suggestions", value="", inline=False)
    embed.set_footer(text="Created by: .swible")
    await ctx.send(embed=embed)

###################################################### Say ######################################################
@client.command()
async def say(ctx, *, mensagem):
    embed = discord.Embed(title=mensagem, description="Created by: .swible", color=discord.Color.purple())
    await ctx.send(embed=embed)

###################################################### Sugerir ######################################################
@client.command()
async def suggest(ctx, *, sugestao):
    await ctx.channel.purge(limit=1)
    channel = client.get_channel(ID_CHANNEL)
    embed = discord.Embed(color=0x0373fc)
    embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar.url)
    embed.add_field(name="💬 Suggestion sent:", value=sugestao)
    embed.set_footer(text="👍 - Accepted | 👎 - Disagree")
    message = await channel.send(embed=embed)
    await message.add_reaction("👍")
    await message.add_reaction("👎")


client.run('TOKEN')
