import discord
from discord.ext import commands

client = discord.Client(intents=discord.Intents.all())  # instanciates as a client object
bot = commands.Bot(command_prefix=':0 ', intents=discord.Intents.all())  # uses Subclass of Client contains prefix method
# bot command set to ':0'

tokenfile = open("Token for fresco.txt", "r")
TOKEN = tokenfile.read()
GUILD = "ECLIPSE"


# shifted from Client class to Bot subclass for connection establishment check
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )


# shifted the prompt to morning for good morning
@bot.command(name='Morning', help="Sends a cute good morning message")
async def morning(ctx):
    if ctx.author == client.user:
        return
    response: str = "Good Morning! Onii-chan"
    await ctx.send(response)
    await ctx.send("https://media.tenor.com/lg67Ynq8SiMAAAAM/kanna-orange-kanna-ohayo.gif")


bot.run(TOKEN)
