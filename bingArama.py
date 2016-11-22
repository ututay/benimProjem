from urllib import request
from urllib.parse import quote
import json


def bingAra(anahtarKelime):
    anahtar = str()
    içerik = list()
    with open("bing.key") as dosya:
        anahtar = dosya.read()
    başlık = {"Host": "api.cognitive.microsoft.com", "Ocp-Apim-Subscription-Key": anahtar}
    url = "https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=" + quote(anahtarKelime) + "&count=20&offset=0&mkt=tr-TR&safeSearch=Moderate"
    istek = request.Request(
                            url=url,
                            headers=başlık,
                            )

    site   = request.urlopen(istek)
    okunan = site.read().decode("utf-8")
    jsonSözlük = json.loads(okunan, encoding="utf-8")
    for veri in jsonSözlük["value"]:
        if "image" in veri.keys():
            içerik.append(
                          {
                          "name": veri.get("name"),
                          "description": veri.get("description"),
                          "url": veri.get("url"),
                          "image": veri.get("image").get("thumbnail").get("contentUrl"),
                          }
                          )
        else:
            içerik.append(
              {
              "name": veri.get("name"),
              "description": veri.get("description"),
              "url": veri.get("url"),
              }
              )
    return içerik
