#!/usr/bin/python
#-*- coding: utf-8 -*-

#===========================================================
# File Name: WenkuGet.py
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2017-01-06
# Version: 1.0
# Description: Download txt in Baidu Wenku
#===========================================================
import re
import urllib
import urllib2
import os
import time
import cookielib
import HTMLParser
import shutil


class WenkuGet():
    url = ''
    def __init__(self, url):
        self.url = url

    def getPage(self):
        url = self.url
        page = urllib.urlopen(url)
        html = page.read()

#Get txt file:
        txt_path='%s.txt'%str(re.findall(re.compile(r'<title>(.*?)</title>'),html)[0])
        if os.path.exists(txt_path):
            #return False
            print "there's already an existed txt"
        else:
            f = open(txt_path,'a')
            plus_tag = re.findall(re.compile(r'<p>(.*?)</p>'),html)  #List all text(with tag)
            for i in plus_tag:
                print i
                #de_tag = re.compile("\<.*?\>").sub('',i).encode("utf-8")   #Remove tags
                #f.write('%s\n\n'%HTMLParser.HTMLParser().unescape(de_tag).encode("utf-8"))  #Write Body& unescape
                f.write('%s'%HTMLParser.HTMLParser().unescape(i).encode("utf-8"))  #Write Body& unescape
            f.close()


if __name__ == '__main__':
    print "\nHi, this is Shaohua, Enjoy downloading!\n"
    File = WenkuGet("https://wenku.baidu.com/view/6e8c4f3408a1284ac950434b.html?from=search")
    File.getPage()
    print "\ndone"
    time.sleep(3)
