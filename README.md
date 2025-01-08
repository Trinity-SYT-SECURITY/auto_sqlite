# auto_sqlite
create/add/search sqlite db


```
python3 main.py
請輸入 SQLite 資料庫路徑: xxx/xxxx.db

資料表如下:
1. users
2. sqlite_sequence
3. test
4. tokens

請選擇一個表 (輸入編號): 1

表 redeye_users 的欄位如下:
- id (INTEGER)
- username (TEXT)
- password (TEXT)
- test1 (TEXT)
- testid (INTEGER)

可以執行的操作: 
1. 新增記錄
2. 刪除記錄
3. 查詢記錄
請選擇操作 (輸入編號): 2
請輸入刪除條件 (例如: id IN (1, 2, 3)): id IN (1,2,3,4,5,6,7,8)  
刪除成功！
                                      

```

可刪出單一行db資料或是多行、新增、查詢..
