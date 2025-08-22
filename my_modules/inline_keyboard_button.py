"""
I will keep some buttons logic so that i can use this
easily in different places
"""

from telegram import InlineKeyboardButton


SET_LANGUAGE_ENGLISH = InlineKeyboardButton(
    text="🇺🇸 English",
    callback_data="set_lang_en",
)

SET_LANGUAGE_HINDI = InlineKeyboardButton(
    text="🇮🇳 Hindi (हिन्दी)",
    callback_data="set_lang_hi",
)

SET_LANGUAGE_CROATIAN = InlineKeyboardButton(
    text="🇭🇷 Croatian (Hrvatski)",
    callback_data="set_lang_hr",
)

SET_LANGUAGE_BENGALI = InlineKeyboardButton(
    text="🇧🇩 Bengali (বাংলা)",
    callback_data="set_lang_bn",
)


SET_LANGUAGE_KEYBOARD = [
    [SET_LANGUAGE_ENGLISH],
    [SET_LANGUAGE_CROATIAN],
    [SET_LANGUAGE_HINDI],
    [SET_LANGUAGE_BENGALI],
]
