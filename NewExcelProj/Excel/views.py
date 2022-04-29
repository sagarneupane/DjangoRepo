from django.shortcuts import render

import pandas as pd
import openpyxl


# Create your views here.

def home(request):
    df_2 = pd.read_excel("E:/MyPythonWebApp/DjangoCRUD/NewExcelProj/Excel/projExcel.xlsx", index_col=0, sheet_name=1)

    print(df_2["Income"])
    return render(request, 'Excel/index.html', {"df": df_2})
