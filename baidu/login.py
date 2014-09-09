#!/usr/bin/env python2
import urllib2, urllib, cookielib, json, bs4
USER_NAME = 'hacphoenix@163.com'
USER_PASSWORD = 'tmac16120'
#get baidu cookie key BAIDUID value

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
baidu_url = 'http://www.baidu.com'
opener.open(baidu_url)

#get baidu token

baidu_getapi_url = 'https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3&class=login&logintype=dialogLogin&callback=bd__cbs__dv9v0p'
response = opener.open(baidu_getapi_url)
content = response.read()
req = content[content.find('(')+1:content.find(')')]
token = eval(req)["data"]['token']

#baidu login
baidu_login_url = "https://passport.baidu.com/v2/api/?login"
params = urllib.urlencode({'charset': 'UTF-8',
          'token': token,
          'tpl':'mn',
          'apiver':'v3',
          'safeflg':0,
          'u': 'http://www.baidu.com',
          'isPhone': 'false',
          'logintype': 'dialogLogin',
          'logLoginType': 'pc_loginDialog',
          'loginmerge': 'true',
          'splogin': 'rate',
          'username': USER_NAME,
          'password': USER_PASSWORD,
          'mem_pass': 'on',
          'callback': 'parent.bd__pcbs__gj5oy2',
          'staticpage': 'http://www.baidu.com/cache/user/html/v3Jump.html',
          'subpro': '',
          'codestring': '',
          'quick_user': 0,
          'idc': ''
          })

headers = {'Referer': 'http://www.baidu.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:24.0) Gecko/20140827 Firefox/24.0'}
request = urllib2.Request(baidu_login_url, params, headers)
f = opener.open(request)
#make a tieba post to check whether we login succesfully
'''
tieba_post_url = "http://tieba.baidu.com/f/commit/thread/add"
params = urllib.urlencode({'ie': 'utf-8',
          'kw': 'python',
          'rich_text': '1',
          'content': 'helloworld',
          'title': 'python tieba test',
          'prefix': '',
          'files': [],
          'mouse_pwd': '32,44,33,56,33,33,39,38,29,37,56,36,56,37,56,36,56,37,56,36,56,37,56,36,56,37,56,36,29,37,37,37,37,45,29,37,34,44,36,56,37,36,33,36,14102528913200',
          'mouse_pwd_isclick': 0,
          '__type__': 'thread',
          })
headers = {'Host': 'tieba.baidu.com',
           'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:24.0) Gecko/20140827 Firefox/24.0',
           'Referer': 'http://tieba.baidu.com/f?kw=python',
           }
requset = urllib2.Request(tieba_post_url, params, headers)
gg = opener.open(request)
ff = bs4.BeautifulSoup(gg)
print ff.prettify()
'''
tbs_url = 'http://tieba.baidu.com/dc/common/tbs'
cc = opener.open(tbs_url).read()
aa = bs4.BeautifulSoup(cc)
print aa.prettify()
dd = json.loads(cc)
print dd['is_login']


