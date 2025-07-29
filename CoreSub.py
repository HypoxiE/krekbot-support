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
# Добро пожаловать на турнир Ruin Ship!
				"""
			),
			self.embed(
				description = """
## Общая информация о турнире
Участникам предстоит 30 дней выживать, убегая от роя механоидов на заранее подготовленном сценарии.

-# Организаторы: стример Krekeros и команда discord сервера KreK4at
				"""
			),
			self.embed(
				description = """
## Как участвовать?
- Весь процесс прохождения должен проходить в прямом эфире на [Twitch](https://www.twitch.tv/) или [YouTube](https://www.youtube.com/) (а лучше и там, и там) с тегами <обязательно добавить теги>
- Можете пригласить всех желающих на свой стрим в канале <#1399878029324324874>
- В конце и начале следующего стрима (если проходите в несколько подходов) нужно целиком показать базу, гравикорабль и статистику колонии
- После окончания турнира достаточно только заполнить [форму](https://forms.gle/CNbLLf1JF3rd5iL47)
- Свой результат вы сможете увидеть в [общей таблице участников](https://docs.google.com/spreadsheets/d/1QkaNYezumeb-QJHSZ3x1vIi5ktf0ooDklYkrP6xSMZc/edit?usp=sharing), а если вы попали в топ-20, то сможете увидеть свой результат в <#1396785366882582538>
				"""
			),
			self.embed(
				description = """
## Крайние сроки подачи заявок
Заявки на участие в турнире принимаются до <обязательно добавить timestamp>. После окончания приёма заявок в течение суток мы перепроверим победителей и озвучим результат турнира.

Заявки, отправленные в последний день до окончания турнира будут оцениваться особо строго, так что просьба отправлять заявки заранее, чтобы у нас было время пересчитать баллы у тех, кто ошибся в подсчёте.
				"""
			),
			self.embed(
				description = """
## Дополнительная информация
### Моды распаковать в папку mods в корневой папке игры!
```C:\\Program Files (x86)\\Steam\\steamapps\\common\\RimWorld\\Mods```

### Быстрее всего в папку с другими файлами можно попасть через 'Открыть сохранения' в настройках Rimworld, либо ввести в поиск на пк `%Appdata%`
**ModsConfig.xml (порядок модов) поместить по этому пути**
```%userprofile%\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Config```

**Файл RuinShipScenaruio.rsc (Сценарий турнира) поместить по этому пути**
```%userprofile%\\AppData\\LocalLow\\Ludeon Studios\\RimWorld by Ludeon Studios\\Scenarios```
				"""
			),
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