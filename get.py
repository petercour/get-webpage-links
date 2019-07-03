import re, urllib.request


def getLinks(url):
    htmlSource = urllib.request.urlopen(url).read()
    htmlSource = htmlSource.decode("utf-8")
    
    linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
    return linksList


linksList = getLinks("https://news.ycombinator.com")
for link in linksList:
    print(link)
