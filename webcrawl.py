#!/usr/bin/env python
# -*- coding: utf-8 -*-
#BOOK EXAMPLE
import os
import sys
from urllib2 import urlopen
from urllib2 import HTTPError
from urllib import urlretrieve
from bs4 import BeautifulSoup
import re
import random
import datetime
import json
import csv


# def gettitle(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# title = gettitle("http://www.pythonscraping.com/pages/page1.html")
# if title == None:
#     print("title not found")
# else:
#     print(title)

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
# namelist = bsObj.findAll("span",{"class":"green"})
# for name in namelist:
#     print(name.get_text())
# alltext = bsObj.findAll(id="text")
# print(alltext[0].get_text())
# html = urlopen("http://www.pythonscraping.com/pages/page3.html")
# bsObj = BeautifulSoup(html)
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

# for child in bsObj.find("table",{"id":"giftList"}).children:
#     print(child)

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.get_text())
# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
# for image in images:
#     print(image["src"])
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
# for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
#Attention# ------------------------------------------------------------------
# random.seed(datetime.datetime.now())
# def getlinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html)
#     return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
# links = getlinks("/wiki/Kevin_Bacon")
# print(links)
# while len(links)>0:
#     newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getlinks(newArticle)

# ------------------------------------------------------------------
# pages = set()
# def getlinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html)
#     for link in bsObj.findAll("a",href = re.compile("^(/wiki/)")):
#         if "href" in link.attrs:
#             if link.attrs["href"] not in pages:
#                 newPage = link.attrs["href"]
#                 print(newPage)
#                 pages.add(newPage)
#                 getlinks(newPage)
# getlinks("")
# ------------------------------------------------------------------
# pages = set()
# def getlinks(pageUrl):
#     global pages
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html)
#     try:
#         print(bsObj.h1.get_text())
#         print(bsObj.find(id="mw-content-text").findAll("p")[0])
#         print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
#     except AttributeError:
#         print("NO enough attributes")
#     for link in bsObj.findAll("a",href = re.compile("^(/wiki/)")):
#         if "href" in link.attrs:
#             if link.attrs["href"] not in pages:
#                 newPage = link.attrs["href"]
#                 print("------------------------\n"+newPage)
#                 pages.add(newPage)
#                 getlinks(newPage)
# getlinks("")

# ------------------------------------------------------------------
# pages =set()
# random.seed(datetime.datetime.now())
# def getInternalLinks(bsObj,includeUrl):
#     internalLinks = []
#     for link in bsObj.findAll("a",href = re.compile("^(/|.*"+includeUrl+")")):
#         if link.attrs["href"] is not None:
#             if link.attrs["href"]  not in internalLinks:
#                 internalLinks.append(link.attrs["href"])
#     return internalLinks
#
# def getExternalLinks(bsObj,excludeUrl):
#     externalLinks = []
#     for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
#         if link.attrs["href"] is not None:
#             if link.attrs["href"] not in externalLinks:
#                 externalLinks.append(link.attrs["href"])
#     return externalLinks
#
# def splitAddress(address):
#     addressParts = address.replace("http://","").split("/")
#     return addressParts
#
# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bsObj = BeautifulSoup(html)
#     externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
#     if len(externalLinks) == 0:
#         internalLinks = getInternalLinks(startingPage)
#         return getInternalLinks(internalLinks[random.randint(0,len(internalLinks)-1)])
#     else:
#         return externalLinks[random.randint(0,len(externalLinks)-1)]
#
# def followExternalOnly(startingSite):
#
#     externalLink = getRandomExternalLink("http://oreilly.com")
#     print("随机外链")
#     print(externalLink)
#     followExternalOnly(externalLink)

# followExternalOnly("http://oreilly.com")

# ------------------------------------------------------------------

