import matplotlib.pyplot as plt
import pandas as pd


choose = input("Do you want to see stadistics about ECUADOR? Write ECUADOR: ")

chose = choose.upper()

if chose == "ECUADOR":
    b = pd.read_excel(r"C:\Users\Tomas\Desktop\database2.xlsx", sheet_name="ECUADOR",usecols="A, C, D", skiprows=2, skipfooter=71310)
    display = int(input("Do you want to display it on 1(BAR) or 2(PIE), select a number: "))
    if display == 1:
        
        plt.bar(b["Empresa"], b["Empleados"], width=0.5)
        plt.xticks([])
        plt.show()
    elif display == 2:
        plt.pie(b["Empleados"], labels=b["Empresa"])
        plt.show()
    else:
        print("An Error Has Happened.")