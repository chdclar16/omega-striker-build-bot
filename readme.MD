# Omega Strikers Bot
The Omega Strikers Bot is a Discord bot designed to provide information and builds for the game Omega Strikers. By using the command `/os {striker_name}`, users can retrieve build details for a specific striker.


## Features
- Retrieve build information for Omega Strikers.
- Supports multiple strikers.
- Provides build details for both forward and goalie roles.
- Sends build information and associated images directly to the user's DM.


## Requirements(requirements.txt)
Python 3.7 or higher
discord.py library
aiohttp library


## Installation
1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/omega-strikers-bot.git
```

2. Navigate to the project directory:
```
cd omega-strikers-bot
```
3. Create a virtual environment (optional but recommended):
```
python3 -m venv .venv
```

4. Activate the virtual environment:

- Windows:
```
.venv\Scripts\activate
```

- Unix / Linux:
```
source .venv/bin/activate
```
5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Set up your Discord bot token:

- Create a new application and bot on the Discord Developer Portal.

- Copy the bot token.

- Create a file named config.py in the project root directory.

- Add the following line to config.py, replacing `<YOUR_TOKEN>` with your bot token:
```
TOKEN = "<YOUR_TOKEN>"
```
7. Run the bot:
```
python bot.py
```

## Usage
1. Invite the bot to your Discord server using the invite link generated on the Discord Developer Portal.

2. In your Discord server, use the command /os {striker_name} in any channel where the bot is present.

    - Example: /os kai

    - Replace {striker_name} with the name of the desired striker.
3. The bot will respond with the build details for the specified striker, including associated images for the forward and goalie roles.

4. The bot will send the build information and images directly to your DM.