# allExtLinks = set()
# allIntLinks = set()
# def getAllExternalLinks(siteUrl):
#     html = urlopen(siteUrl)
#     bsObj = BeautifulSoup(html)
#     internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
#     externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
#
#     for link in externalLinks:
#         if link not in allExtLinks:
#             allExtLinks.add(link)
#             print(link)
#
#     for link in internalLinks:
#         if link not in allIntLinks:
#             try:
#                 print("下一连接")
#                 print(link)
#                 allIntLinks.add(link)
#                 getAllExternalLinks(link)
#             except AttributeError:
#                 print("maybe something wrong")
# getAllExternalLinks("http://oreilly.com")


# ------------------------------------------------------------------
import json
#
# def getCountry(ipAddress):
#     response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
#     responseJson = json.loads(response)
#     return responseJson.get("country_code")
#
# print(getCountry("58.78.253.58"))

# ------------------------------------------------------------------
# import json
#
# jsonString = '{"arrayofNums":[{"number":0},{"number":1},{"number":2}],"arrayofFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
#
# jsonObj = json.loads(jsonString)
# print(jsonObj.get("arrayofNums"))
# print(jsonObj.get("arrayofNums")[1])
# print(jsonObj.get("arrayofNums")[1].get("number")+jsonObj.get("arrayofNums")[2].get("number"))
# print(jsonObj.get("arrayofFruits")[2].get("fruit"))

# ------------------------------------------------------------------

# random.seed(datetime.datetime.now())
#
# def getLinks(articleUrl):
#     hrml = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(hrml)
#     return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
#
# def getHistoryIPs(pageUrl):
#     pageUrl = pageUrl.replace("/wiki/","")
#     historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
#     # print("history url is"+historyUrl)
#     html = urlopen(historyUrl)
#     bsObj = BeautifulSoup(html)
#     ipAddresses = bsObj.findAll("a",{"class":"mw-anonuserlink"})
#     addressList = set()
#     for ipAddress in ipAddresses:
#         addressList.add(ipAddress.get_text())
#         print(ipAddress)
#     return addressList
#
# links = getLinks("/wiki/Python_(programming_language)")
# while (len(links)>0):
#     for link in links:
#         print("--------------------------------")
#         HistoryIPs = getHistoryIPs(link.attrs["href"])
#         for historyIP in HistoryIPs:
#             print(historyIP)
#
#     newlink = links[random.randint(0,len(links)-1)].attrs["href"]
#     links = getLinks(newlink)

# def getCountry(ipAddress):
#     try:
#         response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode("utf-8")
#     except HTTPError:
#         return None
#     responseJson = json.loads(response)
#     return responseJson.get("country_code")
#
# while (len(links)>0):
#     for link in links:
#         print("--------------------------------")
#         HistoryIPs = getHistoryIPs(link.attrs["href"])
#         for historyIP in HistoryIPs:
#             country = getCountry(historyIP)
#
#             print(historyIP)
#             print(country)
#
#     newlink = links[random.randint(0,len(links)-1)].attrs["href"]
#     links = getLinks(newlink)

# ------------------------------------------------------------------

# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html)
# imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
# print(imageLocation)
# urlretrieve(imageLocation,"logo.jpg")

# ------------------------------------------------------------------

# downloadDirectory = "download"
# baseUrl = "http://pythonscraping.com"
#
# def getAbsoluteURL(baseUrl,source):
#     if source.startswith("http://www."):
#         url = "http://"+source[11:]
#     elif source.startswith("http://"):
#         url = source
#     elif source.startswith("www."):
#         url = source[4:]
#         url = "http://"+source
#     else:
#         url = baseUrl +"/"+source
#     if baseUrl not in url:
#         return None
#     return url
#
# def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
#     path = absoluteUrl.replace("www","")
#     path = path.replace(baseUrl,"")
#     path = downloadDirectory+path
#     directory = os.path.dirname(path)
#
#     if not os.path.exists(directory):
#         os.makedirs(directory)
#
#     return path
#
# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html)
# downloadList = bsObj.findAll(src=True)
#
# for download in downloadList:
#     fileUrl = getAbsoluteURL(baseUrl,download["src"])
#     if fileUrl is not None:
#         print(fileUrl)
#
# urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))

# ------------------------------------------------------------------

