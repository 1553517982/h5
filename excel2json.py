import os
import sys
import re
import xlrd
from collections import OrderedDict
import json
import codecs


def checkExcelFile(filePath,fileName):
	wb = xlrd.open_workbook(filePath)
	shName = wb.sheet_names()[0]
	sh = wb.sheet_by_index(0)
        title = sh.row_values(0)
        convert_list = []
        print shName
        for rownum in range(6, sh.nrows):
                rowvalue = sh.row_values(rownum)
                single = OrderedDict()
                for colnum in range(1, len(rowvalue)):
                        single[title[colnum]] = rowvalue[colnum]
                convert_list.append(single)
        j = json.dumps(convert_list,ensure_ascii=False)

        with codecs.open(shName+'.json',"w","utf-8") as f:
                f.write(j)
        
def checkPathExcel(path, file_types):
    for file in os.listdir(path):
        filepath = path + "//"+file 
        if os.path.isdir(filepath):
            checkPathExcel(filepath, file_types)
        elif os.path.isfile(filepath):
            splitlist = filepath.split('.')
            m = len(splitlist)
            prefx = splitlist[m-1]
            
            if prefx in file_types:
                checkExcelFile(filepath,file)
                
file_type_list = ["xlsm","xlsx"]

if __name__ == '__main__':
    checkPathExcel(".", file_type_list)
    os.system("pause")
    

