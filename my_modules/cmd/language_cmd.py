"""
Language Related Code will be present here.
"""

from telegram import Update, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from my_modules.translation_message import get_value_from_language_json
from my_modules.language import get_user_preferred_language_code

from my_modules.inline_keyboard_button import SET_LANGUAGE_KEYBOARD


async def language_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This will allow the user to set his own prefer language.
    This will trigger on private user send /language to bot
    """
    msg = update.effective_message
    user = update.effective_user

    if not user or msg is None:
        return None

    user_prefer_lang_code: str = get_user_preferred_language_code(user_obj=user)

    lang_change_text = get_value_from_language_json(
        language_code=user_prefer_lang_code,
        key_name="language_cmd",
    )

    if not lang_change_text:
        await msg.reply_html("Error Here")
        return None

    await context.bot.send_message(
        chat_id=user.id,
        text=lang_change_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(SET_LANGUAGE_KEYBOARD),
    )
