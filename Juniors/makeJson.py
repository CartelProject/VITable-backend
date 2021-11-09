import pandas as pd
import json

df_CJ = pd.read_excel(r"Juniors\Courses Juniors.xlsx")
dict_CJ = dict(zip(df_CJ.CourseCode, df_CJ.CourseTitle))

with open(r"Juniors\Juniors.json", "w") as output:
    json.dump(dict_CJ, output)