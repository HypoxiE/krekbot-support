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
			super().__init__(
				color = 0x944509,
				**kwargs
			)

	async def send_navigation(self):
		navigation_channel = await self.krekchat.fetch_channel(1398723447399387247)
		embeds = []

		embeds.append(
			self.embed(
				title = "Краткое изложение",
				description = """
					❓Если вам нужна помощь по игре: <#649314697425846272>
					🛠️Все сборки <@337903497401991191>: <#508324056114659330>
					📨Если вам есть, что предложить для новых сборок: <#1120010260392980614>
				"""
			)
		)

		await navigation_channel.purge(limit=1)

		webhooks = await navigation_channel.webhooks()
		webhook = webhooks[0]
		await webhook.send("", embeds=embeds, username="Навигатор")

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