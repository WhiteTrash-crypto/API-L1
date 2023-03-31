import requests
import main

payload = {"n" : "" , "M" : "" ,"T" : "","q" : "", "lang" : "ru"}
urls = ("https://wttr.in/Череповец","https://wttr.in/London","https://wttr.in/SVO")

def main():
  for url in urls:
    response = requests.get(url, params = payload)
    response.raise_for_status() 
    print(response.text)
if __name__ == '__main__':
  main()
