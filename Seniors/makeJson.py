import pandas as pd
import json

df_NCC = pd.read_excel(r"Seniors\Non Credit Courses Seniors.xlsx")
df_PC = pd.read_excel(r"Seniors\Programme Core Seniors.xlsx")
df_PE = pd.read_excel(r"Seniors\Programme Elective Seniors.xlsx")
df_UC = pd.read_excel(r"Seniors\University Core Seniors.xlsx")
df_UE = pd.read_excel(r"Seniors\University Elective Seniors.xlsx")

dict_NCC = dict(zip(df_NCC.CourseCode, df_NCC.CourseTitle))
dict_PC = dict(zip(df_PC.CourseCode, df_PC.CourseTitle))
dict_PE = dict(zip(df_PE.CourseCode, df_PE.CourseTitle))
dict_UC = dict(zip(df_UC.CourseCode, df_UC.CourseTitle))
dict_UE = dict(zip(df_UE.CourseCode, df_UE.CourseTitle))

course_dict = dict_NCC | dict_PC | dict_PE | dict_UC | dict_UE

with open(r"Seniors\Seniors.json", "w") as output:
    json.dump(course_dict, output)