# csvFile =  open("test.csv","w+")
# try:
#     writer = csv.writer(csvFile)
#     writer.writerow(("number","number plus 2","number times 2"))
#     for i in range(10):
#         writer.writerow((i,i+2,i*2))
#
# finally:
#     csvFile.close()


# ------------------------------------------------------------------
# reload(sys)
# sys.setdefaultencoding('utf-8')
# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html)
#
# table = bsObj.findAll("table",{"class":"wikitable"})[0]
# rows = table.findAll("tr")
#
# csvFile = open("test.csv", 'w+')
# writer = csv.writer(csvFile)
#
# try:
#     for row in rows:
#         csvRow =[]
#         for cell in row.findAll(["td","th"]):
#             csvRow.append(cell.get_text())
#             writer.writerow(csvRow)
#
# finally:
#     csvFile.close()


# ------------------------------------------------------------------

# ------------------------------------------------------------------
import scrapy
# import pymysql
#
# conn = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = 'qwer1234',db ='mysql')
# cur = conn.cursor()
# cur.execute("USE scraping")
# cur.execute("SELECT * FROM ")
# print(cur.fetchone())
# cur.close()
# conn.close()

import pymysql

# conn= pymysql.connect(host='127.0.0.1', user='root', passwd='qwer1234',db ='mysql',charset="utf8")
# cur=conn.cursor()
# cur.execute("CREATE DATABASE scraping")
# cur.execute("USE scraping")   #创建数据库
# cur.execute("CREATE TABLE pages (id INT NOT NULL AUTO_INCREMENT, title VARCHAR(200) ,content VARCHAR (10000),created TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,PRIMARY KEY (id))")
# cur.execute("INSERT INTO pages (title,content) VALUES('test','contenttest1234567890')")
# #
# cur.execute("SELECT * FROM pages")
# data=cur.fetchall()
# print(data)
# #
# cur.close()
# conn.close()
# random.seed(datetime.datetime.now())
# def store(title,content):
#     cur.execute("INSERT INTO pages (title,content) VALUES (\"%s\", \"%s\")",(title,content))
#     cur.connection.commit()
#
# def getLinks(articleUrl):
#
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html)
#     title = bsObj.find("h1").get_text()
#     content = bsObj.find("div",{"id":"mw-content-text"}).find("p").get_text()
#     store(title,content)
#     return bsObj.find("div",{"id":"bodyContent"}).findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
# links = getLinks("/wiki/Kevin_Bacon")
# try:
#     while len(links)>0:
#         newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
#         print(newArticle)
#         links = getLinks(newArticle)
# finally:
#     cur.close()
#     conn.close()
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# conn= pymysql.connect(host='127.0.0.1', user='root', passwd='qwer1234',db ='mysql')
# cur=conn.cursor()
# cur.execute("USE wikipedia")
# cur.execute("CREATE DATABASE wikipedia")
# cur.execute("CREATE TABLE pages (id INT NOT NULL AUTO_INCREMENT, url VARCHAR(255) ,created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id))")
# cur.execute("CREATE TABLE links (id INT NOT NULL AUTO_INCREMENT, frompageID INT NOT NULL ,topageID INT NOT NULL ,created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id))")
# cur.close()
# conn.close()

