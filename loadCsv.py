import csv
from database.database import  mydb, mycursor, predwdbcursor
filename = "sheet2.csv"
tableNameSplit = filename.split('.')
# print(tableNameSplit[0]) 
openFile = open(filename, 'r')
csvFile = csv.reader(openFile)
header = next(csvFile)
headers = map((lambda x: '`'+x+'`'), header)
insert = 'INSERT INTO '+tableNameSplit[0]+' (' + ", ".join(headers) + ") VALUES "
# openFileSave = open("sheet1.sql", 'w')
for row in csvFile:
    values = map((lambda x: '"'+x+'"'), row)
    myString = insert +"("+ ", ".join(values) +");" 
    # print (insert +"("+ ", ".join(values) +");" )    
    # openFileSave.write(myString + "\n")    
    mycursor.execute(myString) 
    print("Inserted the DB")
mydb.commit()
# openFile.close()
# openFileSave.close() 