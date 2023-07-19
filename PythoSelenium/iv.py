import openpyxl

inputFile = "C:\\Users\\rahul.m\\Desktop\\PythonDemo.xlsx"
outputFile = "C:\\Users\\rahul.m\\Desktop\\PythonDemo.xlsx"

workbook = openpyxl.load_workbook(inputFile)
Sheet1=workbook.active
Sheet1['A3'] = 'Naveen kumar'

new_row =['Deepak' , 'unknown' , 'unknown']
Sheet1.append(new_row)

workbook.save(outputFile)
print("file has been successfully created with modification")

