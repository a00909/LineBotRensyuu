from __future__ import unicode_literals
import os
import pprint
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, VideoSendMessage, LocationSendMessage

class noteHandler:
    noteBook = []
    def __init__(self) -> None:
        pass

    def addNote(self,content:str):
        reply = ""
        try:
            note = {}

            note["id"] = len(self.noteBook) 
            note["content"] = content
            
            self.noteBook.append(note)
            reply = "succeeded"
        except:
            reply = "failed"
        
        return reply

    def removeNote(self,key):
        iKey = int(key)
        reply = ""
        if iKey >=0 and iKey<len(self.noteBook):
            del self.noteBook[iKey]
            reply = "succeeded"
        else:
            reply = "failed"
        return reply

    def getNote(self):
        return str(self.noteBook)

def parseNoteOperation(message:str):
    op = message.split()
    return op

def decideNoteOperation(op:list,nh:noteHandler) -> str:
    if op[0] == "add":
        return nh.addNote(op[1])
    elif op[0] == "remove":
        return nh.removeNote(op[1])
    elif op[0] == "show":
        return nh.getNote()
    else:
        return "no such operation"

nh = noteHandler()

pp = pprint.PrettyPrinter(indent=4)

app = Flask(__name__)

# LINE 聊天機器人的基本資料
# LINE 的 channel_access_token, channel_secret 換成在 Line Developer 裡的資料

line_bot_api = LineBotApi('oaohXzEPycUDWuIpl8ZcPXCBU+ULkKMgRY8hEUm2sHjBcuaoIcracp5LzfFYccUoJitxMjpANmiXVG0cq3NadEyFE+vaNlF6uU+Auep3lmA05COvmwHARojBTQ3lHwnWVxQYln0nTm37RIlWG7bowwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('fb726949ac3ada1a4050cc550a81ee93')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    #print("[DEBUG]body:",body)
    #print("[DEBUG]signature:",signature)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# 回傳 LINE 的資料
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef": #因為LINE有些預設資料,我們在此排除
        try:
            
            #event.message.text = user傳的訊息
            #pp.pprint(event)
            reply = decideNoteOperation(parseNoteOperation(event.message.text),nh)

            # 回訊息
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=reply)
                # TextSendMessage(text=event.message.text) #鸚鵡說話
            )
            '''
            # 回圖片
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg",
                    preview_image_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg"
                )
            )

            # 回影片
            VideoSendMessage(
              original_content_url='https://www.youtube.com/watch?v=NxOph87AtGc',
              preview_image_url='https://i.ytimg.com/vi/NxOph87AtGc/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAnNrD2Lewo_HJFJNEt1eejHd5U1w'
            )

            # 回地址
            LocationSendMessage(
              title='my location',
              address='Tokyo',
              latitude=35.65910807942215,
              longitude=139.70372892916203
            )
            '''
        except:

            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(
                    original_content_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg",
                    preview_image_url="https://onepage.nownews.com/sites/default/files/2020-05/%E9%A6%96%E9%A0%81%E5%B0%81%E9%9D%A2-%E3%80%8C%E5%8F%AF%E6%86%90%E5%93%AA%E3%80%8D%E3%80%81%E3%80%8C%E9%BB%91%E4%BA%BA%E5%95%8F%E8%99%9F%E3%80%8D%E3%80%81%E3%80%8C%E6%88%91%E5%B0%B1%E7%88%9B%E3%80%8D%E9%80%99%E4%BA%9B%E6%A2%97%E5%9C%96%E7%9A%84%E7%94%B1%E4%BE%86%E4%BD%A0%E7%9F%A5%E9%81%93%E5%97%8E%EF%BC%9F.jpg"
                )
            )

if __name__ == "__main__":
    app.run()