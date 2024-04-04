import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import requests
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.first_name}! It is the most useless bot about Taylor Swift but '
                         f'it was created with love')


@dp.message(Command("midnights"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/10")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("1989"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/1")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("taylor_swift"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/2")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("fearless"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/3")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("speak_now"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/4")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("red"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/5")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("reputation"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/6")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("lover"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/7")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("folklore"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/8")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("evermore"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums/9")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("albums"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/albums")
    titles_string = ""
    if r.status_code == 200:
        data = r.json()
        titles = [song["title"] for song in data]
        titles_string = '\n'.join(titles)
    else:
        print("error")
    await message.answer(titles_string)


@dp.message(Command("random_lyrics"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/lyrics/" + str(random.randint(1, 177)))
    lyrics = ""
    if r.status_code == 200:
        data = r.json()
        title = data.get("song_title")
        lyrics += "Song name: " + title + '\n' + '\n'
        lyrics += data.get("lyrics")

    else:
        print("error")
    await message.answer(lyrics)


@dp.message(Command("random_song"))
async def get_help(message: Message):
    r = requests.get("https://taylor-swift-api.sarbo.workers.dev/songs/" + str(random.randint(1, 177)))
    song_title = ""
    if r.status_code == 200:
        data = r.json()
        song_title += data.get("song_title")
    else:
        print("error")
    await message.answer(song_title)


@dp.message(Command("credits"))
async def get_help(message: Message):
    link = "https://t.me/south_russian"
    await message.answer(link)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stop")
