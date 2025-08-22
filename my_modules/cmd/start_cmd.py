"""
Here i will make write the logics of when user will /start this bot privately it will shows some information to him.

"""

from telegram import Update
from telegram.ext import ContextTypes


from my_modules import message_template

from my_modules.language import get_user_prefer_language


async def start_cmd_private(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    When /start will come in private this will executes for normal users
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

    text = message_template.generate_welcome_message_on_start(
        user_obj=user,
        user_language=lang_code,
    )
    # I make this upper so that, the start message will come form the json

    await msg.reply_html(text=text)
