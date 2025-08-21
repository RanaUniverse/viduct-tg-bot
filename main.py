from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from my_modules import bot_config_settings

from my_modules.cmd import start_cmd, help_cmd, settings_cmd


# The logger module below is the need to print the errors & warnings in the console so i import the whole module so that i not need to worry about what will happens in login module.
from my_modules import logger_related  # type: ignore

BOT_TOKEN = bot_config_settings.BOT_TOKEN


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    if update.message is None or update.message.text is None:
        return None
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start_cmd.start_cmd_private))
    application.add_handler(CommandHandler("help", help_cmd.help_cmd_private))
    application.add_handler(
        CommandHandler("settings", settings_cmd.settings_cmd_private)
    )

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
