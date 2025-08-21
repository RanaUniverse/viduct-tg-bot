"""
This is just demo for /settings
"""

from telegram import Update

from telegram.ext import ContextTypes

from my_modules import message_template


async def settings_cmd_private(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """
    When /help will come in private this will executes for normal users
    """
    msg = update.effective_message
    user = update.effective_user
    if user is None or msg is None:
        return None

    text = message_template.settings_cmd_msg(user_obj=user)

    await msg.reply_html(text=text)
