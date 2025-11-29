import pandas as pd
import matplotlib.pyplot as plt


#6. What is the relationship between the size of the stores, number of employees and revenue?
df_store_size_employees = pd.read_csv('INTERIM PROJECT/Question6/StoreSizevsEmployees.csv')

print(df_store_size_employees.head(20))

correlation = df_store_size_employees[['AnnualRevenue','SquareFeet','NumberEmployees']].corr()
print(correlation)

# correlation.plot(kind='bar', x=('SquareFeet'), y=('NumberEmployees'))
# plt.show()

# plt.figure()
# plt.scatter(df_store_size_employees['SquareFeet'], df_store_size_employees['NumberEmployees'], alpha=0.6)
# plt.show()



#stacked vertically
# fig, (ax1, ax2, ax3) = plt.subplots(3)
# fig.suptitle('Relationship between Store size, Number of employees and Annual Revenue')
# ax1.scatter(df_store_size_employees['SquareFeet'], df_store_size_employees['NumberEmployees'], alpha=0.4, c='lightcoral')
# ax1.set_xlabel('Store Size (sqft)')
# ax1.set_ylabel('Number of Employees')
# ax2.scatter(df_store_size_employees['SquareFeet'], df_store_size_employees['AnnualRevenue'], alpha=0.4, c='slateblue')
# ax2.set_title('Store size vs Annual Revenue')
# ax3.scatter(df_store_size_employees['AnnualRevenue'], df_store_size_employees['NumberEmployees'], alpha=0.4, c='seagreen')
# plt.show()


#stacked horizontally
fig, (ax1, ax2, ax3) = plt.subplots(1,3)
plt.subplots_adjust(wspace=0.5)
fig.suptitle('Relationship between Store size, Number of employees and Annual Revenue', fontsize=19)
#fig.set_facecolor('gold')
ax1.scatter(df_store_size_employees['SquareFeet'], df_store_size_employees['NumberEmployees'], alpha=0.4, c='lightcoral')
ax1.set_title('Store Size vs Number of Employees', fontsize=15)
ax1.set_xlabel('Store Size (sqft)', fontsize=12)
ax1.set_ylabel('Number of Employees', fontsize=12)
ax1.set_facecolor('oldlace')
ax2.scatter(df_store_size_employees['SquareFeet'], df_store_size_employees['AnnualRevenue'], alpha=0.4, c='slateblue')
ax2.set_title('Store size vs Annual Revenue', fontsize=15)
ax2.set_xlabel('Store Size (sqft)', fontsize=12)
ax2.set_ylabel('Annual Revenue ($)', fontsize=12)
ax2.set_facecolor('oldlace')
ax3.scatter(df_store_size_employees['AnnualRevenue'], df_store_size_employees['NumberEmployees'], alpha=0.4, c='seagreen')
ax3.set_title('Annual Revenue vs Number of Employees', fontsize=15)
ax3.set_xlabel('Annual Revenue ($)', fontsize=12)
ax3.set_ylabel('Number of Employees', fontsize=12)
ax3.set_facecolor('oldlace')
plt.show()