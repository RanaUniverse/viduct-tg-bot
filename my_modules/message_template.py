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


BOT_FUNCTIONALITY_NAME = bot_config_settings.BOT_FUNCTIONALITY_NAME


def welcome_message_on_start(user_obj: User):
    text = (
        f"Hello {user_obj.mention_html()}"
        "\n"
        f"Welcome You to the {BOT_FUNCTIONALITY_NAME}"
        "\n"
        f"This Bot Can Help You To Reset Your Device or change device, "
        "and some more usefull things for you."
    )
    return text


def help_msg(user_obj: User):
    text = (
        f"Hello {user_obj.mention_html()},\n"
        "We are here to assist you! 🚀\n\n"
        "Currently, this help section is under development. "
        "Soon, you will be able to find detailed guidance here, "
        "including:\n"
        "- How to set up your server 🖥️\n"
        "- How to configure and use the bot ⚙️\n"
        "- Tips and solutions for common issues 📘\n\n"
        "Stay tuned — more helpful content is on the way!"
    )
    return text




def settings_cmd_msg(user_obj: User):
    text = (
        f"Hello {user_obj.mention_html()},\n"
        "⚙️ The settings feature is not fully available yet.\n\n"
        "In the future, you will be able to customize your preferences here, "
        "such as:\n"
        "- Choosing your preferred language 🌍\n"
        "- Managing notifications 🔔\n"
        "- Adjusting privacy and security options 🔒\n\n"
        "🚧 This section is still under development. Please stay tuned!"
    )
    return text
