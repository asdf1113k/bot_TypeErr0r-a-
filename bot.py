import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from my_secret.my_token import TOKEN


dp = Dispatcher()


@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.reply("🫠")


@dp.message()
async def echo(message: Message) -> None:
    if "хуй" in message.text.lower():
        await message.answer(":| это самое умное что ты мог написать?")
    else:
        await message.reply("...") # message.text


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        pass