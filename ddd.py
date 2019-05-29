def sqlite_test():
    import sqlite3
    import os

    # 연습이므로, 데이터 파일이 있으면 지우는 코드를 넣읍시다.
    filename = './lab.db'
    try:
        os.remove(filehttps://erica.codeonweb.com/code/b76f4d41-3568-4f1d-a2c5-066167346df8name)
    except OSError:
        pass
    # SQLite DB파일을 생성하거나 연결합니다.
    conn = sqlite3.connect("lab.db")

    # 이후 코드를 채우세요.

if __name__ == "__main__":
    sqlite_test()