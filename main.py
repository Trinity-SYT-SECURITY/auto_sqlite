import sqlite3

def list_tables(cursor):
    """列出資料庫中的所有表"""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return [table[0] for table in tables]

def list_columns(cursor, table_name):
    """列出表的所有欄位"""
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    return [(col[1], col[2]) for col in columns]

def add_record(cursor, table_name, columns):
    """新增記錄"""
    values = []
    for col_name, col_type in columns:
        value = input(f"請輸入 {col_name} ({col_type}): ")
        if col_type == "integer":
            value = int(value) if value.isdigit() else None
        values.append(value)
    placeholders = ", ".join(["?" for _ in columns])
    query = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cursor.execute(query, values)

def delete_record(cursor, table_name):
    """刪除記錄（支持多行刪除）"""
    condition = input("請輸入刪除條件 (例如: id IN (1, 2, 3)): ")
    try:
        query = f"DELETE FROM {table_name} WHERE {condition}"
        cursor.execute(query)
        print("刪除成功！")
    except Exception as e:
        print("刪除失敗，錯誤訊息:", e)

def query_table(cursor, table_name):
    """查詢表資料"""
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()
    for record in records:
        print(record)

def main():
    db_path = input("請輸入 SQLite 資料庫路徑(RedDB/managementDB.db): ")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        tables = list_tables(cursor)
        print("\n資料表如下:")
        for i, table in enumerate(tables):
            print(f"{i + 1}. {table}")
        table_index = int(input("\n請選擇一個表 (輸入編號): ")) - 1
        table_name = tables[table_index]

        columns = list_columns(cursor, table_name)
        print(f"\n表 {table_name} 的欄位如下:")
        for col_name, col_type in columns:
            print(f"- {col_name} ({col_type})")

        print("\n可以執行的操作: ")
        print("1. 新增記錄")
        print("2. 刪除記錄")
        print("3. 查詢記錄")
        action = int(input("請選擇操作 (輸入編號): "))

        if action == 1:
            add_record(cursor, table_name, columns)
        elif action == 2:
            delete_record(cursor, table_name)
        elif action == 3:
            query_table(cursor, table_name)
        else:
            print("無效操作，退出程式。")

        conn.commit()
    except Exception as e:
        print("發生錯誤:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