# def InsertPageIfNotExist(url):
#     cur.execute("SELECT * FROM pages WHERE url = %s",(url))
#     if cur.rowcount == 0:
#         cur.execute("INSERT INTO pages (url) VALUES (%s)",(url))
#         conn.commit()
#         return cur.lastrowid
#     else:
#         return cur.fetchone()[0]
#
#
# def insertLink(fromPageId,toPageId):
#     cur.execute("SELECT * FROM links WHERE frompageID = %s AND topageID = %s",(int(fromPageId),int(toPageId)))
#     if cur.rowcount == 0:
#         cur.execute("INSERT INTO links (frompageID,topageID) VALUES (%s,%s)",(int(fromPageId),int(toPageId)))
#         conn.commit()
#
# pages =set()
# def getLinks(pageUrl,recursionLevel):
#     global pages
#     if recursionLevel > 4:
#         return
#     pageId = InsertPageIfNotExist(pageUrl)
#     html = urlopen("http://en.wikipedia.org"+pageUrl)
#     bsObj = BeautifulSoup(html)
#     for link in bsObj.findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
#         insertLink(pageId,InsertPageIfNotExist(link.attrs['href']))
#         if link.attrs['href'] not in pages:
#             newPage = link.attrs['href']
#             pages.add(newPage)
#             getLinks(newPage,recursionLevel+1)
#
# getLinks("/wiki/Kevin_Bacon",0)
# cur.execute("SELECT * FROM pages")
# data=cur.fetchall()
# print(data)
# cur.execute("DROP DATABASE test15")
# cur.close()
# conn.close()
# ------------------------------------------------------------------
# ------------------------------------------------------------------
# conn= pymysql.connect(host='127.0.0.1', user='root', passwd='qwer1234',db ='mysql')
# cur=conn.cursor()
# cur.execute("USE test15")
# cur.close()
# conn.close()
# ------------------------------------------------------------------
# ------------------------------------------------------------------
import smtplib
from email.mime.text import MIMEText
import time
#
# msg = MIMEText("body msg")
# msg['Subject'] = "New Email"
# msg['From'] = "mxb@local.com"
# msg['To'] = "mxbxjtu@hotmail.com"
#
# s = smtplib.SMTP('127.0.0.1')
# s.sendmail(msg)
#
# s.quit()

# bsObj = BeautifulSoup('')
# while (bsObj.find() == ''):
#     print()
#     sendemail()


# ------------------------------------------------------------------
# ------------------------------------------------------------------
# text = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(text.read())

import csv
from io import StringIO
# data =urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
# dataFile = StringIO(data)
# csvRD = csv.reader(dataFile)
# for row in csvRD:
#     print(row[0])
#     print(row[1])

# dictRD = csv.DictReader(dataFile)
# print(dictRD.fieldnames)
#
# for row in dictRD:
#     print(row)
# from pdfminer.pdfinterp import PDFResourceManager
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# def readPDF(pdffile):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr,retstr,laparams=laparams)
#
#     process_pdf(rsrcmgr,device,pdffile)
#     device.close()
#
#     content = retstr.getvalue()
#     retstr.close()
#     return content
# pdffile = urlopen('')
# out = readPDF(pdffile)
# pdffile.close()


# ------------------------------------------------------------------
# ------------------------------------------------------------------

from zipfile import ZipFile
from io import BytesIO

# wordFile = urlopen("http://pythonscraping.com/files/AWordDocument.docx").read()
# wordFile = BytesIO(wordFile)
# document = ZipFile(wordFile)
# xmlcontent = document.read('word/document.xml')
# # print(xmlcontent.decode('utf-8'))
# wordObj = BeautifulSoup(xmlcontent.decode('utf-8'))
# textstr = wordObj.findAll("w:t")
# for i in textstr:
#     # print(i.text)
#     close =""
#     try:
#         style = i.parent.previousSibling.find("w:pstyle")
#         if style is not None and style["w:val"] == "Title":
#             print("<h1>")
#             close = "<h1>"
#     except AttributeError:
#         pass
#     print(i.text)
#     print(close)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

# def ngrams(input,n):
#     input = input.split(' ')
#     output = []
#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     return output

# def ngrams(input,n,content):
#     content = re.sub('\n+'," ",content)
#     content = re.sub(' +'," ",content)
#     content = bytes(content,"UTF-8")
#     content = content.decode("ascii","ignore")
#
#     print(content)
#     input = input.split(' ')
#     output = []
#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     return output

#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html)
# content = bsObj.find("div",{"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content,2)
# print(ngrams)
# print(len(ngrams))

