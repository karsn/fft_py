# -*- coding: utf-8 -*-

import xlrd

from datetime import date,datetime

def read_excel(excel_file,sheet_name,col_num):
#def read_excel():
	#�ļ�λ��
	
	ExcelFile=xlrd.open_workbook(excel_file)
	
	#��ȡĿ��EXCEL�ļ�sheet��
	
	print ExcelFile.sheet_names()
	
	#------------------------------------
	
	#���ж��sheet������Ҫָ����ȡĿ��sheet�����ȡsheet2
	
	#sheet2_name=ExcelFile.sheet_names()[1]
	
	#------------------------------------
	
	#��ȡsheet���ݡ�1.����sheet����2.����sheet���ơ�
	
	#sheet=ExcelFile.sheet_by_index(1)
	
	sheet=ExcelFile.sheet_by_name(sheet_name)
	
	#��ӡsheet�����ƣ�����������
	
	print sheet.name,sheet.nrows,sheet.ncols
	
	#��ȡ���л������е�ֵ
	#
	#rows=sheet.row_values(2)#����������
	#
	cols=sheet.col_values(col_num)#�ڶ�������
	#
	#print cols,rows
	#
	##��ȡ��Ԫ������
	#
	#print sheet.cell(1,0).value.encode('utf-8')
	#
	#print sheet.cell_value(1,0).encode('utf-8')
	#
	#print sheet.row(1)[0].value.encode('utf-8')
	#
	##��ӡ��Ԫ�����ݸ�ʽ
	#
	#print sheet.cell(1,0).ctype
	
	return cols

if __name__ =='__main__':

	read_excel(r'imu_data_static.xlsx','04',0)
