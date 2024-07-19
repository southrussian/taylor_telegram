# Taylor Swift Fan Bot

## Overview
The Taylor Swift Fan Bot is a Telegram bot designed for Taylor Swift fans. It provides information about her albums, songs, lyrics, and quotes. Users can interact with the bot using various commands to get specific details or random selections related to Taylor Swift's discography.

## Features
- **/start**: Sends a welcome message.
- **/help**: Provides a list of available commands and their descriptions.
- **/albums**: Retrieves and displays a list of all Taylor Swift albums.
- **/random_album**: Provides information and cover image of a random Taylor Swift album.
- **/random_song**: Displays lyrics and details of a random Taylor Swift song.
- **/random_quote**: Shows a random quote from Taylor Swift's songs.
- **/credits**: Provides the credits for the bot.
- **Search by song name**: Users can type the name of a song to search for its details.

## Setup and Installation

### Prerequisites
- Python 3.7+
- `pip` (Python package installer)
- Telegram Bot Token (You can get one from [BotFather](https://core.telegram.org/bots#botfather))

### Installation Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/taylor-swift-fan-bot.git
    cd taylor-swift-fan-bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `config.py` file with your bot token:
    ```python
    TOKEN = 'your-telegram-bot-token'
    ```

5. Run the bot:
    ```bash
    python bot.py
    ```

## Project Structure
```
taylor/
├── run.py                # Main script to run the bot
├── config.py             # Configuration file containing the bot token
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Usage
Once the bot is running, you can interact with it on Telegram by sending the following commands:

- **/start**: Initiates a conversation with the bot and sends a welcome message.
- **/help**: Lists all available commands and their descriptions.
- **/albums**: Fetches and displays a list of all Taylor Swift albums.
- **/random_album**: Retrieves and displays a random album with its cover image.
- **/random_song**: Fetches and displays a random song with its lyrics and details.
- **/random_quote**: Retrieves and displays a random quote from Taylor Swift's songs.
- **/credits**: Shows the credits for the bot.

Additionally, you can search for a specific song by typing its name directly in the chat.

## Contributing
If you want to contribute to this project, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
- [Aiogram](https://github.com/aiogram/aiogram) for the Telegram Bot API framework.
- [Taylor Swift API](https://taylor-swift-api.vercel.app/) for providing the data on Taylor Swift's songs, albums, and quotes.

For any issues or questions, please feel free to open an issue in the repository.