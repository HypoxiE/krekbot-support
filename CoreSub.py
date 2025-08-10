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
# 🔥Добро пожаловать на турнир Ruin Ship!
				"""
			),
			self.embed(
				description = """
## 📋Общая информация о турнире Ruin ~~Our~~ Ship
**Полную информацию о турнире, гайды и правила можно посмотреть на [этом сайте 🔗](https://hypoxie.github.io/krekbot-ruinship-tournament-information-file/)**
Участникам предстоит 30 дней выживать, убегая от роя механоидов на заранее подготовленном сценарии.

<a:KrekTurtleSpin:1246089365483163702> Ваш актив побуждает нас и дальше проводить такие уникальные события, так что надеемся на ваши положительные отзывы и поддержку! И помните, главное не результат, а попытка спасти свой корабль!

-# Организаторы: стример Krekeros и команда discord сервера KreK4at
				"""
			),
			self.embed(
				description = """
## <a:NERDGE:1246089390611107986> Особенности турнира
- Уже второй глобальный турнир по RimWorld от нашей команды!
- Призовой фонд 50 000 рублей (на первые 3 призовых места)
- Уникальный сценарий для быстрых путешествий!
- Сборка QoL модов, которые помогут вам в прохождении!
- Специально разработанная система оценивания участников
- Опыт путешествия без использования караванов (только капсулами, шаттлами и гравикораблём)
				"""
			),
			self.embed(
				description = """
## <:A_pepe_write:875461953819127869> Условия участия в турнире
Перед началом убедитесь, что:
- У вас стоит актуальная версия игры 1.6
- Имеются 4 дополнения: Royality, Ideology, Biotech и Odyssey (все кроме Anomaly)
- Установлена турнирная сборка и выставлен наш порядок модов
- Вы ознакомлены и согласны с правилами проведения турнира

Ваш старт:
- Сценарий - 'Турнир RuinShip'
- Рассказчик: `Кассандра Классическая`
- Сложность: `Проигрывать - Весело`
- Установлен `Ответственный режим`
- Ксенотип: `любой ванильный кроме гемофага`
- Идеология: `любая устоявшаяся`
- Размер карты `30%`
**Все остальные параметры генерации(в том числе сид) не трогать!**
				"""
			),
			self.embed(
				description = """
## <:A_u_thonk:493332460923518996> Как участвовать?
- Весь процесс прохождения должен проходить в прямом эфире на [Twitch](https://www.twitch.tv/) или [YouTube](https://www.youtube.com/) (а лучше и там, и там) с тегами #RuinShip #RuinShip_Tournament
- Можете пригласить всех желающих на свой стрим в канале <#1399878029324324874>
- В конце и начале следующего стрима (если проходите в несколько подходов) нужно целиком показать базу, гравикорабль и статистику колонии
- После окончания турнира достаточно только заполнить [форму](https://forms.gle/CNbLLf1JF3rd5iL47)
- Свой результат вы сможете увидеть в [общей таблице участников](https://docs.google.com/spreadsheets/d/1QkaNYezumeb-QJHSZ3x1vIi5ktf0ooDklYkrP6xSMZc/edit?usp=sharing), а если вы попали в топ-20, то сможете увидеть свой результат в <#1396785366882582538>
				"""
			),
			self.embed(
				description = """
## 📆Крайние сроки подачи заявок
Заявки на участие в турнире принимаются до `31 августа 2025 г`. После окончания приёма заявок в течение суток мы перепроверим победителей и озвучим результат турнира.

-# Просьба отправлять заявки заранее, чтобы у нас было время пересчитать баллы у тех, кто ошибся в подсчете.
				"""
			),
			self.embed(
				description = """
## [🗃️ Нужные файлы 🔗](https://drive.google.com/drive/folders/1Cj3r3xmrhbSOarYRJnZ1-Cl9CGJHXKp_)
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
			self.embed(
				description = """
## <:A_anime_u_cut:910548853802029076> Пожелания напоследок
Удачи в вашем прохождении и помните, что самое главное - это путь (даже если без караванов), так что попробуйте не заруинить свой корабль и победить мехрой за эти 30 дней и у вас обязательно всё получится!(или нет<a:AnimatedA_PeepoNoob:982560159974965308>) Мы верим в вас и в вашу победную! Точно так же, как стример верит в свою!<a:AnimatedA_ThisIsFine:982563794133852220>
				"""
			),
			self.embed(
				description = """
## P.S.
По любым вопросам можете обращаться к людям с ролью <@&1241274685459529789>, а можете просто пингануть эту роль в канале <#508324056114659330>.
				"""
			),
		]

		if False:
			test_channel = await self.krekchat.fetch_channel(1382446742087270562)
			for embed in embeds:
				if isinstance(embed, list):
					await test_channel.send("", embeds=embed)
				else:
					await test_channel.send("", embed=embed)
			#return

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