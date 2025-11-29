import pandas as pd
import matplotlib.pyplot as plt

#2. What is the relationship between annual leave taken and bonus?
#df_employee_vs_leave = pd.read_csv('EmployeeVSLeave.csv')

#print(df_employee_vs_leave)

df_employee_rate_vs_leave = pd.read_csv('INTERIM PROJECT/Question2/EmployeeRateVSLeave.csv')
print(df_employee_rate_vs_leave)

df_employee_rate_vs_leave = df_employee_rate_vs_leave[df_employee_rate_vs_leave['Bonus'] != 0]
#print(df_employee_rate_vs_leave)

correlation = df_employee_rate_vs_leave['VacationHours'].corr(df_employee_rate_vs_leave['Bonus'])
print("Correlation between sick leave and bonus:", correlation)

# ax = plt.axes()
# ax.set(facecolor = "oldlace")
# #plt.figure(facecolor='oldlace')
# plt.scatter(df_employee_rate_vs_leave['Bonus'], df_employee_rate_vs_leave['VacationHours'], c='darkcyan', alpha=0.8, marker='.', s=2000)
# plt.title('Relationship between Vacation Hours and Bonus($)', fontsize=19)
# plt.xlabel('Bonus($)', fontsize=15)
# plt.ylabel('Vacation Hours', fontsize=15)
# plt.grid()
# plt.text(4250,38,"Correlation between vacation hours and bonus:" + str(round(correlation,3)), fontsize=15, c='red')
# plt.show()



# plt.bar(df_employee_rate_vs_leave['VacationHours'], df_employee_rate_vs_leave['Bonus'])
# plt.title('Employee Vacation Hours vs Bonus')
# plt.xlabel('Vacation Hours')
# plt.ylabel('Bonus($)')
# plt.xlim(20, 40)
# plt.show()


