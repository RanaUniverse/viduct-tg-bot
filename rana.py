import httpx

BASE_URL = "http://localhost:8000"

def change_user_language(user_tg_id: int, new_lang: str) -> None:
    """
    Update a user's preferred language via API.

    Args:
        user_tg_id (int): The user's Telegram ID.
        new_lang (str): The new language code to set (e.g., 'bn').

    Returns:
        None
    """
    endpoint = "/client/bot/profile"
    url = f"{BASE_URL}{endpoint}"
    
    params = {
        "telegram_id": str(user_tg_id),
    }

    payload = {
        "name": "New Name",
        "preffered_lang": new_lang,
    }

    try:
        response = httpx.put(url, params=params, json=payload)

        if response.status_code == 200:
            print("✅ Language updated successfully.")
        elif response.status_code == 422:
            print("❌ Validation error:", response.json())
        else:
            print(f"⚠️ Unexpected status code {response.status_code}: {response.text}")

    except httpx.RequestError as exc:
        print(f"🚫 An error occurred while making the request: {exc}")


change_user_language(111,"hi")