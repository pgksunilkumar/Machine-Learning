import csv
import xlrd
from database.database import  mydb, mycursor, predwdbcursor
filename = "schedule.xlsx"
tableNameSplit = filename.split('.') 
 
# Xlsx File to SQL Insert Generate and execute the SQL
def xlsxFile():
	book=xlrd.open_workbook(filename)
	sheet=book.sheet_by_index(0) 
	excelHeader = []
	for i in range(sheet.nrows):
		if(i != 0):			
			data = []
			for j in range(sheet.ncols):		 
				data.append(str(sheet.cell_value(i, j)))
			insert =  "insert into "+str(tableNameSplit[0])+" ("
			headerLength = len(excelHeader)
			k = 0
			while(k <= headerLength-2):
				insert = insert + excelHeader[k] + ', '
				k = k + 1
			insert = insert + excelHeader[k] + ") values ("
			
			val = 0
			columnLength = len(data)
			while(val <= columnLength-2):
				insert = insert + "%s" + ', '
				val = val + 1
			insert = insert + "%s" + ")" 
			mycursor.execute(insert, data)
			print("Successfully Inserted the DB")
		else:
			for j in range(sheet.ncols):	
				excelHeader.append(sheet.cell_value(0,j)) 

# csv File to SQL Insert Generate and execute the SQL
def csvFile():
	openFile = open(filename, 'r')
	csvFile = csv.reader(openFile)
	header = next(csvFile)
	headers = map((lambda x: '`'+x+'`'), header)
	insert = 'INSERT INTO '+tableNameSplit[0]+' (' + ", ".join(headers) + ") VALUES " 
	for row in csvFile:
	    values = map((lambda x: '"'+x+'"'), row)
	    myString = insert +"("+ ", ".join(values) +");"  
	    mycursor.execute(myString) 
	    print("Successfully Inserted the DB")

if(tableNameSplit[1] == 'csv'):
	csvFile()
elif(tableNameSplit[1] == 'xlsx'):
	xlsxFile()

mydb.commit() 