"""
Here i will make write the logics of when user will /start this bot privately it will shows some information to him.

"""

from telegram import Update
from telegram.ext import ContextTypes


from my_modules import message_template


async def start_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    When /start will come in private this will executes for normal users
    """
    msg = update.effective_message
    user = update.effective_user
    if user is None or msg is None:
        return None

    text = message_template.welcome_message_on_start(user_obj=user)

    await msg.reply_html(text=text)
