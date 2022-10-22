import requests
import json
from pymongo import MongoClient


URL = "http://openapi.seoul.go.kr:8088/467a696e6b73657236347661676b78/json/tbLnOpendataRtmsV/1/1000/"

response = requests.get(URL)

# f = open(f"response.json", encoding="UTF-8")
raw_data = response.json()
#print(type(raw_data))

HOST = 'cluster0.5ybfoyj.mongodb.net'
USER = 'seul'
PASSWORD = '3379'
DATABASE_NAME = 'rent'
COLLECTION_NAME = 'rent_repos'
MONGO_URI = f"mongodb+srv://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
database = client[DATABASE_NAME]
collection = database[COLLECTION_NAME]
collection.insert_one(document=raw_data)



import pymysql

conn =  pymysql.connect(host='127.0.0.1', 
    user='root', password='3379', db='rent', 
    charset='utf8')


cur = conn.cursor()

cur.execute("""
    DROP TABLE IF EXISTS Apartment,Floors,Gu,Dong, Rent_gbn;
""")



#층수 테이블[층수 id / 층수]_아파트테이블
cur.execute("""
    CREATE TABLE Floors
        (floors_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        floors INT)
""")



#구테이블[구id/ 구]_동테이블
cur.execute("""
    CREATE TABLE Gu 
        (gu_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        gu VARCHAR(20))
""")


#동 태이블[동id/ 동]_아파트테이블
cur.execute("""
    CREATE TABLE Dong 
        (dong_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        dong VARCHAR(20),
        gu_id INT,
        FOREIGN KEY (gu_id) REFERENCES Gu (gu_id) ON UPDATE CASCADE)
""")


#아파트(아파트 고유번호,아파트이름,동id,전/월/매id/층수id/가격)
cur.execute("""
    CREATE TABLE Apartment 
        (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
        apartment_name VARCHAR(20), 
        dong_id INT ,
        floors_id INT ,
        price INT,
        FOREIGN KEY (floors_id) REFERENCES Floors (floors_id) ON UPDATE CASCADE,
        FOREIGN KEY (dong_id) REFERENCES Dong (dong_id) ON UPDATE CASCADE) 
""")
conn.commit()


docs = collection.find_one({})


for doc in docs:
#     # 뭔가 문제인지 모르겠지만,, 문자형태는 저렇게 \"{}\" 해야 작동이 된다..
#     # User 테이블에 데이터 넣기
    cur.execute(f"""
         INSERT OR IGNORE INTO Floors (floors) VALUES 
         ({doc['tbLnOpendataRtmsV']['row']['FLOOR']});
     """)

