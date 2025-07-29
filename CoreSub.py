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
			color = kwargs.pop('color', 0x944509)
			super().__init__(color = color, **kwargs)

	async def send_navigation(self):
		navigation_channel = await self.krekchat.fetch_channel(1399856075519561839)

		embeds = [
			self.embed(
				description = """
Турнир: Ruin Ship


Длительность турнира 30 дней 
Конец турнира по окончанию таймера, либо по завершению концовки будут + баллы за кол-во оставшихся дней до конца (полных)


Критерии 

				"""
			)
		]

		await navigation_channel.purge(limit=len(embeds)+1)

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