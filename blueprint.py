from vkbottle.bot import Bot
from vkbottle.api import API
from blueprints import bps
FileThisToken = open('tokens/PyReload1.txt', 'r')
bot = Bot(token=FileThisToken.read())
for bp in bps:
	bp.load(bot)
bot.run_forever()