from vkbottle.bot import Blueprint, Message
from loguru import logger
from rextester_py import rexec_aio
bot = Blueprint()
@bot.on.message(text="eval <code>")
@logger.catch()
async def nonamecommand(message: Message, code):
	rex = await rexec_aio("python 3", code, None)
	results = rex.results
	if results == None:
		await message.answer('Че это мы тут None/ошибки устраиваем?')
		#await 
	if len(str(results)) > 30:
		if message.from_id == 549204433:
			await message.answer(f'Результат выполнения кода:\n{results}')
		else:
			await message.answer(f'Много символов для вывода({len(results)})')
	else:
		await message.answer(f'Результат выполнения кода:\n{results}')
@bot.on.message(text="Hi")
@logger.catch()
async def nonamecommand(message: Message):
	await message.answer('Hi')
@logger.catch()
'''@bot.on.message(text="message <peer_id> <message>")
async def message(message: Message, peer_id, messages):
	#await message.ctx_api.messages.send(peer_id=peer_id, message=messages, random_id=0)
	await message.ctx_api.messages.send(peer_id=peer_id, random_id=0, message=messages)
'''