#!--coding:utf8--
import re
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def BaoCunData ( filename , data ):
    # print type(data)
    f = file ( filename , "ab" )
    f.write ( data+',\n' )
    f.close ( )
    # print u'保存成功！'

def Json_GetData ( filename , e , key='' ):
    f = open ( filename , "r" )
    item = []
    for data in f.readlines ( ):
        # print json.loads(data)[e][0]
        item.append(json.loads(data)[e][0])
        if key == 'yes': BaoCunData(filename.replace('json','txt') ,json.loads(data)[e][0])
    return item

def Json_GetItem ( filename ):
    f = open ( filename , "r" )
    item = []
    for data in f.readlines ( ):
        item.append(json.loads(data))
    return item

def Pageurls(filename,e):
    pageurls = []
    for url in Json_GetData(filename,e):
        n = str(url).split('-')[-8]
        # print n,'@'
        for i in range(int(n)):
            # print i,"%"
            pageurls.append( re.sub( r"\d+-0-1-0-0-0-0-0.html" , str( i + 1 ) + '-0-1-0-0-0-0-0.html' , str(url) ) )
    return pageurls
def JsonToTxt(filename1,filename2):
    import json
    f = open(filename1,'r')
    u = open(filename2,'wb')
    for s in f.readlines():
        data =  ''.join(json.loads(s)["DanWeiMingChen"])+'|    '+''.join(json.loads(s)["TongXinDiZhi"])+'|    '+''.join(json.loads(s)["MingChen1"])+'|    '+''.join(json.loads(s)["DianHua1"])+'|    '+''.join(json.loads(s)["ChuanZhen1"])+'|    '+''.join(json.loads(s)["MingChen2"])+'|    '+''.join(json.loads(s)["DianHua2"])+'|    '+''.join(json.loads(s)["ChuanZhen2"])+'|    '
        u.write(data.encode('utf-8')+'\n')
    u.close()
    f.close()

def wenzi(n):
    return ''.join(''.join(''.join(n.split(' ')).split('\t')).split('\n'))

def Json_GetUrl ( filename , e ,html):
    f = open ( filename , "r" )
    for data in f.readlines( ):
        yield json.loads(data)[e]+html
