from vkbottle.bot import Blueprint, Message
from loguru import logger
from vkbottle import Keyboard, Text, GroupTypes, GroupEventType, VKAPIError
bot = Blueprint()
@bot.on.raw_event(GroupEventType.LIKE_ADD, dataclass=GroupTypes.LikeAdd)
@logger.catch()
async def like_add_handler(event: GroupTypes.LikeAdd):
	user_firstname = (await event.ctx_api.users.get(user_ids=[event.object.liker_id]))[0].first_name
	#await ans(f"DEBUG {user_info}")
	#await event.ctx_api.messages.send(peer_id=event.object.liker_id, random_id=0, message=f"DEBUG {user_firstname}")
	#await ans(f'Спасибо за лайк, {}')
	await event.ctx_api.messages.send(peer_id=event.object.liker_id, random_id=0, message=f'Спасибо за лайк, {user_firstname}')
@bot.on.raw_event(GroupEventType.MESSAGE_EDIT, dataclass=GroupTypes.MessageEdit)
@logger.catch()
async def like_add_handler(event: GroupTypes.MessageEdit):
	print(event)
	user_firstname = (await event.ctx_api.users.get(user_ids=[event.object.from_id]))[0].first_name
	if 'http' in event.object.text or 'https' in event.object.text:
		await event.ctx_api.messages.send(peer_id=event.object.peer_id, random_id=0, message=f'Только что [id{event.object.from_id}|{user_firstname}] отредактировал сообщение. Его новый текст:\nНайдена ссылка')
	else:
		await event.ctx_api.messages.send(peer_id=event.object.peer_id, random_id=0, message=f'Только что [id{event.object.from_id}|{user_firstname}] отредактировал сообщение. Его новый текст:\n{event.object.text}')