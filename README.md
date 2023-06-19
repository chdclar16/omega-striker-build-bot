Omega Strikers Bot
The Omega Strikers Bot is a Discord bot designed to provide information and builds for the game Omega Strikers. By using the command /os {striker_name}, users can retrieve build details for a specific striker.

Features
Retrieve build information for Omega Strikers.
Supports multiple strikers.
Provides build details for both forward and goalie roles.
Sends build information and associated images directly to the user's DM.
Requirements
Python 3.7 or higher
discord.py library
aiohttp library
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/omega-strikers-bot.git
Navigate to the project directory:

bash
Copy code
cd omega-strikers-bot
Create a virtual environment (optional but recommended):

Copy code
python3 -m venv .venv
Activate the virtual environment:

Windows:

Copy code
.venv\Scripts\activate
Unix / Linux:

bash
Copy code
source .venv/bin/activate
Install the required dependencies:

Copy code
pip install -r requirements.txt
Set up your Discord bot token:

Create a new application and bot on the Discord Developer Portal.

Copy the bot token.

Create a file named config.py in the project root directory.

Add the following line to config.py, replacing <YOUR_TOKEN> with your bot token:

python
Copy code
TOKEN = "<YOUR_TOKEN>"
Run the bot:

Copy code
python bot.py
Usage
Invite the bot to your Discord server using the invite link generated on the Discord Developer Portal.

In your Discord server, use the command /os {striker_name} in any channel where the bot is present.

Example: /os StrikerA

Replace {striker_name} with the name of the desired striker.
The bot will respond with the build details for the specified striker, including associated images for the forward and goalie roles.

The bot will send the build information and images directly to your DM.
