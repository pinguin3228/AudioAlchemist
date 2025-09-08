from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
import asyncio
import os

TOKEN = "8226206985:AAGjkr1RAqVSK1quJSjWOP120iPTpvp0AGM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Отправь голосовое сообщение, я конвертирую его в MP3.")

@dp.message()
async def convert_voice(message: types.Message):
    if message.voice:
        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = file.file_path
        await bot.download_file(file_path, "voice.ogg")
        os.system("ffmpeg -i voice.ogg voice.mp3 -y")
        mp3_file = FSInputFile("voice.mp3")
        await message.answer_document(mp3_file)
        os.remove("voice.ogg")
        os.remove("voice.mp3")
    else:
        await message.answer("Пожалуйста, отправь голосовое сообщение.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
