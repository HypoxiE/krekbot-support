import disnake
from disnake.ext import commands
import asyncio
import datetime
import sys

from data.secrets.TOKEN import token

class Bot(commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix="=",
			intents=disnake.Intents.all()
		)
		self.shutdown_flag = asyncio.Event()

	async def on_ready(self):
		self.krekchat = await self.fetch_guild(490445877903622144)
		print(self.krekchat.name)

		await self.change_presence(status=disnake.Status.online, activity=disnake.Game("Работаю"))
		print(f"{datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')}::  KrekSupportBot activated")

		await self.send_navigation()

		self.shutdown_flag.set()

	class embed(disnake.Embed):
		def __init__(self, **kwargs):
			color = kwargs.pop('color', 0xA687CB)
			super().__init__(color = color, **kwargs)

	async def send_navigation(self):
		navigation_channel = await self.krekchat.fetch_channel(1399856075519561839)

		embeds = [
			self.embed(
				description = """
# 🔥Анонс турнира Ruin Ship!
				"""
			),
			self.embed(
				description = """
## 📋Общая информация о турнире
- **Участвовать в турнире может каждый**, для этого достаточно просто иметь rimworld со всеми dlc кроме anomaly и запустить стрим на YouTube или Twitch с прохождением турнира!
- Участникам предстоит 30 дней выживать, убегая от роя механоидов на специальном сценарии с небольшим количеством QoL модов.

### 📅Начало турнира <t:1755248400:D>
-# Организаторы: стример Krekeros и команда discord сервера KreK4at
				"""
			),
		]

		await navigation_channel.purge(limit=len(embeds)+10)

		#await navigation_channel.send("", embeds=embeds)

		webhooks = await navigation_channel.webhooks()
		webhook = webhooks[0]
		for embed in embeds:
			if isinstance(embed, list):
				await webhook.send("", embeds=embed, username="Ruin Ship")
			else:
				await webhook.send("", embed=embed, username="Ruin Ship")

async def main():
	bot = Bot()
	try:
		bot_task = asyncio.create_task(bot.start(token))

		await bot.shutdown_flag.wait()

		if not bot.is_closed():
		    await bot.close()

		await bot_task
	except KeyboardInterrupt:
		if not bot.is_closed():
			await bot.close()
	finally:
		print("Программа завершена")

if __name__ == "__main__":
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		pass