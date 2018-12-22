# the-invisible-bot

### A collaborative Discord bot project for The Invisible College, written in Python! Using:
* Docker Engine - Community 18.09.0
* Dockerfile link from https://github.com/Gorialis/discord.py-docker
* Discord.py:rewrite from https://github.com/Rapptz/discord.py
* Redis.py from https://github.com/andymccurdy/redis-py
* Python 3.7.1 (Alpine)
* Redis 5.0.3 (Alpine)

### Contribution Guidelines
* Add new functionality via new cogs then add them to the extensions list in main.py. Avoid adding code to main if possible.
* Follow the Google style guide: https://github.com/google/styleguide/blob/gh-pages/pyguide.md
* As stated in the guide, run pylint on your code.
* Use YAPF with the following flags: --style='{based_on_style: chromium, indent_width: 4}'

### Setting up a bot
* Clone the repo and rename config.json.example to config.json
* Go to: https://discordapp.com/developers/applications/ and create a new application.
* Navigate to the "Bot" tab and click "Add Bot."
* Copy the bot token and add it to your config.json.
* Navigate back to the "General Information" tab and copy your client ID.
* Create an invite link using this page: https://discordapi.com/permissions.html
* Click the link you've created after setting desired permissions and add your bot to your server.
* Install Docker then simply run with: docker-compose up -d
* The container volume is linked to the path where the code resides, so you can make changes to the code without re-building the image.
* Run "docker-compose restart" to update changes.

Alternatively, one can simply run the main.py in your Python environment of choice and manually install dependencies. 

### Useful links
* https://docs.python.org/3/
* https://discordpy.readthedocs.io/en/rewrite/
* https://discordpy.readthedocs.io/en/rewrite/ext/commands/commands.html
* https://redis-py.readthedocs.io/en/latest/
* https://docs.docker.com/
* https://docs.docker.com/compose/
