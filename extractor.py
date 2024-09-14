import ifcopenshell
import ifcopenshell.util.element as Element
import pandas as pd


def extract_bep_data_from_ifc_file(input_filename: str, input_directory: str, output_directory: str) -> bool:
    ifc_file = ifcopenshell.open(input_directory + input_filename)

    class_name = "IfcBuildingElementProxy"

    output_file_path: str = output_directory + input_filename.split(".")[0] + ".xlsx"

    with pd.ExcelWriter(output_file_path, engine="openpyxl") as writer:
        objects = ifc_file.by_type(class_name)
        result_df = pd.DataFrame()

        for object in objects:
            class_data = {}
            # Get dict of properties and values
            psets = Element.get_psets(object)
            for _, value in psets.items():
                if isinstance(value, dict):
                    for key, val in value.items():
                        class_data[key] = val
                else:
                    pass
            class_df = pd.DataFrame(class_data, index=[0])
            result_df = pd.concat([result_df, class_df], ignore_index=True)

        result_df.to_excel(writer, sheet_name=class_name, index=False)

        # Set auto fit column width
        worksheet = writer.sheets[class_name]
        for _, col in enumerate(worksheet.columns):
            worksheet.column_dimensions[col[0].column_letter].width = 20

        return True
