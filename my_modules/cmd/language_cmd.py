"""
Language Related Code will be present here.
"""

from telegram import Update, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from my_modules.inline_keyboard_button import SET_LANGUAGE_KEYBOARD


async def language_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This will allow the user to set his own prefer language.
    This will trigger on private user send /language to bot
    """
    user = update.effective_user

    if not user:
        return

    reply_text = (
        f"🌐 Please select your preferred language: \n"
        "(to set as your default language.)\n"
        "👇️👇️👇️"
    )

    await context.bot.send_message(
        chat_id=user.id,
        text=reply_text,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(SET_LANGUAGE_KEYBOARD),
    )
