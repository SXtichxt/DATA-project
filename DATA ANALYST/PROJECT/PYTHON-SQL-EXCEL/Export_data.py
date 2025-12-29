import mysql.connector
from openpyxl import Workbook
#DATABASE
db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = '393854321',
    database = 'i_want_to_buy'
)

cursor = db.cursor()
sql = '''
    select *
    from products;
'''
cursor.execute(sql)
products = cursor.fetchall()


#EXCEL
workbook = Workbook()
sheet = workbook.active
sheet.append(['ID','PRODUCTNAME','PRICE','NECESSARY','CREATE_DATE'])

for p in products:
    print(p)
    sheet.append(p)

workbook.save(filename = 'exported.xlsx')