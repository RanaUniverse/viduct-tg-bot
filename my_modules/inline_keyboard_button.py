"""
I will keep some buttons logic so that i can use this
easily in different places
"""

from telegram import InlineKeyboardButton


SET_LANGUAGE_ENGLISH = InlineKeyboardButton(
    text="🇺🇸 English",
    callback_data="set_lang_en",  # IETF: en
)

SET_LANGUAGE_HINDI = InlineKeyboardButton(
    text="🇮🇳 Hindi (हिन्दी)",
    callback_data="set_lang_hi",  # IETF: hi
)

SET_LANGUAGE_BENGALI = InlineKeyboardButton(
    text="🇧🇩 Bengali (বাংলা)",
    callback_data="set_lang_bn",  # IETF: bn
)

SET_LANGUAGE_CROATIAN = InlineKeyboardButton(
    text="🇭🇷 Croatian (Hrvatski)",
    callback_data="set_lang_hr",  # IETF: hr
)

SET_LANGUAGE_GERMAN = InlineKeyboardButton(
    text="🇩🇪 German (Deutsch)",
    callback_data="set_lang_de",  # IETF: de
)

SET_LANGUAGE_FRENCH = InlineKeyboardButton(
    text="🇫🇷 French (Français)",
    callback_data="set_lang_fr",  # IETF: fr
)

SET_LANGUAGE_SPANISH = InlineKeyboardButton(
    text="🇪🇸 Spanish (Español)",
    callback_data="set_lang_es",  # IETF: es
)

SET_LANGUAGE_ITALIAN = InlineKeyboardButton(
    text="🇮🇹 Italian (Italiano)",
    callback_data="set_lang_it",  # IETF: it
)


SET_LANGUAGE_KEYBOARD = [
    [SET_LANGUAGE_ENGLISH],
    [SET_LANGUAGE_CROATIAN],
    [SET_LANGUAGE_HINDI],
    [SET_LANGUAGE_BENGALI],
    [SET_LANGUAGE_GERMAN],
    [SET_LANGUAGE_FRENCH],
    [SET_LANGUAGE_SPANISH],
    [SET_LANGUAGE_ITALIAN],
]


if __name__ == "__main__":
    # I keep the below code just for my reference
    LANGUAGES = {
        "en": {"main": "English", "native": "English"},
        "hi": {"main": "Hindi", "native": "हिन्दी"},
        "bn": {"main": "Bengali", "native": "বাংলা"},
        "hr": {"main": "Croatian", "native": "Hrvatski"},
        "de": {"main": "German", "native": "Deutsch"},
        "fr": {"main": "French", "native": "Français"},
        "es": {"main": "Spanish", "native": "Español"},
        "it": {"main": "Italian", "native": "Italiano"},
    }

    print(LANGUAGES)
