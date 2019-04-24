#author PGKSUNILKUMAR
import pandas as pand
import numpy as nump
import xlsxwriter

def getRowValues(d):      
    ones = d.sum(axis=0)
    row = d.count()
    zeros = row-ones 
    Entropy= -(zeros/row)*nump.log2(zeros/row) -(ones/row)*nump.log2(ones/row)
    E = Entropy.fillna(0)
    return float(E)

def Info_Gain(clmn, res):
    first_row_id = [i for i , n in enumerate(clmn) if n==1]
    zeroth_row_id = [i for i , n in enumerate(clmn) if n==0]
    first_row_cnt = len(first_row_id)
    zeroth_row_cnt = len(zeroth_row_id)
    total_cnt = clmn.count()
    column_l = pand.DataFrame(data=res, index=first_row_id, dtype=int)
    column_row = pand.DataFrame(data=res, index=zeroth_row_id, dtype=int)
    
    entity_pass = getRowValues(res)
    entity_last = getRowValues(column_l)
    entity_row = getRowValues(column_row) 
    ig = entity_pass - (first_row_cnt/total_cnt)*entity_last - (zeroth_row_cnt/total_cnt)*entity_row
    return ig


# Creating a excel file with Bits Name
BITSROLL_ID = "2018HT12060"
number_of_filesFolder = 56
writer1 = pand.ExcelWriter(BITSROLL_ID+'_infogain.xlsx', engine='xlsxwriter')
for i in range(1,number_of_filesFolder+1):
    csv_allfile = "data/"+str(i)+".csv"
    primarydata = datafile = pand.read_csv(csv_allfile, header=None)
    m=primarydata.median()
    dataset = pand.DataFrame(primarydata>m, dtype=int)
    dataset[20] = primarydata[20] 
    res = pand.DataFrame(data=dataset[20])
    ig = list()
    for f in range(20):
        clmn = dataset[f]
        ig.append(Info_Gain(clmn, res))
    datafile = pand.DataFrame({"Information gain":ig}, index=range(1,21))
    datafile.to_excel(writer1, sheet_name=str(i)+"_csv")
    print(csv_allfile)
    print(datafile)
    
    
writer1.save()