from urllib.request import urlopen
import bs4 as BeautifulSoup
import re
import json
import os


class CarbeoParser:

    # html = urlopen('http://www.carbeo.com/index.php/prixmoyens')
    # soup = BeautifulSoup.BeautifulSoup(html)
    # pricePattern = re.compile(r'(^\d+([,.]\d{1,3})?)')

    # tdOddTags = soup.findAll('tr', attrs={"class": u"officialPriceBe_odd"})

    # dict = {}
    # for elem in tdOddTags:
    #     name = elem.find('td', attrs={"class": u"officialPriceBe_col1"}).text
    #     price = elem.find('td', attrs={'class': None}).text
    # print(name," : ",price)
    #     regexedPrice = (
    #         pricePattern.search(price).groups()[0]).replace(',', '.')
    # print(regexedPrice)
    #     dict[name] = regexedPrice
    # print("dict[",name,"]:",dict[name])

    def __init__(self, aUrl, aFileName):
        myCompiledRegex = re.compile(r'(^\d+([,.]\d{1,3})?)')
        aBunchOfTags = self.getHtmlContent(aUrl)
        myDict = self.processHtmlContent(aBunchOfTags, myCompiledRegex)
        self.writeJson(aFileName, myDict)

    def getHtmlContent(aUrl):
        myHtml = urlopen(aUrl)
        mySoup = BeautifulSoup.BeautifulSoup(myHtml)
        return mySoup.findAll('tr', attrs={"class": u"officialPriceBe_odd"})

    def processHtmlContent(aBunchOfTags, aCompiledRegex):
        aDict = {}
        for elem in aBunchOfTags:
            name = elem.find(
                'td', attrs={"class": u"officialPriceBe_col1"}).text
            price = elem.find('td', attrs={'class': None}).text
            # print(name," : ",price)
            regexedPrice = (
                aCompiledRegex.search(price).groups()[0]).replace(',', '.')
            # print(regexedPrice)
            dict[name] = regexedPrice
        return aDict

    def writeJson(aFileName, aDict):
        if os.access(aFileName, os.W_OK):
            with open(aFileName, 'w', encoding='utf-8') as f:
                json.dump(aDict, f, indent=4)