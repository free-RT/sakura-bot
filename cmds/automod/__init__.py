from os import listdir
import logging


async def setup(bot):
    for name in listdir("cmds/automod"):
        if not name.startswith(("_", ".")):
            try:
                await bot.load_extension("cmds.automod."+name.replace(".py", ""))
            except:
                logging.exception("Error on automod.%s", name)
            else:
                print("[Log][load]" + name)
