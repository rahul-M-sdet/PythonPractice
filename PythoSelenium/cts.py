import openpyxl

input_file = r"C:\Users\naveen.kstb\Desktop\PythonDemo1.xlsx"
output_file = r"C:\Users\naveen.kstb\Desktop\PythonDemo1.xlsx"

workbook = openpyxl.load_workbook(input_file)
sheet = workbook.active
sheet['A3'] = "Siva Shankar"

new_row = ["Naveen", "Unknown", "Unknown"]
sheet.append(new_row)

workbook.save(output_file)
print(f"XLSX file '{output_file}' has been successfully created with the modification")