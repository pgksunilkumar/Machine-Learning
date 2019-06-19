import xlrd
from database.database import  mydb, mycursor, predwdbcursor
filename = "schedule.xlsx"
tableNameSplit = filename.split('.')
book=xlrd.open_workbook(filename)
sheet=book.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)
excelHeader = []
for i in range(sheet.nrows):
	if(i != 0):			
		data = []
		for j in range(sheet.ncols):		
			# print(sheet.cell_value(0,i), sheet.cell_value(i,j))
			data.append(str(sheet.cell_value(i, j)))
			# print(sheet.cell_value(0,j), sheet.cell_value(i, j))
		# print(data)
		# print(excelHeader[0])
		# print(data[0])

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
		# print(insert)
		# print(data)
		mycursor.execute(insert, data)

		print("Successfully Inserted")
	else:
		for j in range(sheet.ncols):	
			excelHeader.append(sheet.cell_value(0,j))
mydb.commit()
# print(excelHeader)

