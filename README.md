# Telegram Bot Project

## Overview

This is a Telegram bot project implemented using the Aiogram library. The bot provides various functionalities, including downloading Instagram media and welcoming users.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Handlers](#handlers)
  - [Download Instagram Handler](#download-instagram-handler)
  - [Start Handler](#start-handler)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/newjasjanpython/new_jasjan_2_bot.git
   cd new_jasjan_2_bot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the bot token and other settings in the appropriate files.

4. Run the main script:

   ```bash
   python main.py
   ```

## Usage

- Start the bot on Telegram.
- Interact with the bot using commands and messages on Telegram.

## Project Structure

- `main.py`: Entry point for the bot script.
- `bot/`: Directory containing the bot modules.
  - `__init__.py`: Initializes the bot, dispatcher, and database connection.
  - `loader.py`: Loads necessary components like the bot, dispatcher, and database.
  - `handlers/`: Directory for bot command handlers.
    - `download_instagram_handler.py`: Handles downloading media from Instagram.
    - `start_handler.py`: Handles the start command and user welcome messages.
  - `database/`: Directory for database-related modules.
    - `__init__.py`: Imports database-related classes.
    - `configurations.py`: Configuration file for database tables.
    - Other database-related files.
- `README.md`: Project documentation (you're here).

## Handlers

### Download Instagram Handler

This handler is triggered when a message contains an Instagram URL. It fetches the post metadata using Instaloader, constructs a media group, and responds with the media and caption.

### Start Handler

This handler is triggered when a user sends the "/start" command. It welcomes the user, checks the database, and sends a welcome back or a new welcome message accordingly.

## Configuration

- `bot/loader.py`: Bot configurations such as token and admins.
- `bot/database/configurations.py`: Database table configurations.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).