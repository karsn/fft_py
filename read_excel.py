# -*- coding: utf-8 -*-

import xlrd

from datetime import date,datetime

def read_excel(excel_file,sheet_name,col_num):
#def read_excel():
	#文件位置
	
	ExcelFile=xlrd.open_workbook(excel_file)
	
	#获取目标EXCEL文件sheet名
	
	print ExcelFile.sheet_names()
	
	#------------------------------------
	
	#若有多个sheet，则需要指定读取目标sheet例如读取sheet2
	
	#sheet2_name=ExcelFile.sheet_names()[1]
	
	#------------------------------------
	
	#获取sheet内容【1.根据sheet索引2.根据sheet名称】
	
	#sheet=ExcelFile.sheet_by_index(1)
	
	sheet=ExcelFile.sheet_by_name(sheet_name)
	
	#打印sheet的名称，行数，列数
	
	print sheet.name,sheet.nrows,sheet.ncols
	
	#获取整行或者整列的值
	#
	#rows=sheet.row_values(2)#第三行内容
	#
	cols=sheet.col_values(col_num)#第二列内容
	#
	#print cols,rows
	#
	##获取单元格内容
	#
	#print sheet.cell(1,0).value.encode('utf-8')
	#
	#print sheet.cell_value(1,0).encode('utf-8')
	#
	#print sheet.row(1)[0].value.encode('utf-8')
	#
	##打印单元格内容格式
	#
	#print sheet.cell(1,0).ctype
	
	return cols

if __name__ =='__main__':

	read_excel(r'imu_data_static.xlsx','04',0)
