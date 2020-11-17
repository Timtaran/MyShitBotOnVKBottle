from vkbottle.bot import Blueprint, Message
from loguru import logger
bot = Blueprint()
@bot.on.message(text="привет")
@logger.catch()
async def info(message: Message):
	#current_group = (await message.ctx_api.groups.get_by_id())[0]
	#await message.answer(f"Этот бот работает в разных группах. \nНазвание группы в которой вы сейчас находитесь: {current_group.name}")
	await message.answer(sticker_id=18463)
	#await message.ctx_api.messages.sendSticker(peer_id = message.peer_id, sticker_id=18463)