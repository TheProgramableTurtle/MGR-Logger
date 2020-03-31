#                     ===MGR Logger a0.1===
#                        ===main.py===
#          ======Copyright TheProgramableTurtle======

from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = ""


bot = cmd.Bot(command_prefix='$')

@bot.command()
async def test(ctx):
    pass

# or:

@cmd.command()
async def log(ctx):
    pass

bot.add_command(log)

bot.run(TOKEN)