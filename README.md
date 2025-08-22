
This project i make for a bot, which will talk with the api.

## How to start this bot ?

The below command need to run one after another.

```
git clone https://github.com/RanaUniverse/viduct-tg-bot
uv sync
```
Upper Two command need to run just once, and just to run the bot service, i need to see below...

```
uv run main.py
```
Upper command i need to run each time i want to start the bot



This Repo is connected with,
[Viduct-API](https://github.com/razorblade23/Viduct-API)



## Features Of This Bot 

1. /start - It will reply
2. /help - I just keep it for now
3. /settings - Just i keep it
4. /language - It will shows a keyboard to user , for now buttons not working...



## Structer of my repo
> How my code is logically separated, i will write those thigns here...



## How i start this repo.

This will start making my repo in main branch for git.
it first start this repo workable for git
```
git init . -b main
```
```
uv init .
```
```
uv add "python-telegram-bot[all]"
```
I need to run below to start this bot from fresh
```
uv sync 
uv run main.py
```