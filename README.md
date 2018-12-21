# the-invisible-bot

A collaberative Discord bot project for The Invisible College, written in Python! Using:

* Docker Engine - Community 18.09.0
* Dockerfile link from https://github.com/Gorialis/discord.py-docker
* Discord.py:rewrite from https://github.com/Rapptz/discord.py
* Python 3.7.1 (Alpine)
* Redis 5.0.3 (Alpine)

## Setting up a bot
* Clone the repo and rename config.json.example to config.json
* Go to: https://discordapp.com/developers/applications/ and create a new application
* Navigate to the "Bot" tab and click "Add Bot"
* Copy the bot token and add it to your config.json
* Navigate back to the "General Information" tab and copy your client ID
* Create an invite link using this page: https://discordapi.com/permissions.html
* Click the link you've created after setting desired permissions and add your bot to your server
* Install Docker then simply run with: docker-compose up