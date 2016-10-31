import pymssql
import csv
conn = pymssql.connect(server='tia33kx9ix.database.windows.net', user='the_force@tia33kx9ix', password='abc123!@#', database='students')
cursor = conn.cursor()
#cursor.execute('SELECT c.CustomerID, c.CompanyName,COUNT(soh.SalesOrderID) AS OrderCount FROM SalesLT.Customer AS c LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID GROUP BY c.CustomerID, c.CompanyName ORDER BY OrderCount DESC;')
csvfile1 = open('./Movie_Data_Set/SciFi.csv', 'rb')
reader = csv.reader(csvfile1, delimiter=',', quotechar='|')

for row in reader:
	cursor.executemany(
    	"INSERT INTO [dbo].[Table] VALUES (%s, %d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d,%d, %d, %d, %d)",
    	)
# you must call commit() to persist your data if you don't set autocommit to True
conn.commit()

#row = cursor.fetchone()
#while row:
#    print row[0] + " " + str(row[1]) + " " + str(row[2])   
 #   row = cursor.fetchone()