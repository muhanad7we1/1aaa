#!/usr/bin/python3
email="pywpest488@usbcspot.com"
password="000000"
url="http://aminoapps.com/p/xqjkusc"
'''
حط اي رابط من المنتدى ، المهم 
يكون من المنتدى الي انت تبيه 

'''
from ast import literal_eval
from os import system
import signal
from os import _exit
system("clear")
def signal_handler(sig, frame):
    print('\nYou pressed Ctrl+C!')
    _exit(1)
signal.signal(signal.SIGINT, signal_handler)
print('if you need to exit\nPress Ctrl+C\n\nwaiting ..\n')



system("pip3 install -U Amino.py pip")
import amino
infoos=url
infoo=amino.Client().get_from_code(infoos)
comId=infoo.path[1:infoo.path.index("/")]

system("clear")
connn=False
while connn==False:
    lines = []
    print("paste your comment here :\n\nif you finish type : @end")
    while True:
        line = input()
        if line.strip()=="@end":
            break
        else:
            lines.append(line)
    comment = "\n".join(lines)
    comment=comment.strip()
    xcv=input("\nthis is your comment are you sure ? \n\nto be continue? y/n : ")
    if xcv=="y":
        connn=True
client=None
sub_c=None
def logino():
    global client
    global sub_c
    client=amino.Client()
    client.login(email=email,password=password)
    sub_c=amino.SubClient(comId=comId,profile=client.profile)
logino()
nnn=0
listob=[]
listor=[]

while True:
    blogIds=sub_c.get_recent_blogs(start=0,size=20)
    for blogId,ref in zip(blogIds.blogId,blogIds.refObjectId):
        g=False
        if blogId in listob or ref in listor:pass
        else:
            try:
                nnn=nnn+1
                if ref==None:
                    ref=blogId
                    g=True
                if g==True:
                    sub_c.like_blog(blogId=[ref])
                else:
                    sub_c.like_blog(wikiId=ref)
                print(str(nnn)+") - "+str(ref)+" liked")
            except Exception as e:
                if hasattr(e, 'message'):
                    mess=str(e.message)
                    print(e.message)
                else:
                    mess=str(e)
                    dc=literal_eval(mess)
                    if dc.get("api:statuscode")==105:
                        logino()
                        print("re-login")
                print("error")
            try:
                if ref==None:
                    ref=blogId
                if g==True:
                    sub_c.comment(message=comment,blogId=ref)
                else:
                    sub_c.comment(message=comment,wikiId=ref)
                print(str(nnn)+") - "+str(ref)+" commented")
            except:
                print("error")
            if g==False:
                listor.append(ref)
            else:
                listob.append(blogId)
    print("\n\nnext\n\n")
    
