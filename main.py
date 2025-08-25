from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from my_modules import bot_config_settings

from my_modules.cmd import start_cmd, help_cmd, settings_cmd, language_cmd


# The logger module below is the need to print the errors & warnings in the console so i import the whole module so that i not need to worry about what will happens in login module.
from my_modules import logger_related  # type: ignore

BOT_TOKEN = bot_config_settings.BOT_TOKEN


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    if update.message is None or update.message.text is None:
        return None
    await update.message.reply_text(update.message.text)


from telegram.constants import ChatMemberStatus
from my_modules.bot_config_settings import PRIVATE_GROUP_ID


async def rana_checking(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    For testing some innere shorts thing i will do here
    """
    user = update.effective_user
    msg = update.effective_message

    if user is None or msg is None:
        print("Soemthings wrong")
        return None

    # lets check if user is in the gourp or not
    group_member_status = await context.bot.get_chat_member(
        chat_id=PRIVATE_GROUP_ID,
        user_id=user.id,
    )

    allowed_statuses = {
        ChatMemberStatus.OWNER,
        ChatMemberStatus.ADMINISTRATOR,
        ChatMemberStatus.MEMBER,
        ChatMemberStatus.RESTRICTED,
    }

    if group_member_status.status in allowed_statuses:
        text = (
            f"Hello {user.mention_html()}\n"
            "✅ You are in the group — you can use the bot."
        )
        await msg.reply_html(text=text)
    else:
        text = (
            f"🚫 You are currently '{group_member_status.status}' in Our Main group.\n"
            "You cannot use the bot until you join or are unbanned."
        )
        await msg.reply_html(text=text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(
        CommandHandler(
            command="rana",
            callback=rana_checking,
            block=False,
        )
    )
    application.add_handler(
        CommandHandler(
            command="start",
            callback=start_cmd.start_cmd_private,
            block=False,
        )
    )
    application.add_handler(
        CommandHandler(
            command="help",
            callback=help_cmd.help_cmd_private,
            block=False,
        )
    )
    application.add_handler(
        CommandHandler(
            command="settings",
            callback=settings_cmd.settings_cmd_private,
            block=False,
        )
    )
    application.add_handler(
        CommandHandler(
            command="language",
            callback=language_cmd.language_cmd,
            block=False,
        )
    )

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
