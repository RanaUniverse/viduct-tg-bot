"""
This module will work on /help related concepts.


"""

from telegram import Update
from telegram.ext import ContextTypes


from my_modules import message_template


async def help_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    When /help will come in private this will executes for normal users
    """
    msg = update.effective_message
    user = update.effective_user
    if user is None or msg is None:
        return None
    
    lang_code = user.language_code
    if not lang_code:
        lang_code = "en"
    # i make the default langauge as english when it will not in the api

    text = message_template.generate_help_msg(
        user_obj=user,
        user_language=lang_code,
    )

    await msg.reply_html(text=text)