import string
from collections import OrderedDict
#
# def cleanInput(input):
#     input = re.sub('\n+'," ",input)
#     input = re.sub('\[[0-9]*\]',"", input)
#     input = re.sub(' +'," ",input)
#     # input = bytes(input, "UTF-8")
#     # input = input.decode("ascii","ignore")
#
#     cleaninput =[]
#     input = input.split(' ')
#     for item in input:
#         item = item.strip(string.punctuation)
#         if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
#             cleaninput.append(item)
#
#     return cleaninput
#
#
# def ngrams(input,n):
#
#     input = cleanInput(input)
#     output = []
#     for i in range(len(input)-n+1):
#         output.append(input[i:i+n])
#     return output
#
# html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
# bsObj = BeautifulSoup(html)
# content = bsObj.find("div",{"id":"mw-content-text"}).get_text()
# ngrams = ngrams(content,2)
# ngrams = OrderedDict(sorted(ngrams,key = lambda t: t[1] ,reverse = True))
#
# print(ngrams)
# print(len(ngrams))

# ------------------------------------------------------------------
# ------------------------------------------------------------------



import string
import operator

# def iscommon(ngram):
#     commonwords = ["the","be","and","of","a","in","to","have",
#                    "it","i","that","for","you","he","with","on","do",
#                    "say","this","they","is","an","at","but","we","his",
#                    "from","that","not","by","she","or","as","what","go",
#                    "their","can","who","get","if","would","her","all","my",
#                    "make","about","know","will","as","up","one","time","has",
#                    "been","there","year","so","think","when","which","them",
#                    "some","me","people","take","out","into","just","see","him",
#                    "your","come","could","now","than","like","other","how","then",
#                    "its","our","two","more","these","want","way","look","first",
#                    "also","new","because","day","more","use","no","man","find",
#                    "here","thing","give","many","well"]
#     for word in ngram:
#         if word in commonwords:
#             return True
#     return False

# from random import randint
#
# def WordListSum(wordList):
#     sum = 0
#     for word,value in wordList.items():
#         sum += value
#     return sum
#
# def retrieveRandomWord(wordList):
#     randIndex = randint(1,WordListSum(wordList))
#     for word,value in wordList.items():
#         randIndex -= value
#         if randIndex <= 0:
#             return word
#
# def buildWordList(text):
#     text = text.replace("\n"," ")
#     text = text.replace("\""," ")
#     punctuation = [',',', ','.',';',':']
#     for symbol in punctuation:
#         text = text.replace(symbol," "+symbol+" ")
#     words = text.split(" ")
#     words = [word for word in words if word != ""]
#     WordDict = {}
#     for i in range(1,len(words)):
#         if words[i-1] not in WordDict:
#             WordDict[words[i-1]] = {}
#         if words[i-1] not in WordDict[words[i-1]]:
#             WordDict[words[i-1]][words[i]] = 0
#             WordDict[words[i-1]][words[i]] = WordDict[words[i-1]][words[i]] + 1
#
#     return WordDict
#
# text = urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read()
# worddict = buildWordList(text)
# length =100
# chain = ""
#
# currentword = "I"
# for i in range(0,length):
#     chain += currentword + " "
#     currentword = retrieveRandomWord(worddict[currentword])
# print(chain)


# conn = pymysql.connect(host ='127.0.0.1',user = 'root',passwd = 'qwer1234',db ='mysql')
# cur = conn.cursor()
# cur.execute("USE wikipedia")
# cur.close()
# conn.close()
# class SolutionFound(RuntimeError):
#     def __init__(self,message):
#         self.message = message
#
# def getlinks(fromPagaId):
#     cur.execute("SELECT toPageId FROM links WHERE fromPageId = %s",(fromPagaId))
#     if cur.rowcount == 0:
#         return None
#     else:
#         return [x[0] for x in cur.fetchall()]
#
# def constructDict(currentPageId):
#     links =getlinks(currentPageId)
#     if links:
#         return dict(zip(links,[{}]*len(links)))
#     return {}
#
#
# def searchDepth(targetPageId,currentPageId,linkTree,depth):
#     if depth == 0:
#         return linkTree
#     if not linkTree:
#         linkTree = constructDict(currentPageId)
#         if not linkTree:
#             return {}
#
#     if targetPageId in linkTree.keys():
#         print("target"+str(targetPageId)+"found")
#         raise SolutionFound("page"+ str(currentPageId))
#
#     for branchkey,branchvalue in linkTree.items():
#         try:
#             linkTree[branchkey] = searchDepth(targetPageId,branchkey,branchvalue,depth - 1)
#         except SolutionFound as e:
#             print(e.message)
#             raise SolutionFound("page"+ str(currentPageId))
#     return linkTree
#
#
# try:
#     searchDepth(134951,1,{},4)
#     print("none")
# except SolutionFound as e:
#     print(e.message)

