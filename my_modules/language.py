"""
Here i will keep some ideas of user's language preference
Fun 1. I will make this fun which actually give the language code the user want to use for him.

"""


def get_user_prefer_language(tg_user_id: int) -> str | None:
    """
    Here i will pass the user's tg id (int) and it will actually get the
    string of his own choice's language, actually it will take it from database
    for now i am just checking with some values.
        Return Values: "en", "bn", "hi", "hr" ...
    """

    # i will make a dict for now against the tg_user_id and get his own string
    # 1. Rana Universe, 2. Linux Account, 3. Razorblade (The below values)
    user_lang_dict = {
        1895194333: "en",
        7914427214: "hi",
        1844500681: "hr",
    }
    lang_value = user_lang_dict.get(tg_user_id, None)

    return lang_value
