# LineBotMemo
LineBot筆記。

## 1.Line
到Line developer開通機器人帳號。
## 2.Git
我所選擇的Paas平台Heroku需要用Git作為部屬工具，先裝起來放。可以多裝陸龜gui工具。
## 3.Heroku
提供Paas的平台，同樣先申請帳號。然後下載CLI安裝。
## 4.建立儲存庫
儲存庫的根目錄需要有下面幾個檔案:  
- Procfile  
告訴heroku此app的資訊:類型和要執行的檔案 
- requirements.txt  
告訴heroku需要另外安裝的library
以這個app來說有這些
    - Flask  
    - gunicorn
    - line-bot-sdk

- runtime.txt  
告訴heroku要執行的python版本，可選，heroku會自己選用最新穩定版
## 5.部屬
使用命令提示字元(到app資料夾):  
```
(第一次)
$ git init
$ heroku git:remote -a 你-APP-的名字
$ git add .
$ git commit -m "一些註解"
$ git push heroku master
```
```
(之後)
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
## 5.除錯工具:ngrok
暫略

## 6.參考教學
https://ithelp.ithome.com.tw/users/20120178/ironman/2654


