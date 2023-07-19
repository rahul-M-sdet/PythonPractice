import openpyxl
# to load the Excel file
Book1=openpyxl.load_workbook("C:\\Users\\rahul.m\\Desktop\\Book1.xlsx")

# specify the sheet name
sheet=Book1['Sheet1']

# read the data from excel
value=sheet['A1'].value
print("value in cell A1: ",value)