# ------------------------------------------------------------------
# ------------------------------------------------------------------
import sys
reload(sys)
sys.setdefaultencoding('gbk')
from nltk import word_tokenize
from nltk import Text

# tokens = word_tokenize("here is some not very interesting text")
# text = Text(tokens)
# text = str("here is some not very interesting text")
# # from nltk.book import *
#
from nltk import FreqDist
# fdist = FreqDist(text)
# print(fdist.most_common(10))


from nltk import bigrams
# big = bigrams("here is some not very interesting text")
# bigdist = FreqDist(big)
# print(bigdist.items())

from nltk import ngrams
# big = ngrams("here is some not very interesting text",4)
# bigdist = FreqDist(big)
# print(bigdist.items())

from nltk import pos_tag
# print(pos_tag("here is some not very interesting text"))

import requests
# params = {'firstname':'Ryan','lastname':'Mitchell'}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
# print(r.text)

# params = {'email_addr':'ryan.e.mitchell@gmail.com'}
# r =requests.post("http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi",data=params)
# print(r.text)

# files = {'uploadFile':open('../sample.png'),'rb'}
# r = requests.post("http://pythonscraping.com/pages/processing2.php",files=files)
# print(r.text)

# params = {'username':'Ryan','password':'password'}
# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
# print(r.cookies.get_dict())
# r = requests.post("http://pythonscraping.com/pages/cookies/profile.php",cookies= r.cookies)
# print(r.text)

# session = requests.Session()
# params = {'username':'Ryan','password':'password'}
# s = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
# print(s.cookies.get_dict())
# s = session.post("http://pythonscraping.com/pages/cookies/profile.php",cookies= s.cookies)
# print(s.text)

from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

# auth = HTTPBasicAuth('ryan','password')
# r = requests.post("http://pythonscraping.com/pages/auth/login.php",auth=auth)
# print(r.text)

from selenium import webdriver
import time

# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# time.sleep(3)
# page = driver.page_source
# bsObj = BeautifulSoup(page)
# # print(bsObj.find(id = "content"))
# print(driver.find_element_by_id('content').text)
# driver.close()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# try:
#     element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"loadedButton")))
#
# finally:
#     print(driver.find_element_by_id("content").text)
#     driver.close()

from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

# def waitforload(driver):
#     elem = driver.find_element_by_tag_name("html")
#     count = 0
#     while True:
#         count +=1
#         if count > 20:
#             print("time out after 10 secs and auto return")
#             return
#         time.sleep(.5)
#         try:
#             elem = driver.find_element_by_tag_name("html")
#         except StaleElementReferenceException:
#             return
#
# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
# waitforload(driver)
# print(driver.page_source)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

from PIL import Image,ImageFilter

# kitten = Image.open("logo.jpg")
# bk = kitten.filter(ImageFilter.GaussianBlur)
# bk.save("new.jpg")
# bk.show()

import subprocess

# def cleanFile(filepath,newfilepath):
#     image = Image.open(filepath)
#     image = image.point(lambda x: 0 if x<143 else 255)
#     image.save(newfilepath)
#     subprocess.call(["tesseract", newfilepath, "output"])
#     outputfile = open("output.txt","r")
#     print(outputfile.read())
#     outputfile.close()
#
#
# cleanFile("D:/test.jpg","new.png")

# c
# driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# time.sleep(2)
#
# driver.find_element_by_id("sitbLogoImg").click()
#
# imagelist = set()
#
# time.sleep(5)
# while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
#     driver.find_elements_by_id("sitbReaderRightPageTurner").click()
#     time.sleep(2)
#     pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
#     for page in pages:
#         image = page.get_attribute("src")
#         imagelist.add(image)
#
#     driver.quit()
#
#     for image in sorted(imagelist):
#         urlretrieve(image,"page.jpg")
#         p = subprocess.Popen(["tesseract","page.jpg","page"],stdout= subprocess.PIPE,stderr=subprocess.PIPE)
#         p.wait()
#         f = open("page.txt","r")
#         print(f.read())

