import requests
import main

article_id = ["Череповец", "London", "SVO"]
payload = {"n": "", "M": "", "T": "", "q": "", "lang": "ru"}


def main():
    for city in article_id:
        response = requests.get(f"https://wttr.in/{city}", params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
