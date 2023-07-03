import pandas as pd
import streamlit as st

def read_fuel_elements_from_excel(df, element_column, value_column):
    fuel_elements = []
    element_names = []

    for element, value in zip(df[element_column], df[value_column]):
        try:
            numeric_value = float(value)
            fuel_elements.append(numeric_value)
            element_names.append(element)
        except ValueError:
            continue

    num_elements = len(fuel_elements)

    return fuel_elements, num_elements, element_names


def list_gen(list_of_fuel_elements, list_of_percent):
    list_of_percent = [num * 0.01 for num in list_of_percent]
    result = [x * y for x, y in zip(list_of_percent, list_of_fuel_elements)]
    return result

def main():
    st.title("Fuel Data Calculation")
    st.write("Upload an Excel file with the fuel elements and their values.")

    file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if file is not None:
        df = pd.read_excel(file)
        element_column = st.selectbox("Select Element Column", df.columns)
        value_column = st.selectbox("Select Value Column", df.columns)

        list_of_fuel_elements, num_elements, element_names = read_fuel_elements_from_excel(df, element_column, value_column)

        st.write("Number of elements in Excel file:", num_elements)

        list_of_percent = []
        for i, element_name in enumerate(element_names):
            element = st.number_input("Enter percentage for {}:".format(element_name), min_value=0.0, max_value=100.0, value=0.0, step=0.1)
            list_of_percent.append(float(element))  # Convert to float


        result = list_gen(list_of_fuel_elements, list_of_percent)
        total_sum = sum(result)

        st.write("Result:", result)
        st.write("Total Sum:", total_sum)

        output_df = pd.DataFrame({"Element": element_names, "Percentage": list_of_percent, "Result": result})
        st.write("Download Result Table")
        st.download_button(label="Download", data=output_df.to_csv(index=False), file_name="result_table.csv")

if __name__ == "__main__":
    main()