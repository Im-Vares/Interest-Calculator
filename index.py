import pandas as pd

def read_fuel_elements_from_excel(file_path, sheet_name, element_column, value_column):
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    fuel_elements = df[value_column].tolist()
    num_elements = len(df[element_column])
    element_names = df[element_column].tolist()
    return fuel_elements, num_elements, element_names

def list_gen(list_of_fuel_elements, list_of_percent):
    list_of_percent = [num * 0.01 for num in list_of_percent]
    result = [x * y for x, y in zip(list_of_percent, list_of_fuel_elements)]
    return result

file_path = "C:/Users/Nikita/Music/PythonLearning/Exam File/Element_Configuration.xlsx"
sheet_name = "Sheet1"  
element_column = "Element"  
Specific_Air_column = "Specific_Air"  

list_of_fuel_elements, num_elements, element_names = read_fuel_elements_from_excel(file_path, sheet_name, element_column, Specific_Air_column)

print("Number of elements in Excel file:", num_elements)

list_of_percent = []
for i, element_name in enumerate(element_names):
    element = float(input("Enter element {}: ".format(element_name)))
    list_of_percent.append(element)

result = list_gen(list_of_fuel_elements, list_of_percent)
total_sum = sum(result)

print(result)
print("Total Sum:", total_sum)

