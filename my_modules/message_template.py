"""
Here i will keep some funcions or variable where some most useful predefined
Message will be written and i can use those things in other places, so that
it will easy for me to keep this text generating part here, and code part in
other main code part.

I am making this text support the html of tg, so i need to make sure,
it will have all valid html tags as per telegram docs
(https://core.telegram.org/bots/api#html-style)

"""

from telegram import User


from my_modules import bot_config_settings
from my_modules.translation_message import get_value_from_language_json


BOT_FUNCTIONALITY_NAME = bot_config_settings.BOT_FUNCTIONALITY_NAME


def generate_welcome_message_on_start(
    user_obj: User,
    user_language: str = "en",
):
    user_safe_name = user_obj.mention_html()
    start_text_from_json = get_value_from_language_json(user_language, "start_cmd")
    if start_text_from_json is None:
        return "Some Error for start"
        # i will add logger here.

    start_welcome_text = start_text_from_json.format(
        name=user_safe_name,
    )
    # at upper format i need to must know {name} is present in the json

    return start_welcome_text


def generate_help_msg(
    user_obj: User,
    user_language: str = "en",
):
    help_text_from_json = get_value_from_language_json(user_language, "help_cmd")

    if help_text_from_json is None:
        return "⚠️ Missing help message in JSON."

    help_text = f"Hi {user_obj.mention_html()}" "\n" + help_text_from_json
    return help_text


def generate_settings_cmd_msg(
    user_obj: User,
    user_language: str = "en",
):
    settings_text_from_json = get_value_from_language_json(user_language, "settings_cmd")

    if settings_text_from_json is None:
        return "Missing the Settings in Json"

    settings_text = f"⚙️⚙️⚙️" f"\n" f"{settings_text_from_json}"

    return settings_text
