import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()


# Command start handler
@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Hello, {message.from_user.first_name}! Here is the bot for Taylor Swift fans with lyrics, albums info and quotes')

@dp.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "Hello! This is the Taylor Swift Fan Bot. Here are the commands you can use:\n\n"
        "/start - Welcome message\n"
        "/help - Show this help message\n"
        "/albums - Get a list of all Taylor Swift albums\n"
        "/random_album - Get a random Taylor Swift album with cover image\n"
        "/random_song - Get a random Taylor Swift song with lyrics\n"
        "/random_quote - Get a random quote from Taylor Swift's songs\n"
        "/credits - View the bot credits\n\n"
        "You can also search for specific songs by sending a message with the song name."
    )
    await message.answer(str(help_text))


# Generic message handler
@dp.message(lambda message: True)
async def handle_message(message: Message):
    user_text = message.text.strip()

    if user_text.lower().startswith('/albums'):
        await get_albums(message)
    elif user_text.lower().startswith('/random_quote'):
        await get_random_quote(message)
    elif user_text.lower().startswith('/random_song'):
        await get_random_song(message)
    elif user_text.lower().startswith('/random_album'):
        await get_random_album(message)
    elif user_text.lower().startswith('/credits'):
        await get_credits(message)
    else:
        await search_songs(message, user_text)


# Function to search songs
async def search_songs(message: Message, query: str):
    url = f"https://taylor-swift-api.vercel.app/api/songs/search/?name={query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            results = []
            for song in data:
                song_info = (f"Name: {song.get('name')}\n"
                             f"Artist: {song.get('artist')}\n"
                             f"Duration: {song.get('duration')}\n"
                             f"Album: {song.get('album')}\n"
                             f"Lyrics: {song.get('lyrics')}\n")
                results.append(song_info)
            result = '\n\n'.join(results)
        else:
            result = "No songs found with that name."
    else:
        result = "Error fetching data."

    await message.answer(result)



# Handler for /albums command
@dp.message(Command("albums"))
async def get_albums(message: Message):
    response = requests.get("https://taylor-swift-api.vercel.app/api/albums")
    if response.status_code == 200:
        data = response.json()
        titles = [album["title"] for album in data]
        result = '\n'.join(titles)
    else:
        result = "Error fetching data."

    await message.answer(result)


# Handler for /random_quote command
@dp.message(Command("random_quote"))
async def get_random_quote(message: Message):
    response = requests.get("https://taylor-swift-api.vercel.app/api/quotes")
    if response.status_code == 200:
        data = response.json()
        quote = f"Song: {data.get('song')}\n\n{data.get('quote')}"
    else:
        quote = "Error fetching data."

    await message.answer(quote)


# Handler for /random_song command
@dp.message(Command("random_song"))
async def get_random_song(message: Message):
    response = requests.get("https://taylor-swift-api.vercel.app/api/songs/random")
    if response.status_code == 200:
        data = response.json()
        song = (f"Song: {data.get('name')}\n\n{data.get('lyrics')}\n\n"
                f"Duration: {data.get('duration')}\n\nAlbum: {data.get('album')}")
    else:
        song = "Error fetching data."

    await message.answer(song)


# Handler for /credits command
@dp.message(Command("credits"))
async def get_credits(message: Message):
    link = "https://t.me/south_russian"
    await message.answer(link)


@dp.message(Command("random_album"))
async def get_random_album(message: Message):
    response = requests.get("https://taylor-swift-api.vercel.app/api/albums/random")
    if response.status_code == 200:
        data = response.json()
        album_info = (f"Title: {data.get('title')}\n"
                      f"Release Date: {' '.join(map(str, data.get('releaseDate')))}")
        album_cover_url = data.get('albumCover')
    else:
        album_info = "Error fetching data."
        album_cover_url = None

    if album_cover_url:
        await bot.send_photo(chat_id=message.chat.id, photo=album_cover_url, caption=album_info)
    else:
        await message.answer(album_info)


# Main function
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
