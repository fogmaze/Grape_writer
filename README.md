# Rememberer
a tool that help to memorize

本地使用
===========
#初始設定
------
1. 請先下載python3  
2. 安裝python依賴:  
   本專案用的所有依賴都寫在requirements.txt中  
   你可以專案跟目錄下執行以下指令來安裝
```
pip install -r .\requirements.txt
```
3. 執行以下指令來創建一個自己的資料庫 (data.db)
```
py createDataBase.py
```

#寫入資料庫
------
執行以下指令:
```
py writer.py
```
  
#抽考
------
執行以下指令:
```
py test.py
```

手機
=====
原理
---
  把資料庫存在手機上，使用有線/無線方式把資料庫檔案傳到電腦，電腦本地使用將更新過的資料庫檔案傳到手機  

無線
----
手機運行 server.py 並確保其一直處於運行狀態  
電腦運行 writer_client.py / tester_client.py
