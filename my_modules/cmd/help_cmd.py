"""
This module will work on /help related concepts.


"""

from telegram import Update
from telegram.ext import ContextTypes


from my_modules import message_template

from my_modules.language import get_user_prefer_language


async def help_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    When /help will come in private this will executes for normal users
    """
    msg = update.effective_message
    user = update.effective_user
    if user is None or msg is None:
        return None

    lang_code = get_user_prefer_language(user.id)
    if not lang_code:
        await msg.reply_html(
            "You Have Not Selected Your Language so bye, "
            "select your language in /language"
        )
        return None

    text = message_template.generate_help_msg(
        user_obj=user,
        user_language=lang_code,
    )

    await msg.reply_html(text=text)
