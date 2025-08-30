"""
Here i will check some backend logic of how to connect api
"""

import json


import httpx

base_url = "http://localhost:8000"


def check_get_1():
    files_endpoint = "/files/abc.txt"

    url = base_url + files_endpoint
    response = httpx.get(url)

    status_code = response.status_code

    if status_code == 200:
        print("Good Connection Established with 200")

        resp_dict = json.loads(response.text)
        print(resp_dict)

    else:
        print("Not Good Result")
        print("Status Code:", response.status_code)
        print(response.json())


def check_post_1():

    final_endpoint = "/items/"

    url = base_url + final_endpoint

    payload: dict[str, str | int] = {
        "name": "Rana Universe Book",
        "price": 250,
        "description": "This is a good book written for our universe.",
        "tax": 20,
        "extra_key_1": 111,
        "extra_key_2": 222,
        "extra_key_3": 333,
    }

    params = {"tax": 15, "poo": 12}

    response = httpx.post(url, json=payload, params=params)

    status_code = response.status_code

    if status_code == 200:
        print("✅ POST request success (200 OK)")
        resp_dict = json.loads(response.text)
        print(resp_dict)
    else:
        print("❌ POST request failed")
        print("Status Code:", response.status_code)
        try:
            print(response.json())
        except Exception:
            print(response.text)


def check_get_2():
    final_endpoint = "/time/"
    url = base_url + final_endpoint
    parameters_dict = {"after_minute": 200}
    response = httpx.get(url=url, params=parameters_dict)
    print(response.json())


def check_get_profile(tg_user_id: int | str | None = None):
    final_endpoint = "/client/bot/profile"
    url = base_url + final_endpoint

    parameters_dict = {"telegram_id": f"{tg_user_id}"}

    response = httpx.get(url=url, params=parameters_dict)

    print("Status Code:", response.status_code)
    print("Response:", response.json())


def register_profile():
    final_endpoint = "/client/bot/register"
    url = base_url + final_endpoint

    payload = {
        "access_key": "YwfjYlfj",
        "telegram_id": "233",
        "preffered_lang": "en",
    }

    response = httpx.post(url=url, json=payload)

    print("Status Code:", response.status_code)
    print("Response:", response.json())


def get_user_lang(telegram_id: int) -> str | None:
    final_endpoint = "/client/bot/profile"
    url = base_url + final_endpoint
    params = {"telegram_id": telegram_id}

    response = httpx.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("preffered_lang", None)

    elif response.status_code == 400:
        return None

    else:
        return None


def change_user_language(user_tg_id: int, new_lang: str, new_name: str):
    final_endpoint = "/client/bot/profile"
    url = base_url + final_endpoint

    tg_id = str(user_tg_id)
    params = {
        "telegram_id": tg_id,
    }

    data = {
        "name": new_name,
        "preffered_lang": new_lang,
    }

    response = httpx.put(url, params=params, json=data)

    if response.status_code == 200:
        print("Language Updated Successful...")

    elif response.status_code == 422:
        print("Some Error happens here...")

    elif response.status_code == 404:
        print("User not found")

    else:
        print("Unknow things happesn", response.status_code)


if __name__ == "__main__":
    # check_get_profile(111)
    change_user_language(999, "en", "abc")
