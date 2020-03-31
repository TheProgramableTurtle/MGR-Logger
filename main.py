#                     ===MGR Logger a0.1===
#                        ===main.py===
#  ======Copyright 2020 Pr0x1mas, TheProgramableTurtle======

from discord.ext import commands as cmd
# ---Setup connection to bot---
TOKEN = "Njk0NDkzMTAxMjQ2NTEzMTYy.XoMbhQ.ZLfCH7I3VGApsC99f9fco_Nek9o"


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