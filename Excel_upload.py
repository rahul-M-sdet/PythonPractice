import openpyxl

input_file=r"C:\Users\RAHUL\Desktop\rahul.xlsx"
output_file=r'C:\Users\RAHUL\Desktop\rahul.xlsx'

workbook=openpyxl.load_workbook(input_file)
Sheet1=workbook.active

Sheet1['A3']="Naveen Kumar"

new_row=["Deepak","unknown","unknown"]
Sheet1.append(new_row)

workbook.save(output_file)

print(f"{output_file} data has been modified and save successfully")