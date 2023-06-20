import pandas as pd

sales = pd.read_csv('Sales.csv')
print(sales.info())
profit = sales['Revenue'].sum() - sales['Cost'].sum()
print(profit)

sales = sales.assign(
    Profit=lambda x: x['Revenue'] - x['Cost'],
    profit_per_unit=lambda x: x['Profit']/x['Quantity_Sold']
)

print(
    sales.groupby('Product')['Profit'].sum().sort_values(ascending=False)
)

returns = pd.read_csv('Returns.csv')

df = sales.merge(returns, on=['Product', 'Month'], how='left')
print(
    df.groupby('Product')\
    .apply(lambda x: x['Revenue'].sum() - x['Refund_Amt'].sum())
)