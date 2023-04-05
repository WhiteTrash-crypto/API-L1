import requests


def main():
    cities = ["Череповец", "London", "SVO"]
    payload = {"n": "", "M": "", "T": "", "q": "", "lang": "ru"}
    for city in cities:
        response = requests.get(f"https://wttr.in/{city}", params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()