from PIL import ImageOps

# def cleanImage(imagepath):
#     image = Image.open(imagepath)
#     image = image.point(lambda x: 0 if x<143 else 255 )
#     borderImage = ImageOps.expand(image,border=20,fill = 'white')
#     borderImage.save(imagepath)
#
# html = urlopen("http://pythonscraping.com/humans-only")
# bsObj = BeautifulSoup(html)
# imagelocation = bsObj.find("img",{"title":"Image CAPTCHA"})["src"]
# print(imagelocation)
# formbuildID = bsObj.find("input",{"name":"form_build_id"})["value"]
# print(formbuildID)
# captchaSID = bsObj.find("input",{"name":"captcha_sid"})["value"]
# print(captchaSID)
# captchaToken = bsObj.find("input",{"name":"captcha_token"})["value"]
# print(captchaToken)
# captchaUrl = "http://pythonscraping.com"+imagelocation
# urlretrieve(captchaUrl,"captcha.jpg")
# cleanImage("captcha.jpg")
#
# p = subprocess.Popen(["tesseract","captcha.jpg","captcha"],stdout= subprocess.PIPE,stderr=subprocess.PIPE)
# p.wait()
# f = open("captcha.txt","r")
# print("flag")
# captchaResponse = f.read().replace(" ","").replace("\n","")
#
# print(captchaResponse)
#
# if len(captchaResponse) == 5:
#     params = {"captcha_token":captchaToken, "captcha_sid":captchaSID,
#               "form_id":"comment_node_page_form","form_build_id":formbuildID,
#               "captcha_response":captchaResponse,"name":"Ryan Mitchell",
#               "subject":"I come to seek the Grail",
#               "comment_body[und][0][value]":
#                                         "...and I am definitely not a bot"}
#     r =requests.post("http://www.pythonscraping.com/comment/reply/10",data=params)
#
#     responseObj = BeautifulSoup(r.text)
#     if responseObj.find("div",{"class":"messages"}) is not None:
#         print(responseObj.find("div",{"class":"messages"}).get_text())
#
# else:
#     print("error reading captcha")


#**************************************************************************************

# session = requests.Session()
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkit 537.36 (KHTML, like Gecko) Chrome",
#            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
# url = "http://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
# req = session.get(url,headers=headers)
# bsObj = BeautifulSoup(req.text)
# print(bsObj.find("table",{"class":"table-striped"}))


# driver = webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# print("what")
# driver.get("http://pythonscraping.com")
# print("here1")
# driver.implicitly_wait(1)
# print("here2")
# print(driver.get_cookies())
#
# savecookies = driver.get_cookies()
#
# driver2 = webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
#
# driver2.get("http://pythonscraping.com")
# driver2.delete_all_cookies()
# for cookie in savecookies:
#     driver2.add_cookie(cookie)
#
# driver2.get("http://pythonscraping.com")
# driver.implicitly_wait(1)
# print(driver.get_cookies())

# driver.close()
# driver2.close()



from selenium.webdriver.remote.webelement import WebElement
# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/itsatrap.html")
# print(driver)
# links = driver.find_element_by_tag_name("a")
# print(links)
# # for link in links:
# if not links.is_displayed():
#     print("the link" + links.get_attribute("href") + "is a trap")
#
# fields = driver.find_element_by_tag_name("input")
# print(fields)
# # for field in fields:
# if not fields.is_displayed:
#     print("do not change the value of" + fields.get_attribute("name"))
#
#
#**************************************************************************************
#**************************************************************************************

import unittest
# class TestAddition(unittest.TestCase):
#     def setUp(self):
#         print("setting up")
#
#     def tearDown(self):
#         print("tearing down")
#
#     def test_twoplustwo(self):
#         total = 2+2
#         self.assertEqual(4,total)
#
# if __name__ == "__main__":
#     unittest.main()

