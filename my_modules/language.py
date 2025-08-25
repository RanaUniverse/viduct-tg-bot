"""
Here i will keep some ideas of user's language preference
Fun 1. I will make this fun which actually give the language code the user want to use for him.

"""

from telegram import User


def get_user_prefer_language_old(tg_user_id: int) -> str | None:
    """
    Here i will pass the user's tg id (int) and it will actually get the
    string of his own choice's language, actually it will take it from database
    for now i am just checking with some values.
        Return Values: "en", "bn", "hi", "hr" ...
    """

    # 1. Rana Universe, 2. Linux Account, 3. Razorblade (The below values)
    # i will make a dict for now against the tg_user_id and get his own string
    user_lang_dict = {
        1895194333: "bn",
        7914427214: "hi",
        1844500681: "en",
    }
    lang_value = user_lang_dict.get(tg_user_id, None)

    return lang_value


def get_user_preferred_language_code(user_obj: User) -> str:
    """
    Get the preferred language code for a user.
    en, hi, bn, cr, ...

    Current logic:
    - Use Telegram's `user.language_code` if available
    - Otherwise default to 'en'

    Later i will do for:
    - Fetch from your database
    - Or call an external API (e.g., viduct-api)
    """
    return user_obj.language_code or "en"
