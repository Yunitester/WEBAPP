# 登录地址
def geturl(url):
    urls=url.split('/')
    url=urls[0]+'/'+urls[1]+'/'+urls[2]+'/'+urls[3]+'/'
    return url

testurl=geturl('http://localhost/phpwind')+'login'