# class TestWikipedia(unittest.TestCase):
#     bsObj = None
#
#     def setUpClass():
#         global bsObj
#         url = "http://en.wikipedia.org/wiki/Monty_Python"
#         bsObj = BeautifulSoup(url)
#
#     def test_titleText(self):
#         global bsObj
#         pageTitle = bsObj.find("h1").get_text()
#         self.assertEqual("Monty Python",pageTitle)
#
#     def test_contentExists(self):
#         global bsObj
#         content = bsObj.find("div",{"id":"mw-content-text"})
#         self.assertIsNotNone(content)
#
# if __name__ == "__main__":
#     unittest.main()
from  urllib import unquote
# class TestWikipedia(unittest.TestCase):
#     bsObj = None
#     url = None
#     def test_pageProperties(self):
#         global bsObj
#         global url
#         url = "http://en.wikipedia.org/wiki/Monty_Python"
#         # for i in range(1,100):
#         bsObj = BeautifulSoup(urlopen(url))
#         titles = self.titleMatchesUrl()
#         self.assertEqual(titles[0],titles[1])
#         self.assertTrue(self.contentExists())
#         url = self.getNextLink()
#
#         print("done")
#
#     def titleMatchesUrl(self):
#         global bsObj
#         global url
#         pageTitle = bsObj.find("h1").get_text()
#         urlTitle = url[(url.index("/wiki/")+6):]
#         urlTitle = urlTitle.replace("_"," ")
#         urlTitle = unquote(urlTitle)
#         return [pageTitle.lower(),urlTitle.lower()]
#     def contentExists(self):
#         global bsObj
#         content = bsObj.find("div",{"id":"mw-content-text"})
#         if content is not None:
#             return True
#         return False
#
#     def getNextLink(self):
#         pass
#
# if __name__ == "__main__":
#      unittest.main()


# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://en.wikipedia.org/wiki/Monty_Python")
# assert "Monty Python" in driver.title
# driver.close()

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get("http://pythonscraping.com/pages/form.html")
#
# firstnamefield = driver.find_element_by_name("firstname")
# lastnamefield = driver.find_element_by_name("lastname")
# submitButton = driver.find_element_by_id("submit")
#
# firstnamefield.send_keys("Ryan")
# lastnamefield.send_keys("Mitchell")
# submitButton.click()

# actions = ActionChains(driver).click(firstnamefield.send_keys("Ryan")).click(lastnamefield.send_keys("Mitchell")).send_keys(Keys.RETURN)
# actions.perform()

# print(driver.find_element_by_tag_name("body").text)
# driver.close()


# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get('http://pythonscraping.com/pages/javascript/draggableDemo.html')
# print(driver.find_element_by_id("message").text)
# element = driver.find_element_by_id("draggable")
# target = driver.find_element_by_id("div2")
# actions = ActionChains(driver)
# actions.drag_and_drop(element,target).perform()
#
# print(driver.find_element_by_id("message").text)

# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
# driver.get('http://www.pythonscraping.com/')
# driver.get_screenshot_as_file('sample.png')

# class TestADDition(unittest.TestCase):
#     driver = None
#     def setUp(self):
#         global driver
#         driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs')
#         driver.get('http://www.pythonscraping.com/pages/javascript/draggableDemo.html')
#
#     def tearDown(self):
#         print("tearing down the test")
#
#     def test_drag(self):
#         global driver
#         element = driver.find_element_by_id("draggable")
#         target = driver.find_element_by_id("div2")
#         actions = ActionChains(driver)
#         actions.drag_and_drop(element,target).perform()
#
#         self.assertEqual("You are definitely not a bot!",driver.find_element_by_id("message").text)
#     if __name__ == "__main__":
#         unittest.main()
#
#
import socks
import socket

# socks.set_default_proxy(socks.SOCKS5,"localhost",9150)
# socket.socket = socks.socksocket
# print(urlopen('http://icanhazip.com').read())
#
#
# service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5']
# driver =webdriver.PhantomJS(executable_path='D:/program/phantomjs-2.1.1-windows/bin/phantomjs',service_args=service_args)
# driver.get("http://icanhazip.com")
# driver.close()