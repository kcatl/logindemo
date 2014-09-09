#!/usr/bin/env python2

import urllib, urllib2, cookielib

#global variables
USER_NAME = ""
USER_PASSWD = ""
LOGIN_URL = "http://172.18.90.155/portal/j_spring_security_check"
LOGIN = "http://172.18.90.155/portal/site/whxd/login.jsp"

#enable cookie
cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
urllib2.install_opener(opener)
content = opener.open(LOGIN)
#open the login page

params = urllib.urlencode({
    'j_username': USER_NAME,
    'j_password': USER_PASSWD
})

headers = {'HOST': '172.18.90.155',
           'USER-AGENT': 'Mozilla/5.0 (X11; Linux i686; rv:24.0) Gecko/20140827 Firefox/24.0',
           'Referer': 'http://172.18.90.155/portal/site/whxd/login.jsp',
           }
request = urllib2.Request(LOGIN_URL, params, headers)

if content:
    #print "ok"
    try:
        a = opener.open(request)
        print a.geturl()
    except:
        print "wrong"
else:
    print "error"