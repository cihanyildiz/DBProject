import sys
from postgres import PostgresSql

x = PostgresSql("gis", "postgres", "60", "localhost", "5432")
cursor = x.get_connection().cursor()
cursor.execute("SELECT *FROM DENEME_TABLE")
mobile_records = cursor.fetchall()
for row in mobile_records:
    print("", row[0],)
    print("", row[1])
    print("", row[2], "\n")

print(2)
