#%%
import pandas as pd

df = pd.read_excel('SampleData.xlsx', 'SalesOrders', engine="openpyxl")

#%%

regs = df.groupby('Item').agg(
    Order_Date=('OrderDate', (min)),
    Regions=('Region', lambda x: ','.join(x.unique())),
    Total_Units=('Units', 'sum'),
    Mean_Unit_Cost=('Unit Cost', 'mean'),
    Total_Cost=('Total', 'sum')
)
#%%