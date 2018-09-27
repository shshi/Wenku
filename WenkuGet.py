#-*- coding: utf-8 -*-
#===========================================================
# Author：Sha0hua
# E-mail:shi.sh@foxmail.com
# Modified Date: 2018-09-28
# Version: 1.0
# Version Description: Download txt from wenku.baidu.com
#===========================================================
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.setrecursionlimit(1000000) #设置最大递归次数（若不设置，默认值为998，递归998次后将出现"maximum recursion depth exceeded"的报错）
 
def Get():
    d.get('https://wenku.baidu.com/view/6e8c4f3408a1284ac950434b.html?from=search')#WE登录页
    print "finished loading"
    try:
        list=d.find_elements_by_tag_name("p")
        #list=d.find_elements_by_class_name("ie-fix")
    except:
        print "error"
    txt_path='%s.txt'%d.title
    f = open(txt_path,'a')
    for i in list:
        try:
            print i.text
            f.write(i.text)        
            #print "=============================================="
        except Exception as e:
            print e
        continue
            
def ShowMore():
    js = "document.getElementById('showMoreDiv').style.display='block'"
    d.execute_script(js)
    d.find_element_by_xpath('//*[@id="showMoreDiv"]/a').click()
    time.sleep(3)
        
if __name__ == "__main__":
    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.stylesheet', 2) #禁加载CSS
    firefoxProfile.set_preference('permissions.default.image', 2) #禁加载图片
    firefoxProfile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false') #禁加载Flash
    options = Options()
    options.add_argument('-headless') #无浏览器参数
    d=webdriver.Firefox(firefoxProfile, firefox_options=options)
    d.set_window_size(1600, 900)
    print "initiating..."        
    Get()
    print "the end"
    d.quit()
