import json

from pathlib import Path


JSON_TEMPLATES_DIR = Path("my_modules/translation_templates")


def get_value_from_language_json(
    language_code: str,
    key_name: str,
):
    """
    The Key Names are like, start, help, settings strings.
    The Language code are like, bn, en, hi, hr, like this code.
    """
    file_name = f"{language_code}.json"
    file_path = JSON_TEMPLATES_DIR / file_name

    if not file_path.exists():
        return f"⚠️ File not found: {file_path}"
    # i dont think for now if this will return this,
    # it will think as the value of the key

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json_content_dict = json.load(f)
    except json.JSONDecodeError as e:
        return f"⚠️ Invalid JSON in {file_path}: {e}"
    # I added this exception so that if json has some
    # inner mistakes it will not stop my program continuation.

    value_of_key = json_content_dict.get(f"{key_name}", None)
    return value_of_key


if __name__ == "__main__":
    abc = get_value_from_language_json(key_name="settings", language_code="bn")
    print(abc)
