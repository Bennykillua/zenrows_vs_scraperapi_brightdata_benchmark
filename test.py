from firecrawl import Firecrawl

firecrawl = Firecrawl(api_key="fc-YOUR-API-KEY")


# Scrape a website:

doc = firecrawl.scrape("https://www.bbc.com/news/technology", formats=["markdown", "html"])

html = doc.html or ""
markdown = doc.markdown or ""

print(f"Firecrawl   | bytes (html): {len(html)} | bytes (md): {len(markdown)}")
print(html[:300])
print("-" * 60)

print("\n--- Zenrows ---\n")


import requests

zr = requests.get(
    "https://api.zenrows.com/v1/",
    params={
        "apikey": "cfb057cbc15a3617a8dfcb525806ccbbdfe61f94",
        "url": "https://www.bbc.com/news/technology",
        "mode": "auto"
    }
)

print(f"ZenRows    | status: {zr.status_code} | bytes: {len(zr.text)}")
print(zr.text[:300])
print("-" * 60)

print("\n--- Bright Data Tests ---\n")


import requests

bd = requests.post(
    "https://api.brightdata.com/request",
    headers={"Authorization": "Bearer a988dc79-4136-44dd-ae31-d6c83e9c73a8"},
    json={
        "zone": "web_unlocker1",
        "url": "https://www.bbc.com/news/technology",
        "format": "raw"
    }
)

print(f"Bright Data | status: {bd.status_code} | bytes: {len(bd.text)}")
print(bd.text[:300])