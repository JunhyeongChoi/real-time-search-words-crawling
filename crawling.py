from requests_html import HTMLSession

url = "https://www.signal.bz/"
session = HTMLSession()
response = session.get(url,timeout=800000)

response.html.render()

info = response.html.find(".rank-text")
rank = 0
for item in info:
    rank += 1
    print(rank, "위: ", item.text, sep='')